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
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.endereco import EnderecoModel


class PessoaJuridicaModel(
                            AuditMixin, SoftDeleteMixin,
                            InactivateMixin, models.Model
                        ):
    """
    Model que representa uma Pessoa Jurídica (empresa).

    Atributos:
        razao_social (str): Razão social da empresa.
        nome_fantasia (str): Nome fantasia da empresa.
        cnpj (str): CNPJ da empresa (único).
        inscricao_estadual (str): Inscrição estadual da empresa.
        usuario_titular (ForeignKey): Referência ao titular da empresa
        (usuário pessoa física).
        iniciador_id (ForeignKey): Referência à pessoa que criou a conta da 
        empresa (conta pessoa física).
    """
    razao_social = models.CharField(max_length=255)
    nome_fantasia = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=18, unique=True)  # CNPJ no formato 00.000.000/0000-00
    inscricao_estadual = models.CharField(max_length=14, blank=True, null=True)  # Inscrição estadual
    usuario_titular = models.ForeignKey(
        PessoaFisicaModel, on_delete=models.CASCADE, 
        related_name='empresas_titulares'
    )
    iniciador_id = models.ForeignKey(
        PessoaFisicaModel, on_delete=models.CASCADE, 
        related_name='empresas_iniciadas'
    )
    enderecos = models.ManyToManyField(EnderecoModel, related_name='pessoa_juridica_enderecos')
    
    class Meta:
        """
        Metadados da model PessoaJuridicaModel.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_pessoa_juridica'
        verbose_name = 'Pessoa Jurídica'
        verbose_name_plural = 'Pessoas Jurídicas'

    def __str__(self):
        return f"{self.razao_social} ({self.cnpj})"
