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
        ('Redes Sociais', {
            'fields': ('redes_sociais',),
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
