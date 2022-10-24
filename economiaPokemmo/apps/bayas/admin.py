from django.contrib import admin
from .models import Baya


class BayaAdmin(admin.ModelAdmin):
    '''Admin View for Baya'''

    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)

# Register your models here.
admin.site.register(Baya,BayaAdmin)