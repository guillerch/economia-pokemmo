from django.db import models

# Create your models here.
class Guia(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True,null=True,unique=True)
    description = models.TextField('Descripción', max_length=100, blank=True,null=True,)
    img = models.ImageField(default='null',verbose_name='Portada',upload_to='guias')
    video = models.CharField('Video', max_length=255, blank=True,null=True,unique=True)

    class Meta:
        verbose_name='Guia'
        verbose_name_plural='Guias'

    def __str__(self):
        return self.name