"""
Configuração do Django Admin para o modelo ArtefatoPluginModel.

Este módulo define a interface administrativa para o modelo
ArtefatoPluginModel, incluindo como os campos são exibidos, filtrados
e pesquisados no Django Admin. Ele permite que os administradores do
site gerenciem os artefatos dos plugins através de uma interface
gráfica amigável.
"""

from django.contrib import admin
from infrastructure.models.artefato_plugin import ArtefatoPluginModel

@admin.register(ArtefatoPluginModel)
class ArtefatoPluginAdmin(admin.ModelAdmin):

    """
    Configuração do Django Admin para a model ArtefatoPluginModel.
    Define como a model será exibida e manipulada no Django Admin.
    """

    list_display = ('nome', 'versao', 'tipo_arquivo', 'ativo', 'created_at', 'updated_at')
    list_filter = ('ativo', 'tipo_arquivo', 'created_at', 'updated_at')
    search_fields = ('nome', 'versao', 'tipo_arquivo')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao', 'versao', 'tipo_arquivo', 'caminho_arquivo', 'ativo')
        }),
        ('Informações de Auditoria', {
            'fields': ('created_at', 'updated_at', 'created_by', 'updated_by'),
            'classes': ('collapse',),
        }),
    )
