"""
Módulo responsável pela configuração do Django Admin para a model PessoaFisica.

Este módulo define a classe PessoaFisicaAdmin, que gerencia a exibição,
edição e busca de registros da model PessoaFisicaModel no painel administrativo
do Django. Ele inclui funcionalidades adicionais como o cálculo da idade
em anos e meses com base na data de nascimento, além de customizar a
organização e a apresentação dos campos.

Classes:
    PessoaFisicaAdmin: Classe que define as configurações do Django Admin
    para o modelo PessoaFisicaModel.
    
Funções:
    idade_em_anos(obj): Calcula a idade em anos com base na data de nascimento.
    idade_em_meses(obj): Calcula a idade em meses com base na data de
    nascimento.
"""

from typing import Optional
from django.contrib import admin
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.marketing.pessoa_fisica_rede_social import (
                                            PessoaFisicaRedeSocialModel)
from domain.shared.utils.calcular_idade import calcular_idade


# Inline para gerenciamento de redes sociais associadas
# Inline para gerenciamento de redes sociais associadas
class PessoaFisicaRedeSocialInline(admin.TabularInline):
    """ Gerenciamento de rede social da pessoa física"""
    model = PessoaFisicaRedeSocialModel
    extra = 1
    autocomplete_fields = ['rede_social']


@admin.register(PessoaFisicaModel)
class PessoaFisicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PessoaFisicaModel
    no Django Admin.
    """
    
    list_display = ('first_name', 'last_name', 'cpf', 'email', 
                    'data_nascimento', 'idade_completa', 
                    'genero', 'situacao', 'conta_pessoa',
                    'iniciador_conta_empresa')

    search_fields = ('first_name', 'last_name', 'cpf', 'email', 'whatsapp')

    list_filter = ('genero', 'situacao', 'conta_pessoa', 'iniciador_conta_empresa', 'data_nascimento')

    readonly_fields = ('cpf', 'email', 'data_nascimento', 'ultimo_login')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('first_name', 'last_name', 'cpf', 'genero', 'data_nascimento', 'email', 'whatsapp', 'foto', 'bios')
        }),
        ('Endereços', {'fields': ('enderecos',)}),
        ('Situação e Conta', {'fields': ('situacao', 'conta_pessoa', 'iniciador_conta_empresa', 'ultimo_login')}),
        ('Profissão e Ocupação', {'fields': ('profissao', 'ocupacao')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )

    ordering = ('first_name', 'last_name', 'cpf')

    date_hierarchy = 'data_nascimento'

    inlines = [PessoaFisicaRedeSocialInline]

    def idade_completa(self, obj: PessoaFisicaModel) -> Optional[str]:
        """
        Exibe a idade completa (anos e meses) no formato "X anos e Y meses".
        """
        idade = calcular_idade(obj.data_nascimento)
        if idade["anos"] is not None and idade["meses"] is not None:
            return f"{idade['anos']} anos e {idade['meses']} meses"
        return None

    idade_completa.short_description = 'Idade Completa'

