from django.shortcuts import render
from .models import Baya
# Create your views here.

def bayas(request):
    berry=Baya.objects.all()
    times=[16,20,42,44,67]
    context={
        'bayas':berry,
        'tiempos':times
        }
    return render(request,'bayas.html',context)