from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=255)
    intro = models.TextField()
    conclusion = models.TextField()
    thumbnail = models.ImageField(upload_to='post-thumbnails', null=True, blank=True)
    header_image = models.ImageField(upload_to='post-headers', null=True, blank=True)
    slug = models.SlugField(unique=True, max_length=255)
    categories = models.ManyToManyField(Category, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

class Point(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    order = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='points')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title


class Paragraph(models.Model):
    text = models.TextField()
    order = models.PositiveIntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='paragraphs')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.text
