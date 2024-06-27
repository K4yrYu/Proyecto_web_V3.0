from django.shortcuts import render

# Create your views here.
def index (request):
    context ={}
    return render (request, 'megagames/index.html',context)


def juego (request):
    context ={}
    return render (request, 'megagames/juego.html',context)

def consolas (request):
    context ={}
    return render (request, 'megagames/consolas.html',context)

def jugetes (request):
    context ={}
    return render (request, 'megagames/jugetes.html',context)