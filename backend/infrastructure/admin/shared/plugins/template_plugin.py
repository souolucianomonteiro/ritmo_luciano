"""
Módulo de configuração do Django Admin para o modelo TemplatePluginModel.

Este módulo contém a configuração da interface administrativa para o modelo
TemplatePluginModel, utilizado para gerenciar os templates associados aos plugins
no sistema.

Classes:
    TemplatePluginAdmin: Configurações de exibição e administração do modelo TemplatePluginModel no Django Admin.
"""


from django.contrib import admin
from infrastructure.models.shared.plugins.template_plugin import TemplatePluginModel

@admin.register(TemplatePluginModel)
class TemplatePluginAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo TemplatePluginModel no Django Admin.
    """

    list_display = ('plugin', 'nome_template', 'contexto_placeholder', 'caminho_arquivo')
    search_fields = ('nome_template', 'plugin__nome', 'contexto_placeholder')
    list_filter = ('plugin', 'contexto_placeholder')

    # Organizando os campos em seções
    fieldsets = (
        ('Informações do Template', {
            'fields': ('plugin', 'nome_template', 'contexto_placeholder', 'caminho_arquivo')
        }),
        ('Informações de Auditoria e Soft Delete', {
            'fields': ('created_by', 'updated_by', 'is_deleted', 'deleted_at', 'is_active', 'inactivated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Lógica adicional pode ser adicionada aqui, se necessário
        return form
