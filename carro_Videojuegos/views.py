from django.shortcuts import render

from .carro_Videojuegos import CARRO_videojuegos 

from megagames.models import Videojuego

from django.shortcuts import redirect
 

# Create your views here.

def agregar_videojuego(request, videojuego_id):
    # Crear una instancia del carro de la compra
    carroV = CARRO_videojuegos(request)
    
    # Obtener el objeto Videojuego por su id
    productoJ = Videojuego.objects.get(id=videojuego_id)
    
    # Agregar el videojuego al carro (dependiendo de cómo esté definido el método agregar_videojuegos)
    carroV.agregar_videojuegos(productoJ)
    
    # Redirigir a la vista 'juego' (reemplaza 'juego' con el nombre de tu vista destino)
    return redirect("juego")



def eliminar_videojuego(request, videojuego_id):
    
    #se envia la request (clase.request) a una variable 
    carroV = CARRO_videojuegos(request)
    
    productoJ=Videojuego.objets.get(id=videojuego_id)
    
    carroV.eliminar_videojuegos(productoJ=Videojuego)
    
    return redirect("juego")



def restar_videojuego(request, videojuego_id):
    
    #se envia la request (clase.request) a una variable 
    carroV = CARRO_videojuegos(request)
    
    productoJ=Videojuego.objets.get(id=videojuego_id)
    
    carroV.restar_videojuegos(productoJ=Videojuego)
    
    return redirect("juego")



def limpiar_carro_videojuegos(request, videojuego_id):
    
    #se envia la request (clase.request) a una variable 
    carroV = CARRO_videojuegos(request)
    
    carroV.limpiar_carro_videojuegos()
    
    return redirect("juego")





