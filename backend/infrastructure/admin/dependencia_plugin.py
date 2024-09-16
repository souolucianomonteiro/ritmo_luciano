from django.contrib import admin
from infrastructure.models.dependencia_plugin import DependenciaModel

@admin.register(DependenciaModel)
class DependenciaPluginAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo DependenciaModel no Django Admin.
    """

    list_display = ('plugin', 'tipo_dependencia', 'dependencia_plugin', 'nome_dependencia', 'url_dependencia')
    search_fields = ('plugin__nome', 'dependencia_plugin__nome', 'nome_dependencia')
    list_filter = ('tipo_dependencia', 'plugin')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Lógica adicional pode ser adicionada aqui, se necessário
        return form
