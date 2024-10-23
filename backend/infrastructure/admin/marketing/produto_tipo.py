"""Implementa o registro e exibição da model produto_tipo"""

from django.contrib import admin
from infrastructure.models.marketing.produto_tipo import TipoProdutoModel

@admin.register(TipoProdutoModel)
class TipoProdutoAdmin(admin.ModelAdmin):
    """
    Admin para o modelo TipoProdutoModel.
    Configurações de exibição, busca, filtros e formatação no Django Admin.
    """

    # Configurando os campos que serão exibidos na lista de objetos
    list_display = ('nome', 'descricao', 'get_situacao_display', 'created_at', 'updated_at', 'is_active')

    # Configurando os campos que podem ser usados para busca
    search_fields = ('nome', 'descricao')

    # Configurando os filtros laterais
    list_filter = ('is_active', 'situacao', 'created_at', 'updated_at')

    # Definindo os campos editáveis diretamente na lista de objetos
    list_editable = ('is_active', 'situacao')

    # Definindo a ordenação padrão da lista
    ordering = ('-created_at',)

    # Campos que serão exibidos no formulário de criação/edição
    fieldsets = (
        ('Informações Gerais', {
            'fields': ('nome', 'descricao', 'situacao', 'is_active')
        }),
        ('Informações de Auditoria', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),  # Esconde a seção por padrão
        }),
    )

    # Campos que serão apenas de leitura no formulário
    readonly_fields = ('created_at', 'updated_at')

    # Exibe o valor amigável da situação no list_display
    def get_situacao_display(self, obj):
        return obj.get_situacao_display()
    get_situacao_display.short_description = 'Situação'
