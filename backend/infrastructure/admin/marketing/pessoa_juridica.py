"""
Módulo responsável pela configuração da exibição da model PessoaJuridica
no Django Admin.

Este módulo define a classe PessoaJuridicaAdmin, que personaliza a forma
como os dados da pessoa jurídica são exibidos e gerenciados no painel 
administrativo do Django. Inclui configurações para listagem, filtros,
campos de busca e gerenciamento de relacionamentos como administradores,
endereços, atividades econômicas e redes sociais.

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
    """

    list_display = (
        'razao_social', 'cnpj', 'website', 'iniciador', 'get_administradores'
    )
    search_fields = ('razao_social', 'cnpj', 'nome_fantasia')
    list_filter = ('atividades_economicas', 'administradores')
    filter_horizontal = ('enderecos', 'administradores', 'atividades_economicas', 'redes_sociais')

    fieldsets = (
        (None, {
            'fields': ('razao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'website')
        }),
        ('Relacionamentos', {
            'fields': ('iniciador', 'administradores', 'enderecos', 'atividades_economicas', 'redes_sociais')
        }),
        ('Situação', {
            'fields': ('deleted', 'active'),
        }),
    )

    def get_administradores(self, obj):
        """
        Exibe os administradores no list_display.
        """
        return ", ".join([admin.first_name for admin in obj.administradores.all()])
    get_administradores.short_description = 'Administradores'
