from django.shortcuts import render

from .models import Videojuego,Consola,Jugete

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
    query = request.GET.get('q', '')
    if query:
        consolas = Consola.objects.filter(nombre__icontains=query)
    else:
        consolas = Consola.objects.all()
    
    context = {"consolas": consolas}  
    return render(request, 'megagames/consolas.html', context)

def jugetes (request):
    query = request.GET.get('q', '')
    if query:
        jugetes = Jugete.objects.filter(nombre__icontains=query)
    else:    
        jugetes = Jugete.objects.all()

    context ={"jugetes":jugetes}
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