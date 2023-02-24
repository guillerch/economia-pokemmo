from django.shortcuts import render
from .models import Baya
from rest_framework import viewsets
from .serializers import BayaSerializer
# Create your views here.

def bayas(request):
    berry=Baya.objects.all()
    times=[16,20,42,44,67]
    context={
        'bayas':berry,
        'tiempos':times
        }
    return render(request,'bayas.html',context)

class BayaViewSet(viewsets.ModelViewSet):
    queryset = Baya.objects.all()
    serializer_class = BayaSerializer