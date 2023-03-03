from .models import Baya
from rest_framework import viewsets
from .serializers import BayaSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BayaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Baya.objects.all()
    serializer_class = BayaSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]