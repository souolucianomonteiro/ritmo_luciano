# pylint: disable=unused-variable
"""
Módulo responsável pela definição da model PessoaJuridicaModel.

Este módulo contém a implementação da model PessoaJuridicaModel, que
representa uma entidade de pessoa jurídica no sistema. A model inclui
informações como razão social, nome fantasia, CNPJ, inscrição estadual,
além de referências ao titular (usuário pessoa física) e ao iniciador
da conta da empresa.

Classes:
    PessoaJuridicaModel: Model que representa uma pessoa jurídica e
    suas informações associadas.
"""
from django.db import models
from domain.shared.validations.valida_cnpj import validar_cnpj
from domain.shared.exceptions.validation_exception import ValidationException
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.status import StatusMixin  # Incluindo o StatusMixin
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.marketing.endereco import EnderecoModel
from infrastructure.models.marketing.atividade_economica import (
                                        AtividadeEconomicaModel)
from infrastructure.models.shared.resources.rede_social import RedeSocialModel


class PessoaJuridicaModel(
    AuditMixin, SoftDeleteMixin, InactivateMixin, StatusMixin, models.Model
):
    """
    Model que representa uma Pessoa Jurídica no sistema.

    Atributos:
        razao_social (str): Razão social da empresa.
        nome_fantasia (str): Nome fantasia da empresa.
        cnpj (str): CNPJ da empresa, que deve ser único e validado.
        inscricao_estadual (Optional[str]): Inscrição estadual da empresa.
        administradores (ManyToMany): Relacionamento com os administradores (Pessoa Física).
        iniciador (ForeignKey): Referência para a pessoa física que iniciou a empresa.
        enderecos (ManyToMany): Relacionamento com os endereços da empresa.
        atividades_economicas (ManyToMany): Relacionamento com as atividades econômicas.
        website (Optional[str]): Website da empresa.
        redes_sociais (ManyToMany): Relacionamento com redes sociais da empresa.
        status (CharField): Status da empresa (ativo, inativo, suspenso etc.)
    """

    STATUS_CHOICES = [
        ('criada', 'Criada'),
        ('ativada', 'Ativada'),
        ('inativada', 'Inativada'),
        ('suspensa', 'Suspensa'),
    ]

    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)  # 18 por incluir a formatação do CNPJ
    inscricao_estadual = models.CharField(max_length=20, null=True, blank=True)

    # Relacionamento com Pessoa Física (administradores)
    administradores = models.ManyToManyField(
        PessoaFisicaModel, related_name='empresas_administradas', blank=True
    )

    # O iniciador da empresa (pessoa física que criou a conta)
    iniciador = models.ForeignKey(
        PessoaFisicaModel, on_delete=models.PROTECT, related_name='empresas_iniciadas'
    )

    # Relacionamento com Endereços
    enderecos = models.ManyToManyField(EnderecoModel, related_name='empresas')

    # Relacionamento com Atividades Econômicas
    atividades_economicas = models.ManyToManyField(
        AtividadeEconomicaModel, related_name='empresas', blank=True
    )

    # Website (opcional)
    website = models.URLField(max_length=255, null=True, blank=True)

    # Relacionamento com Redes Sociais
    redes_sociais = models.ManyToManyField(RedeSocialModel, related_name='empresas', blank=True)

    # Status da Pessoa Jurídica (Criada,Ativada, Inativada, Suspensa, etc.)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='criada')

    def get_status_choices(self):
        """
        Retorna as opções de status disponíveis para a Pessoa Jurídica.
        
        Returns:
            list: Lista de tuplas com os status disponíveis.
        """
        return self.STATUS_CHOICES

    def clean(self):
        """
        Validações customizadas para a model PessoaJuridica.

        Este método garante que o CNPJ é válido.
        """
        # Valida o CNPJ
        if not validar_cnpj(self.cnpj):
            raise ValidationException({'cnpj': 'CNPJ inválido.'})

    def __str__(self):
        """
        Retorna a representação amigável da Pessoa Jurídica.

        Returns:
            str: Razão social e CNPJ.
        """
        return f'{self.razao_social} - CNPJ: {self.cnpj}'

    class Meta:
        """
        Metadados da model PessoaJuridica.

        Define o nome da tabela no banco de dados, o app ao qual pertence e nomes
        amigáveis para exibição no Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_pessoa_juridica'
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'

