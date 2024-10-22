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

from datetime import date
from typing import Optional
from django.contrib import admin
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.marketing.pessoa_fisica_rede_social import (
                                            PessoaFisicaRedeSocialModel)
from infrastructure.models.shared.resources.rede_social import (
                                                    RedeSocialModel)


# Inline para gerenciamento de redes sociais associadas
class PessoaFisicaRedeSocialInline(admin.TabularInline):
    """
    Define o inline da tabela associativa PessoaFisicaRedeSocialModel no admin.
    Permite gerenciar as redes sociais diretamente a partir do cadastro de 
    PessoaFisicaModel.
    """
    model = PessoaFisicaRedeSocialModel
    extra = 1  # Quantidade de campos vazios para adicionar novas redes sociais
    autocomplete_fields = ['rede_social']  # Facilita a seleção de redes sociais já cadastradas


@admin.register(PessoaFisicaModel)
class PessoaFisicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PessoaFisicaModel
    no Django Admin.
    Organiza os campos e melhora a experiência de administração.
    """
    
    # Exibir no painel principal do admin
    list_display = ('first_name', 'last_name', 'cpf', 'email', 
                    'data_nascimento', 'idade_em_anos', 'idade_em_meses',
                    'genero', 'situacao', 'conta_pessoa',
                    'iniciador_conta_empresa')
   
    # Campos de busca no painel de admin
    search_fields = ('first_name', 'last_name', 'cpf', 'email', 'whatsapp')

    # Filtros para facilitar a navegação
    list_filter = ('genero', 'situacao', 'conta_pessoa', 
                   'iniciador_conta_empresa', 'data_nascimento')
  
    # Campos de leitura apenas
    readonly_fields = ('cpf', 'email', 'data_nascimento', 'ultimo_login')

    # Organização dos campos no formulário de exibição/edição
    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('first_name', 'last_name', 'cpf', 'genero', 
                       'data_nascimento', 'email', 'whatsapp', 
                       'foto', 'bios')
        }),
        ('Endereços', {
            'fields': ('enderecos',),
        }),
        ('Situação e Conta', {
            'fields': ('situacao', 'conta_pessoa', 'iniciador_conta_empresa', 
                       'ultimo_login'),
        }),
        ('Profissão e Ocupação', {
            'fields': ('profissao', 'ocupacao'),
        }),
        ('Permissões', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups',
                       'user_permissions'),
        }),
    )

    # Define a ordenação dos registros na listagem do admin
    ordering = ('first_name', 'last_name', 'cpf')

    # Adicionando um filtro lateral baseado em data de nascimento
    date_hierarchy = 'data_nascimento'

    # Adiciona as redes sociais como inline para edição no admin
    inlines = [PessoaFisicaRedeSocialInline]  # Adiciona inline para redes sociais associadas

    # Calcular e exibir idade em anos
    def idade_em_anos(self, obj: PessoaFisicaModel) -> Optional[int]:
        """Calcula a idade em anos com base na data de nascimento."""
        if obj.data_nascimento:
            hoje = date.today()
            idade_anos = hoje.year - obj.data_nascimento.year - (
                (hoje.month, hoje.day) < (obj.data_nascimento.month,
                                          obj.data_nascimento.day)
            )
            return idade_anos
        return None

    def idade_em_meses(self, obj: PessoaFisicaModel) -> Optional[int]:
        """Calcula a idade em meses com base na data de nascimento."""
        if obj.data_nascimento:
            hoje = date.today()
            idade_meses = (hoje.year - obj.data_nascimento.year) * 12 + hoje.month - obj.data_nascimento.month
            return idade_meses
        return None

    idade_em_anos.short_description = 'Idade (Anos)'
    idade_em_meses.short_description = 'Idade (Meses)'


@admin.register(RedeSocialModel)
class RedeSocialAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para o gerenciamento das redes sociais.
    """
    list_display = ('nome', 'icone')  # Exibe o nome e ícone da rede social
    search_fields = ('nome',)  # Permite buscar redes sociais pelo nome
