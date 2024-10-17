"""
Módulo responsável pela definição da model PessoaFisicaModel.

Este módulo define a model PessoaFisicaModel, que representa uma pessoa física
no sistema.
A model inclui campos para armazenar informações pessoais, como nome, email,
CPF, data de nascimento, e aplica validações para garantir a integridade
desses dados.

Validações:
    - CPF: Verifica se o CPF fornecido é válido de acordo
    com as regras brasileiras.
    - Email: Verifica se o formato do email está correto.
    - Data de nascimento: Garante que a data de nascimento é plausível
    e não está no futuro.

Classes:
    PessoaFisicaModel: Model que representa uma pessoa física no banco
    de dados.
"""
from typing import List, Tuple
import re
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.status import StatusMixin
from infrastructure.models.marketing.endereco import EnderecoModel
from infrastructure.models.marketing.usuario_tipo import UsuarioTipo
from domain.shared.validations.valida_email import validar_email
from domain.shared.validations.valida_nascimento import validar_data_nascimento
from domain.shared.validations.valida_cpf import validar_cpf


class PessoaFisicaModel(
                        AbstractUser, AuditMixin, SoftDeleteMixin,
                        InactivateMixin, StatusMixin
                       ):
    """
    Model que representa uma pessoa física no sistema, atuando também como uma conta.
    
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
        usuario_tipo: Associações entre Pessoa Física e tipos de usuários.
    """
    STATUS_CHOICES: List[Tuple[str, str]] = [
        ('adimplente', 'Adimplente'),
        ('atraso', 'Pagamento em Atraso'),
        ('suspenso', 'Suspenso'),
        ('renegociacao', 'Com Renegociação'),
    ]        
    pessoa_fisica_id = models.AutoField(primary_key=True)
    conta_pessoa = models.BooleanField(default=True)
    situacao = models.CharField(max_length=255, choices=STATUS_CHOICES, default='adimplente')
    first_name = models.CharField('Primeiro Nome', max_length=150, blank=True)
    last_name = models.CharField('Sobrenome', max_length=150, blank=True)
    email = models.EmailField(unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    foto = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bios = models.TextField(max_length=500, null=True, blank=True)
    profissao = models.ForeignKey('ProfissaoModel', on_delete=models.SET_NULL, null=True, blank=True, related_name='pessoas_fisicas')
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

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'cpf']  # Campos obrigatórios para o cadastro

    iniciador_conta_empresa = models.BooleanField(default=False)
    enderecos = models.ManyToManyField(EnderecoModel, related_name='pessoas_fisicas', blank=True)
    tipos_de_usuario = models.ManyToManyField(
        UsuarioTipo,
        through='PessoaFisicaTipo',  # Model intermediária
        related_name='pessoas_fisicas'
    )

    # Adicionando related_name exclusivos para evitar conflitos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='pessoa_fisica_groups',  # Nome exclusivo para evitar conflito
        blank=True,
        help_text='Os grupos aos quais este usuário pertence.',
        verbose_name='Grupos'
    )
    
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='pessoa_fisica_permissions',  # Nome exclusivo para evitar conflito
        blank=True,
        help_text='Permissões específicas deste usuário.',
        verbose_name='Permissões de usuário'
    )

    def get_status_choices(self):
        return self.STATUS_CHOICES

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def clean(self):
        """
        Método de validação personalizado para PessoaFisicaModel.

        Este método valida o CPF, email, e data de nascimento.
        """
         # Remover caracteres não numéricos (como pontos e traço)
        self.cpf = re.sub(r'[^0-9]', '', self.cpf)

        try:
            validar_cpf(self.cpf)  # Chamada da função de validação do CPF
        except ValidationError as exc:
            raise ValidationError({"cpf": "CPF inválido."}) from exc

        # Valida o email usando a função personalizada
        validar_email(self.email)

        # Valida a data de nascimento usando a função personalizada
        validar_data_nascimento(self.data_nascimento)

    class Meta:
        """
        Metadados da model Pessoa Física.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_pessoa_fisica'
        verbose_name = 'Pessoa Física'
        verbose_name_plural = 'Pessoas Físicas'
