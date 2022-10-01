from django.contrib import admin
from .models import GrupoHuevo,Ataque,Genero,Pokemon


class GrupoHuevoAdmin(admin.ModelAdmin):
    '''Admin View for GrupoHuevo'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class AtaqueAdmin(admin.ModelAdmin):
    '''Admin View for Ataque'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class GeneroAdmin(admin.ModelAdmin):
    '''Admin View for Genero'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class PokemonAdmin(admin.ModelAdmin):
    '''Admin View for Pokemon'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    
# Register your models here.
admin.site.register(GrupoHuevo,GrupoHuevoAdmin)
admin.site.register(Ataque,AtaqueAdmin)
admin.site.register(Genero,GeneroAdmin)
admin.site.register(Pokemon,PokemonAdmin)