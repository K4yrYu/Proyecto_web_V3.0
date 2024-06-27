from django.urls import path
from . import views

urlpatterns = [ 
    path('index' , views.index , name="index" ),
    path('juego' , views.juego , name="juego" ),
    path('consolas' ,views.consolas , name="consolas" ),
    path('jugetes' ,views.jugetes , name="jugetes" ),
    path('contacto' ,views.contacto , name="contacto" ),
    path('perfil' ,views.perfil , name="perfil" ),
    ]