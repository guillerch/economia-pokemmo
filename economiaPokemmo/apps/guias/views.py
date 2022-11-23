from django.shortcuts import render
from .models import Guia
# Create your views here.
def guias(request):
    guides = Guia.objects.all()
    context = {
        'guides':guides,
    }
    return render(request,'guias.html',context)