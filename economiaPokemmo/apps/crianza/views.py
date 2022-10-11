from django.shortcuts import render
from .models import Pokemon

# Create your views here.

def index(request):
    return render(request, 'index.html')

def crianza(request):

    pokes=Pokemon.objects.all()
    context={
        'pokes': pokes,
        'ivs': range(2,7),
    }
    return render (request,'crianza.html',context)