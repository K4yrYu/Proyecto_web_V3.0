#creacion de variables globales

#acumulador del preico final (repetir para consola y videojuegos)
#al repetir sumar a la misma variable

def valor_final_carrito(request):
    precio_final = 0
    if request.user.is_authenticated:
        if "carro_Videojuegos" in request.session:
            for key, value in request.session["carro_Videojuegos"].items():
                precio_final += float(value["precio"]) * value["stock"]
    return {"valor_final_carrito": precio_final}
