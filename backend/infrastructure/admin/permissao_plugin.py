# backend/infrastructure/admin.py
"""
Módulo de configuração do Django Admin para o modelo PermissaoPluginModel.

Este módulo contém a configuração da interface administrativa para o modelo
PermissaoPluginModel, utilizado para gerenciar as permissões associadas aos
plugins no sistema.

Classes:
    PermissaoPluginAdmin: Configurações de exibição e administração do modelo PermissaoPluginModel no Django Admin.
"""
from django.contrib import admin
from infrastructure.models.permissao_plugin import PermissaoPluginModel

@admin.register(PermissaoPluginModel)
class PermissaoPluginAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PermissaoPluginModel
    no Django Admin.
    """

    list_display = ('plugin', 'codename', 'name')
    search_fields = ('codename', 'name', 'plugin__name')
    list_filter = ('plugin',)

    # Organizando os campos em seções
    fieldsets = (
        ('Informações da Permissão', {
            'fields': ('plugin', 'codename', 'name')
        }),
        ('Informações de Auditoria e Soft Delete', {
            'fields': ('created_by', 'updated_by', 'is_deleted', 'deleted_at', 'is_active', 'inactivated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Filtra as permissões existentes, pode-se adicionar lógica específica se necessário
        form.base_fields['codename'].help_text = "Escolha um codename único para a permissão."
        return form
