from django.urls import path
from . import views

urlpatterns = [ 
    path('index' , views.index , name="index" ),
    path('juego' , views.juego , name="juego" ),
    path('consolas' ,views.consolas , name="consolas" ),
    path('jugetes' ,views.jugetes , name="jugetes" ),
    path('contacto' ,views.contacto , name="contacto" ),
    path('perfil' ,views.perfil , name="perfil" ),
    path('carrito' ,views.carrito , name="carrito" ),
    path('jugete/<str:nombre>/', views.detalle_jugete, name='detalle_jugete'),
    path('juego/<str:nombre>/', views.detalle_juego, name='detalle_juego'),
    path('consola/<str:nombre>/', views.detalle_consola, name='detalle_consola'),
    ]