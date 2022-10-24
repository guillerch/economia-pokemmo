from django.db import models

# Create your models here.

class Baya(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True,null=True,unique=True)
    time = models.IntegerField('Tiempo')
    description = models.TextField('Descripción', max_length=255, blank=True)
    seed1 = models.CharField('Semilla 1', max_length=255)
    seed2 = models.CharField('Semilla 2', max_length=255)
    seed3 = models.CharField('Semilla 3', max_length=255,default="")

    class Meta:
        verbose_name='Baya'
        verbose_name_plural='Bayas'

    def __str__(self):
        return self.name