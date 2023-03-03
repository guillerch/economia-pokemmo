from rest_framework import viewsets, permissions
from .models import Category, Post, Point, Paragraph
from .serializers import CategorySerializer, PostSerializer, PointSerializer, ParagraphSerializer


class CategoryList(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PointViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ParagraphViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Paragraph.objects.all()
    serializer_class = ParagraphSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]