"""
Configurações de exibição e administração do modelo AtividadeEconomicaModel
no Django Admin.

Este admin organiza os campos do modelo AtividadeEconomicaModel para facilitar a
visualização, pesquisa e edição das atividades econômicas no painel
administrativo 
do Django. Inclui opções de busca, filtros, listagem e organização dos campos.

Listagem:
    list_display: Define os campos visíveis na listagem principal do admin.
    search_fields: Campos que podem ser usados para busca textual.
    list_filter: Filtros aplicados para facilitar a pesquisa por atributos.
    ordering: Define a ordenação padrão dos registros.

Formulário:
    fieldsets: Agrupa os campos de código e descrição da atividade econômica,
    facilitando a navegação no formulário de edição.
"""
from django.contrib import admin
from infrastructure.models.marketing.atividade_economica import (
                                        AtividadeEconomicaModel)

@admin.register(AtividadeEconomicaModel)
class AtividadeEconomicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo
    AtividadeEconomicaModel no Django Admin.
    Organiza os campos em seções para facilitar a visualização e busca.
    """
    
    # Campos que aparecem na listagem
    list_display = ('atividade_econ_codigo', 'atividade_econ_descricao')
    
    # Campos que permitem busca no admin
    search_fields = ('atividade_econ_codigo', 'atividade_econ_descricao')
    
    # Filtros para facilitar a pesquisa
    list_filter = ('atividade_econ_codigo',)
    
    # Organização dos campos em seções no formulário de edição
    fieldsets = (
        ('Informações da Atividade Econômica', {
            'fields': ('atividade_econ_codigo', 'atividade_econ_descricao')
        }),
    )
    
    # Ordenação padrão
    ordering = ('atividade_econ_codigo',)
