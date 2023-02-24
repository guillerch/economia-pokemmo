from django.urls import path
from . import views
from .views import GuiaList, GuiaDetail

urlpatterns = [
    path('guias/', views.guias,name='guias'),
    path('guias-list/', GuiaList.as_view(), name='guia-list'),
    path('guias-list/<int:pk>/', GuiaDetail.as_view(), name='guia-detail'),
    ]