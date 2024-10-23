"""Implementa a interface do django admin"""

from django.contrib import admin
from infrastructure.models.marketing.produto import ProdutoModel

@admin.register(ProdutoModel)
class ProdutoAdmin(admin.ModelAdmin):
    """
    Admin para o modelo ProdutoModel.
    Configurações de exibição, busca, filtros e formatação no Django Admin.
    """

    # Campos que serão exibidos na lista de objetos
    list_display = ('nome', 'descricao', 'tipo_produto', 'created_at', 'updated_at', 'is_active')

    # Campos que podem ser usados para busca
    search_fields = ('nome', 'descricao', 'tipo_produto__nome')

    # Filtros laterais
    list_filter = ('tipo_produto', 'is_active', 'created_at', 'updated_at')

    # Definindo os campos editáveis diretamente na lista de objetos
    list_editable = ('is_active',)

    # Definindo a ordenação padrão da lista
    ordering = ('-created_at',)

    # Campos que serão exibidos no formulário de criação/edição
    fieldsets = (
        ('Informações do Produto', {
            'fields': ('nome', 'descricao', 'tipo_produto', 'is_active')
        }),
        ('Informações de Auditoria', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Esconde a seção por padrão
        }),
    )

    # Campos que serão apenas de leitura no formulário
    readonly_fields = ('created_at', 'updated_at')

