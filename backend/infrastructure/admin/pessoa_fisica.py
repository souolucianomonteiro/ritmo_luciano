from django.contrib import admin
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from domain.website.domain_service.calcular_idade_titular import (
                                CalcularIdadePessoaFisicaService)

@admin.register(PessoaFisicaModel)
class PessoaFisicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PessoaFisicaModel no Django Admin.
    Organiza os campos da pessoa física em seções no formulário.
    """

    list_display = (
        'primeiro_nome', 'sobrenome', 'email', 'cpf', 'genero', 
        'idade_em_anos', 'idade_em_meses', 'conta_pessoa', 
        'iniciador_conta_empresa', 'foto', 'bios', 'situacao'
    )
    search_fields = ('primeiro_nome', 'sobrenome', 'email', 'cpf')
    list_filter = ('genero', 'conta_pessoa', 'iniciador_conta_empresa', 'situacao')
    ordering = ('primeiro_nome','sobrenome')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('primeiro_nome', 'sobrenome', 'email', 'cpf', 'data_nascimento', 'genero', 'foto', 'bios', 'situacao'),
            'description': 'Preencha as informações pessoais da pessoa física.',
        }),
        ('Contato', {
            'fields': ('whatsapp', 'redes_sociais'),
            'description': 'Informações de contato, como WhatsApp e redes sociais.',
        }),
        ('Profissão', {
            'fields': ('profissao', 'ocupacao'),
            'description': 'Profissão e ocupação atual da pessoa física.',
        }),
        ('Conta', {
            'fields': ('conta_pessoa', 'iniciador_conta_empresa'),
            'description': 'Informações relacionadas à conta e relação com pessoa jurídica.',
        }),
    )

    def idade_em_anos(self, obj):
        if obj.data_nascimento:
            service = CalcularIdadePessoaFisicaService()
            idade_anos, _ = service.execute(obj)
            return idade_anos
        return None

    def idade_em_meses(self, obj):
        if obj.data_nascimento:
            service = CalcularIdadePessoaFisicaService()
            _, idade_meses = service.execute(obj)
            return idade_meses
        return None

    idade_em_anos.short_description = 'Idade (Anos)'
    idade_em_meses.short_description = 'Idade (Meses)'
