from django.shortcuts import render
from .models import Guia
from rest_framework import generics
from .serializers import GuiaSerializer
# Create your views here.
def guias(request):
    guides = Guia.objects.all()
    context = {
        'guides':guides,
    }
    return render(request,'guias.html',context)

class GuiaList(generics.ListCreateAPIView):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer

class GuiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guia.objects.all()
    serializer_class = GuiaSerializer