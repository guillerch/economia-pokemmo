from rest_framework import serializers
from .models import Category,Post, Point, Paragraph



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name','slug')

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ('id', 'post', 'text', 'order')

class PointSerializer(serializers.ModelSerializer):
    paragraphs = ParagraphSerializer(many=True, read_only=True)

    class Meta:
        model = Point
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    points = PointSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'intro', 'thumbnail', 'header_image', 'conclusion', 'points', 'categories')
