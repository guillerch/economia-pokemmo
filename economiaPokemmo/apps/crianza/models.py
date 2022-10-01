from django.db import models

# Create your models here.
class Ataque(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True,null=True,unique=True)

    class Meta:
        verbose_name='Ataque'
        verbose_name_plural='Ataques'

    def __str__(self):
        return self.name


class GrupoHuevo(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True,null=True)

    class Meta:
        verbose_name='Grupo'
        verbose_name_plural='Grupos'

    def __str__(self):
        return self.name

class Genero(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True,null=True)

    class Meta:
        verbose_name='Genero'
        verbose_name_plural='Generos'

    def __str__(self):
        return self.name

class Pokemon(models.Model):
    name = models.CharField('Nombre', max_length=255, blank=True,null=True)
    grupo=models.ManyToManyField(GrupoHuevo, verbose_name='Grupo Huevo',blank=True)
    ataque=models.ManyToManyField(Ataque, verbose_name='Ataques',blank=True)
    especial=models.BooleanField(default=False)
    genero=models.ManyToManyField(Genero, verbose_name='Genero',blank=True)
    imagen=models.ImageField(default='null',verbose_name='Imagen',upload_to='pokemons')

    class Meta:
        verbose_name='Pokemon'
        verbose_name_plural='Pokemones'

    def __str__(self):
        return self.name