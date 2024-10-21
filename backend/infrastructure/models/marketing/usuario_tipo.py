"""
Módulo responsável pela definição da model UsuarioTipoModel.

Este módulo define a model UsuarioTipoModel, que utiliza mixins para auditoria,
ordenação, inativação e exclusão lógica, e armazena os tipos de usuário no sistema.
"""

from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.ordering import OrderingMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin


class UsuarioTipoModel(AuditMixin, OrderingMixin, InactivateMixin, SoftDeleteMixin, models.Model):
    """
    Model que representa um tipo de usuário no banco de dados.

    Atributos:
        nome (str): Nome do tipo de usuário.
        descricao (Optional[str]): Descrição do tipo de usuário.
    """
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        """
        Metadados da model UsuarioTipoModel.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_usuario_tipo'
        verbose_name = 'Tipo de Usuário'
        verbose_name_plural = 'Tipos de Usuário'
        ordering = ['order']

    def __str__(self):
        return f"{self.nome} - {self.descricao or 'Sem descrição'}"
