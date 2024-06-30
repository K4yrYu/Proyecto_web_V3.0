from django.urls import path
from . import views

app_name="carro_Videojuegos"



urlpatterns = [ 
    
    #se identifica con add_GAME, etc...  para no confundir con otras funciones
    path("add_GAME/<int:videojuego_id>/", views.agregar_videojuego, name="add_GAME"),
    #path("eliminar/<int:videojuego_id>/", views.eliminar_videojuego, name="del_GAME"),
    #path("restar/<int:videojuego_id>/", views.restar_videojuego, name="minus_GAME"),
    #path("limpiar", views.limpiar_carro_videojuegos, name="clean_GAME"),
    
    
]

    

    