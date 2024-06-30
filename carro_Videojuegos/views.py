from django.shortcuts import render

from .carro_Videojuegos import CARRO_videojuegos 

from megagames.models import videojuego

from django.shortcuts import redirect
 

# Create your views here.

def agregar_videojuego(request, videojuego_id):
    
    #se envia la request (clase.request) a una variable 
    carroV = CARRO_videojuegos(request)
    
    productoJ=videojuego.objets.get(id=producto_id)
    
    carroV.agregar(productoJ=videojuego)
    
    return redirect("juego")

#resto en proceso



