from django.shortcuts import render, get_object_or_404 , redirect   

from .models import Videojuego,Consola,Jugete

from .forms import VideojuegoForm

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

def detalle_juego(request, nombre):
    videojuego = get_object_or_404(Videojuego, nombre=nombre)  
    context = {"videojuego": videojuego}  
    return render(request, 'megagames/detalle_juego.html', context)

def consolas(request):
    query = request.GET.get('q', '')
    if query:
        consolas = Consola.objects.filter(nombre__icontains=query)
    else:
        consolas = Consola.objects.all()
    
    context = {"consolas": consolas}  
    return render(request, 'megagames/consolas.html', context)


def detalle_consola(request, nombre):
    consola = get_object_or_404(Consola, nombre=nombre)
    context = {"consola": consola}
    return render(request, 'megagames/detalle_consola.html', context)

def jugetes (request):
    query = request.GET.get('q', '')
    if query:
        jugetes = Jugete.objects.filter(nombre__icontains=query)
    else:    
        jugetes = Jugete.objects.all()

    context ={"jugetes":jugetes}
    return render (request, 'megagames/jugetes.html',context)

def detalle_jugete(request, nombre):
    jugete = get_object_or_404(Jugete, nombre=nombre)
    context = {"jugete": jugete}
    return render(request, 'megagames/detalle_jugete.html', context)

def contacto (request):
    context ={}
    return render (request, 'megagames/contacto.html',context)

def perfil (request):
    context ={}
    return render (request, 'megagames/perfil.html',context)

def carrito (request):
    context ={}
    return render (request, 'megagames/carrito.html',context)


def juegoraw(request):
    videojuegos = Videojuego.objects.raw('SELECT * FROM megagames_videojuego')
    context = {"videojuegos": videojuegos}
    return render(request, 'megagames/juegoraw.html', context)


######## CRUD VIDEOJUEGO 



### Listar juegos 
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'megagames/lista_videojuegos.html', {'videojuegos': videojuegos})

def videojuego_crear(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'megagames/videojuego_crear.html', {'form': form})

def editar_videojuego(request, nombre):
    videojuego = get_object_or_404(Videojuego, nombre=nombre)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'megagames/editar_videojuego.html', {'form': form, 'titulo': f'Editar {videojuego.nombre}'})

def eliminar_videojuego(request, nombre):
    videojuego = get_object_or_404(Videojuego, nombre=nombre)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'megagames/eliminar_videojuego.html', {'videojuego': videojuego})

