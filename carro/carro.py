#creacion estructura del carrito
class carro:
    def _init_(self,request):
        self.request=request
        self.request=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        else:
            self.carro=carro
        
    #funcion para agregar productos al carro
    def agregar(self,producto):
        if(str(producto.id) not in self.carro.keys()):
            self.carro[producto.id]={
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carro()
        
    #funcion para guardar el carro segun la sesion
    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True
    
    #funcion para eliminar el carro segun la sesion    
    def eliminar(self,producto):
        producto.id=str(producto.id)
        if producto.id in self.carro:
            del self.carro[producto.id]
            self.guardar_carro()
    
    
    #funcion para restar del carrito 1 producto
    def restar_producto(self,producto):
            for key, value in self.carro.items():
                if key==str(producto.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(producto)
                    break
        self.guardar_carro()
        
    
    #limpiar el carro al cerrar la sesion 
    def limpiar_carro(self):
        carro=self.session["carro"]={}
        self.session.modified=True
        
    
    