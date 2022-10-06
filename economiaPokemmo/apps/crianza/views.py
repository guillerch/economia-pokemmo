from django.shortcuts import render
from .models import Pokemon

# Create your views here.

def index(request):
    return render(request, 'index.html')

def crianza(request):
    return render (request,'crianza.html')