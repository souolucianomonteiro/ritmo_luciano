"""
Configurações do Django Admin para o modelo Plugin.

Este módulo contém a configuração necessária para exibir e gerenciar o modelo 
Plugin no painel de administração do Django. Ele define como o modelo será 
exibido, quais campos serão visíveis, filtros e funcionalidades adicionais 
que facilitam a administração dos plugins.

Classes:
    PluginAdmin: Configuração do Django Admin para a model PluginModel.

"""
from django.contrib import admin
from infrastructure.models.plugin import PluginModel

@admin.register(PluginModel)
class PluginAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para a model PluginModel.
    Define como a model será exibida e manipulada no Django Admin.
    """

    list_display = (
        'nome', 
        'categoria', 
        'tipo_plugin', 
        'versao', 
        'status', 
        'uuid',  # Exibindo o UUID na lista
        'created_at', 
        'updated_at'
    )
    list_filter = (
        'categoria', 
        'tipo_plugin', 
        'status', 
        'created_at', 
        'updated_at'
    )
    search_fields = (
        'nome', 
        'versao', 
        'uuid'  # Permitindo busca pelo UUID
    )
    readonly_fields = (
        'uuid',  # O UUID é somente leitura
        'created_at', 
        'updated_at', 
        'created_by', 
        'updated_by'
    )

    fieldsets = (
        (None, {
            'fields': (
                'nome', 
                'categoria', 
                'tipo_plugin', 
                'versao', 
                'status', 
                'uuid',  # Incluindo UUID no conjunto de campos
                'descricao', 
                'caminho_arquivo', 
                'documentacao', 
                'permissoes', 
                'historico_modificacoes', 
                'tags', 
                'dependencias'
            )
        }),
        ('Informações de Auditoria', {
            'fields': (
                'created_at', 
                'updated_at', 
                'created_by', 
                'updated_by'
            ),
            'classes': ('collapse',),
        }),
    )
