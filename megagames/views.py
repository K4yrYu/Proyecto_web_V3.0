from django.shortcuts import render

from .models import Videojuego,Consola

# Create your views here.
def index (request):
    context ={}
    return render (request, 'megagames/index.html',context)


def juego(request):
    query = request.GET.get('q', '')
    if query:
        videojuegos = Videojuego.objects.filter(nombre__icontains=query)
    else:
        videojuegos = Videojuego.objects.all()
    
    context = {"videojuegos": videojuegos}
    return render(request, 'megagames/juego.html', context)

def consolas(request):
    consolas = Consola.objects.all()  # Fetch all instances of Consola
    context = {"consolas": consolas}  # Pass instances to the context dictionary
    return render(request, 'megagames/consolas.html', context)

def jugetes (request):
    context ={}
    return render (request, 'megagames/jugetes.html',context)

def contacto (request):
    context ={}
    return render (request, 'megagames/contacto.html',context)

def perfil (request):
    context ={}
    return render (request, 'megagames/perfil.html',context)

def carrito (request):
    context ={}
    return render (request, 'megagames/carrito.html',context)