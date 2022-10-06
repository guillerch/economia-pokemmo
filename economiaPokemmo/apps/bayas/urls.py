from django.urls import path
from . import views

urlpatterns = [
    path('bayas/',views.bayas,name='bayas')
    ]