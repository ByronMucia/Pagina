from django.contrib import admin
from .models import CategoriaAsig, Asignatura

# Register your models here.

class CategoriaAsigAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

class AsigAdmin(admin.ModelAdmin):

    readonly_fields=("created","updated")

admin.site.register(CategoriaAsig, CategoriaAsigAdmin)

admin.site.register(Asignatura, AsigAdmin)
