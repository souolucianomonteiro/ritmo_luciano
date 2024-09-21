from django.contrib import admin
from infrastructure.models.pessoa_fisica import PessoaFisicaModel

@admin.register(PessoaFisicaModel)
class PessoaFisicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PessoaFisicaModel no Django Admin.
    Organiza os campos da pessoa física em seções no formulário.
    """

    list_display = ('primeiro_nome', 'sobrenome', 'email', 'cpf', 'genero', 'idade_em_anos', 'idade_em_meses', 'conta_pessoa', 'iniciador_conta_empresa')
    search_fields = ('primeiro_nome', 'sobrenome', 'email', 'cpf')
    list_filter = ('genero', 'conta_pessoa', 'iniciador_conta_empresa')
    ordering = ('primeiro_nome', 'sobrenome')

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('primeiro_nome', 'sobrenome', 'email', 'cpf', 'data_nascimento', 'idade_em_anos', 'idade_em_meses', 'genero'),
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

    # Método para exibir idade em anos no admin
    def idade_em_anos(self, obj):
        return obj.idade_anos

    # Método para exibir idade em meses no admin
    def idade_em_meses(self, obj):
        return obj.idade_meses

    # Definir as descrições para os campos de idade no admin
    idade_em_anos.short_description = 'Idade (Anos)'
    idade_em_meses.short_description = 'Idade (Meses)'
