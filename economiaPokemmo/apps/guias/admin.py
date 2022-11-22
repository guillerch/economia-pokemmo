from django.contrib import admin
from .models import Guia

class GuiaAdmin(admin.ModelAdmin):
    '''Admin View for Guia'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)
    
# Register your models here.
admin.site.register(Guia,GuiaAdmin)