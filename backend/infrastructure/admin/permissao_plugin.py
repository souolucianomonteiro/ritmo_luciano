# backend/infrastructure/admin.py

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

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Filtra as permissões existentes, pode-se adicionar lógica específica se necessário
        form.base_fields['codename'].help_text = "Escolha um codename único para a permissão."
        return form
