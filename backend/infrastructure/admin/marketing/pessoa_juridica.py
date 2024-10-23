"""
Módulo responsável pela configuração da exibição da model PessoaJuridica
no Django Admin.

Este módulo define a classe PessoaJuridicaAdmin, que personaliza a forma
como os dados da pessoa jurídica são exibidos e gerenciados no painel 
administrativo do Django. Inclui configurações para listagem, filtros,
campos de busca e gerenciamento de relacionamentos como administradores,
endereços, atividades econômicas, redes sociais e situação.

Classes:
    PessoaJuridicaAdmin: Classe que configura o Django Admin para a
    model PessoaJuridica.
"""

from django.contrib import admin
from infrastructure.models.marketing.pessoa_juridica import PessoaJuridicaModel

@admin.register(PessoaJuridicaModel)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição da model PessoaJuridica no Django Admin.
    Gerencia campos como razão social, CNPJ, administradores, atividades
    econômicas, endereços, redes sociais e a situação da empresa.
    """

    # Campos exibidos na listagem de pessoas jurídicas no painel de admin
    list_display = (
        'razao_social', 'cnpj', 'website', 'iniciador', 'get_administradores',
        'situacao'
    )

    # Campos utilizados para busca no admin
    search_fields = ('razao_social', 'cnpj', 'nome_fantasia')

    # Filtros laterais disponíveis para navegação
    list_filter = ('atividades_economicas', 'administradores', 'situacao')

    # Campos relacionados gerenciados via caixas de seleção
    filter_horizontal = ('enderecos', 'administradores', 'atividades_economicas', 'redes_sociais')

    # Organização dos campos exibidos ao editar/criar
    fieldsets = (
        (None, {
            'fields': ('razao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'website')
        }),
        ('Relacionamentos', {
            'fields': ('iniciador', 'administradores', 'enderecos', 'atividades_economicas', 'redes_sociais')
        }),
        ('Situação', {
            'fields': ('situacao', 'deleted', 'active'),
        }),
    )

    def get_administradores(self, obj):
        """
        Exibe os administradores no list_display.

        Args:
            obj (PessoaJuridicaModel): Instância da pessoa jurídica.

        Returns:
            str: Lista de administradores formatada como string.
        """
        return ", ".join([admin.first_name for admin in obj.administradores.all()])
    get_administradores.short_description = 'Administradores'
