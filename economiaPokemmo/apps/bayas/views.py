from .models import Baya
from rest_framework import viewsets
from .serializers import BayaSerializer
# Create your views here.

class BayaViewSet(viewsets.ModelViewSet):
    queryset = Baya.objects.all()
    serializer_class = BayaSerializer