"""
Módulo responsável pela definição da model ProfissaoModel.

Este módulo define a model ProfissaoModel, que utiliza mixins para auditoria,
ordenação, inativação e exclusão lógica, e armazena as profissões no sistema.
"""

from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.ordering import OrderingMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin


class ProfissaoModel(AuditMixin, OrderingMixin, InactivateMixin, SoftDeleteMixin, models.Model):
    """
    Model que representa uma profissão no banco de dados.

    Atributos:
        codigo (str): Código único da profissão.
        descricao (str): Descrição da profissão.
    """
    codigo = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        """
        Metadados da model ProfissaoModel.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_profissao'
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'
        ordering = ['order']

    def __str__(self):
        return f"{self.codigo} - {self.descricao}"
