# backend/infrastructure/models/admin.py
"""
Módulo de configuração do Django Admin para o modelo TagPluginModel.

Este módulo contém a configuração da interface administrativa para o modelo
TagPluginModel, utilizado para gerenciar as tags associadas aos plugins no sistema.

Classes:
    TagPluginAdmin: Configurações de exibição e administração do modelo TagPluginModel no Django Admin.
"""
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

    # Organizando os campos em seções
    fieldsets = (
        ('Informações da Tag', {
            'fields': ('nome',)
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted')
        }),
        ('Informações de Auditoria', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by')
        }),
    )
