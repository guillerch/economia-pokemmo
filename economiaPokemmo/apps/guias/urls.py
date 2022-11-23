from django.urls import path
from . import views

urlpatterns = [
    path('guias/', views.guias,name='guias'),
    ]