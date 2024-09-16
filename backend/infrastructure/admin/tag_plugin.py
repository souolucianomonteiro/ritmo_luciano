# backend/infrastructure/models/admin.py

from django.contrib import admin
from infrastructure.models.tag_plugin import TagPluginModel

@admin.register(TagPluginModel)
class TagPluginAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo TagPluginModel no Django Admin.

    Atributos:
        list_display (tuple): Campos a serem exibidos na lista de tags.
        search_fields (tuple): Campos pelos quais a pesquisa pode ser feita.
        list_filter (tuple): Filtros disponíveis na barra lateral do Django Admin.
    """

    list_display = ('id', 'nome', 'created_at', 'updated_at', 'is_active', 'is_deleted')
    search_fields = ('nome',)
    list_filter = ('is_active', 'is_deleted', 'created_at', 'updated_at')
