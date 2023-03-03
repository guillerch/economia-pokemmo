from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'api/categories',views.CategoryList)
router.register(r'api/posts', views.PostViewSet)
router.register(r'api/points', views.PointViewSet)
router.register(r'api/paragraphs', views.ParagraphViewSet)


urlpatterns = [
    path('', include(router.urls)),
]