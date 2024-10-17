"""
Módulo de configuração do Django Admin para o modelo HistoricoModificacoesModel.

Este módulo contém a configuração da interface administrativa para o modelo
HistoricoModificacoesModel, utilizado para gerenciar o histórico de modificações
dos plugins no sistema.

Classes:
    HistoricoModificacoesAdmin: Configurações de exibição e administração do modelo HistoricoModificacoesModel no Django Admin.
"""
from django.contrib import admin
from infrastructure.models.shared.plugins.historico_modificacoes import (
                                HistoricoModificacoesModel)

@admin.register(HistoricoModificacoesModel)
class HistoricoModificacoesAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo HistoricoModificacoesModel no Django Admin.
    """

    list_display = ('plugin', 'data_modificacao', 'usuario', 'descricao_modificacao')
    search_fields = ('usuario', 'descricao_modificacao', 'plugin__nome')
    list_filter = ('plugin', 'data_modificacao')

    # Organizando os campos em seções
    fieldsets = (
        ('Detalhes da Modificação', {
            'fields': ('plugin', 'data_modificacao', 'usuario', 'descricao_modificacao')
        }),
        ('Informações de Auditoria e Soft Delete', {
            'fields': ('created_by', 'updated_by', 'is_deleted', 'deleted_at', 'is_active', 'inactivated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        # Lógica adicional pode ser adicionada aqui, se necessário
        return form

