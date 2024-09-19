"""
Módulo responsável pela definição da model PessoaFisicaModel.

Este módulo define a model PessoaFisicaModel, que representa uma pessoa física
no sistema.
A model inclui campos para armazenar informações pessoais, como nome, email,
CPF, data de nascimento, e aplica validações para garantir a integridade desses dados.

Validações:
    - CPF: Verifica se o CPF fornecido é válido de acordo
    com as regras brasileiras.
    - Email: Verifica se o formato do email está correto.
    - Data de nascimento: Garante que a data de nascimento é plausível
    e não está no futuro.

Classes:
    PessoaFisicaModel: Model que representa uma pessoa física no banco de dados.
"""
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.status import StatusMixin
from infrastructure.models.endereco import EnderecoModel
from domain.shared.validations.valida_email import validar_email
from domain.shared.validations.valida_data import validar_data_nascimento
from domain.shared.validations.valida_cpf import validar_cpf
from .profissao import ProfissaoModel


class PessoaFisicaModel(
                        User, AuditMixin, SoftDeleteMixin,
                        InactivateMixin, StatusMixin
                       ):
    """
    Model que representa uma pessoa física no sistema, atuando também como uma
    conta.
    
    Atributos:
        primeiro_nome: Primeiro nome da pessoa física.
        sobrenome: Sobrenome da pessoa física.
        email: Email da pessoa física (usado como login).
        data_nascimento: Data de nascimento da pessoa física.
        profissao: Referência à profissão da pessoa física.
        ocupacao: Ocupação atual da pessoa física.
        whatsapp: Número de WhatsApp da pessoa física.
        redes_sociais: Links para as redes sociais da pessoa física.
        cpf: CPF da pessoa física, identificador único.
        genero: Identidade de gênero da pessoa física.
        conta_pessoa: Indica se essa pessoa física é também uma conta no
        sistema.
        iniciador_conta_empresa: Indica se essa pessoa física iniciou uma
        conta de pessoa jurídica.
    """
    id = models.AutoField(primary_key=True)  
    conta_pessoa = models.BooleanField(default=True)
    primeiro_nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    profissao = models.ForeignKey(ProfissaoModel, on_delete=models.SET_NULL, null=True, blank=True, related_name='pessoas_fisicas')
    ocupacao = models.CharField(max_length=255, null=True, blank=True)
    whatsapp = models.CharField(max_length=20, null=True, blank=True)
    redes_sociais = models.CharField(max_length=500, null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    genero = models.CharField(max_length=20, choices=[
        ('homem', 'Homem'),
        ('mulher', 'Mulher'),
        ('homem bissexual', 'Homem Bissexual'),
        ('homem trans', 'Homem Trans'),
        ('mulher bissexual', 'Mulher Bissexual'),
        ('mulher trans', 'Mulher Trans')
    ])
    iniciador_conta_empresa = models.BooleanField(default=False)
    enderecos = models.ManyToManyField(EnderecoModel, related_name='pessoas_fisicas', blank=True)

    class Meta:
        
        app_label = 'infrastructure'
        db_table = 'infrastructure_pessoa_fisica'
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'

    def __str__(self):
        return f'{self.primeiro_nome} {self.sobrenome}'


def clean(self):
        """
        Método de validação personalizado para PessoaFisicaModel.

        Este método valida o CPF, email, e data de nascimento.
        """
        # Valida o CPF usando a função personalizada
        try:
            validar_cpf(self.cpf)
        except ValidationError as exc:
            raise ValidationError({"cpf": "CPF inválido."}) from exc

        # Valida o email usando a função personalizada
        validar_email(self.email)

        # Valida a data de nascimento usando a função personalizada
        validar_data_nascimento(self.data_nascimento)
