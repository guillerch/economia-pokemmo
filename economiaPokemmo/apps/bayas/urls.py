from django.urls import path,include
from . import views
from rest_framework import routers
from .views import BayaViewSet

router = routers.DefaultRouter()
router.register(r'baya', BayaViewSet)

urlpatterns = [
    path('bayas/',views.bayas,name='bayas'),
    path('', include(router.urls)),
    ]