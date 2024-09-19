from django.contrib import admin
from infrastructure.models.pessoa_fisica import PessoaFisicaModel

@admin.register(PessoaFisicaModel)
class PessoaFisicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PessoaFisicaModel no Django Admin.
    Organiza os campos da pessoa física em seções no formulário.
    """

    list_display = ('nome', 'email', 'cpf', 'genero', 'idade_anos', 'idade_meses', 'conta_pessoa', 'iniciador_conta_empresa')
    search_fields = ('nome', 'email', 'cpf')
    list_filter = ('genero', 'conta_pessoa', 'iniciador_conta_empresa')
    ordering = ('nome',)

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'email', 'cpf', 'data_nascimento', 'idade_anos', 'idade_meses', 'genero'),
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
