from django.contrib import admin
from .models import Category, Post, Point, Paragraph


class PointInline(admin.StackedInline):
    model = Point
    extra = 0


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    extra = 0


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at', 'updated_at']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [PointInline, ParagraphInline]
    filter_horizontal = ['categories']


@admin.register(Point)
class PointAdmin(admin.ModelAdmin):
    list_display = ['title', 'post', 'order']
    list_filter = ['post']
    search_fields = ['title', 'post__title']
    ordering = ['order']


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ['text', 'post', 'order']
    list_filter = ['post']
    search_fields = ['text', 'post__title']
    ordering = ['order']