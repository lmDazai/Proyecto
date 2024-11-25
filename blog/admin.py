from django.contrib import admin
from .models import Articulo

# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
    list_display=["titulo","contenido","autor"]

admin.site.register(Articulo,ArticuloAdmin)


