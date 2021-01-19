from django.contrib import admin
from .models import Curso
from .models import Orla

# Register your models here.

admin.site.register(Curso)
admin.site.register(Orla)

class CursoAdmin (admin.ModelAdmin):
    list_display=('num','titulo','subtitulo','Fecha','logo')
    search_fields=('num','titulo','Fecha')
    list_filter=('Fecha')
    date_hierarchy='Fecha'

class OrlaAdmin(admin.ModelAdmin):
    list_display=('owner','nombre','apellidos','texto','image','video','created','estado')
    search_fields=('owner','nombre','apellidos')
    list_filter=('estado')
    