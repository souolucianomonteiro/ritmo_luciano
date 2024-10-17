"""
Módulo de configuração do Django Admin para o modelo DependenciaModel.

Este módulo contém a configuração da interface administrativa para o modelo
DependenciaModel, utilizado para gerenciar as dependências dos plugins no
sistema.

Classes:
    DependenciaPluginAdmin: Configurações de exibição e administração do
    modelo DependenciaModel no Django Admin.
"""
from django.contrib import admin
from infrastructure.models.shared.plugins.dependencia_plugin import DependenciaModel

@admin.register(DependenciaModel)
class DependenciaPluginAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo DependenciaModel no Django Admin.
    """

    list_display = ('plugin', 'tipo_dependencia', 'dependencia_plugin', 'nome_dependencia', 'url_dependencia')
    search_fields = ('plugin__nome', 'dependencia_plugin__nome', 'nome_dependencia')
    list_filter = ('tipo_dependencia', 'plugin')

    # Organizando os campos em seções
    fieldsets = (
        ('Informações da Dependência', {
            'fields': ('plugin', 'tipo_dependencia', 'dependencia_plugin', 'nome_dependencia', 'url_dependencia')
        }),
        ('Informações de Auditoria e Soft Delete', {
            'fields': ('created_by', 'updated_by', 'is_deleted', 'deleted_at', 'is_active', 'inactivated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Lógica adicional pode ser adicionada aqui, se necessário
        return form

