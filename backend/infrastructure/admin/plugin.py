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
    Configurações de exibição e administração do modelo PluginModel no Django Admin.
    """

    list_display = ('nome', 'categoria', 'tipo_plugin', 'versao')
    search_fields = ('nome', 'categoria__nome', 'tipo_plugin__nome', 'versao')
    list_filter = ('categoria', 'tipo_plugin')

    filter_horizontal = ('permissoes', 'historico_modificacoes', 'tags', 'dependencias', 'templates')

    # Organizando campos em seções com títulos
    fieldsets = (
        ('Informações do Plugin', {
            'fields': ('nome', 'categoria', 'tipo_plugin', 'versao', 'descricao', 'documentacao', 'caminho_arquivo')
        }),
        ('Associações', {
            'fields': ('tags', 'permissoes', 'historico_modificacoes', 'dependencias', 'templates')
        }),
        ('Informações de Auditoria e Soft Delete', {
            'fields': ('created_by', 'updated_by', 'is_deleted', 'deleted_at', 'is_active', 'inactivated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Lógica adicional pode ser adicionada aqui, se necessário
        return form
