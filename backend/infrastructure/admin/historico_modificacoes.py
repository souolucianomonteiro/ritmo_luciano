from django.contrib import admin
from infrastructure.models.historico_modificacoes import (
                                HistoricoModificacoesModel)

@admin.register(HistoricoModificacoesModel)
class HistoricoModificacoesAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo HistoricoModificacoesModel no Django Admin.
    """

    list_display = ('plugin', 'data_modificacao', 'usuario', 'descricao_modificacao')
    search_fields = ('usuario', 'descricao_modificacao', 'plugin__nome')
    list_filter = ('plugin', 'data_modificacao')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Lógica adicional pode ser adicionada aqui, se necessário
        return form
