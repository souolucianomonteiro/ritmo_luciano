"""
Configurações de exibição e administração do modelo EnderecoModel no Django Admin.

Este admin organiza os campos do modelo EnderecoModel para facilitar a exibição,
pesquisa e edição de endereços no painel administrativo do Django. Inclui opções
de busca, filtros, listagem e agrupamento de campos por seções.

Listagem:
    list_display: Define os campos visíveis na listagem principal do admin.
    search_fields: Campos que podem ser usados para busca textual.
    list_filter: Filtros aplicados para facilitar a pesquisa por atributos.
    ordering: Define a ordenação padrão dos registros.

Formulário:
    fieldsets: Agrupa os campos em seções, organizando as informações de 
    endereço, tipo de endereço, associações e status.
    readonly_fields: Campos que são somente leitura.
"""
from django.contrib import admin
from infrastructure.models.marketing.endereco import EnderecoModel

@admin.register(EnderecoModel)
class EnderecoAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo EnderecoModel no Django Admin.
    Organiza os campos em seções para facilitar a visualização e busca.
    """
    
    # Campos que aparecem na listagem
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'pais', 'tipo', 'is_active')
    
    # Campos que permitem busca no admin
    search_fields = ('rua', 'bairro', 'cidade', 'estado', 'cep', 'pais')
    
    # Filtros para facilitar a pesquisa
    list_filter = ('cidade', 'estado', 'pais', 'tipo', 'is_active')
    
    # Organização dos campos em seções no formulário de edição
    fieldsets = (
        ('Informações do Endereço', {
            'fields': ('rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'pais')
        }),
        ('Tipo de Endereço', {
            'fields': ('tipo',)
        }),
        ('Associações', {
            'fields': ('pessoa_fisica', 'pessoa_juridica')
        }),
        ('Validade e Status', {
            'fields': ('is_active', 'data_inicio', 'data_fim')
        }),
    )
    
    # Campos de leitura somente
    readonly_fields = ('data_inicio', 'data_fim')
    
    # Ordenação padrão
    ordering = ('rua', 'numero')

