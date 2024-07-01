

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
    
        
    # Función para restar productos del carro
    def restar_videojuegos(self, videojuego):
        for key, value in self.CARRO_videojuegos.items():
            if key == str(videojuego.id):
                if value["Stock"] > 1:
                    value["Stock"] -= 1
                else:
                    self.eliminar_videojuegos(videojuego)
                break
        self.guardar_carro_videojuegos()
    
    # Función para eliminar productos del carro
    def eliminar_videojuegos(self, videojuego):
        videojuego_id = str(videojuego.id)
        if videojuego_id in self.CARRO_videojuegos:
            del self.CARRO_videojuegos[videojuego_id]
            self.guardar_carro_videojuegos()
    
    # Función para limpiar el carro
    def limpiar_carro_videojuegos(self):
        self.session["CARRO_videojuegos"] = {}
        self.session.modified = True

    # Función para guardar el carro en la sesión
    def guardar_carro_videojuegos(self):
        self.session["CARRO_videojuegos"] = self.CARRO_videojuegos
        self.session.modified = True
        
        
############################################################

#apartado exclusivo para sumar y restar desde el carrito

        