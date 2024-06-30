

#creacion estructura del carrito
class CARRO_videojuegos:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro_videojuegos = self.session.get("CARRO_videojuegos")
        if not carro_videojuegos:
            carro_videojuegos = self.session["CARRO_videojuegos"] = {}
        self.CARRO_videojuegos = carro_videojuegos

    def agregar_videojuegos(self, videojuego):
        videojuego_id = str(videojuego.id)
        if videojuego_id not in self.CARRO_videojuegos:
            self.CARRO_videojuegos[videojuego_id] = {
                "videojuego_id": videojuego.id,
                "nombre": videojuego.nombre,
                "precio": str(videojuego.precio),
                "Stock": 1,
                "imagen": videojuego.imagen.url,
            }
        else:
            self.CARRO_videojuegos[videojuego_id]["Stock"] += 1

        self.guardar_carro_videojuegos()
    
        
    #funcion para guardar el carro segun la sesion
    def guardar_carro_videojuegos(self):
        self.session["CARRO_videojuegos"]=self.CARRO_videojuegos
        self.session.modified=True
    
    
    #funcion para eliminar el carro segun la sesion    
    def eliminar_videojuegos(self,videojuego):
        videojuego.id = str(videojuego.id)
        if videojuego.id in self.CARRO_videojuegos:
            del self.CARRO_videojuegos[videojuego.id]
            self.guardar_carro_videojuegos()
    
    
    #funcion para restar del carrito 1 producto
    def restar_videojuegos(self,videojuego):
            for key, value in self.CARRO_videojuegos.items():
                if key==str(videojuego.id):
                    value["stock"]=value["stock"]-1
                    if value["stock"]<1:
                        self.eliminar_videojuegos(videojuego)
                    break
            self.guardar_carro_videojuegos()
        
    
    #limpiar el carro al cerrar la sesion 
    def limpiar_carro_videojuegos(self):
        CARRO_videojuegos=self.session["CARRO_videojuegos"]={}
        self.session.modified=True
        