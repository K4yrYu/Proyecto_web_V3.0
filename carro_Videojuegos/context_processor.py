#creacion de variables globales

#acumulador del preico final (repetir para consola y videojuegos)
#al repetir sumar a la misma variable

def valor_final_carrito(request):
    precio_total = calcular_precio_total(request)
    return {"valor_final_carrito": precio_total}

def calcular_precio_total(request):
    precio_total = 0
    if request.user.is_authenticated:
        if "CARRO_videojuegos" in request.session:
            for key, value in request.session["CARRO_videojuegos"].items():
                precio_total += float(value["precio"]) * value["Stock"]
    return precio_total
