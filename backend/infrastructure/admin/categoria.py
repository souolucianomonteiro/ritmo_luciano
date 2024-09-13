# infrastructure/admin/categoria_admin.py

from django.contrib import admin
from infrastructure.models.categoria import CategoriaModel

@admin.register(CategoriaModel)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)
