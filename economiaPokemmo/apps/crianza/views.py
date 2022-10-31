from django.shortcuts import render
from .models import Pokemon

# Create your views here.

def index(request):
    return render(request, 'index.html')

def politicas(request):
    return render(request, 'politicas.html')
def terminos(request):
    return render(request, 'terminos.html')

def crianza(request):

    pokes=Pokemon.objects.all()
    context={
        'pokes': pokes,
        'ivs': range(2,7),
    }
    return render (request,'crianza.html',context)