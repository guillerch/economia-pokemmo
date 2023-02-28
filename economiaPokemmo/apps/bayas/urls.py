from django.urls import path,include
from . import views
from rest_framework import routers
from .views import BayaViewSet

router = routers.DefaultRouter()
router.register(r'api/bayapokemmo123456', BayaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]