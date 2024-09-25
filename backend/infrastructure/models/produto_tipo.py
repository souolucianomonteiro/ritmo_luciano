""""Módulo que implementa a model produto_tipo"""
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin


class TipoProdutoModel(
                    AuditMixin, InactivateMixin,
                    SoftDeleteMixin, models.Model
                    ):
    """
    Model que representa o tipo de produto no banco de dados.
    """
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_tipo_produto'
        verbose_name = 'Tipo de Produto'
        verbose_name_plural = 'Tipos de Produto'

    def __str__(self):
        return str(self.nome)
