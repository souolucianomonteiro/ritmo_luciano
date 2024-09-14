"""
Mixin para implementar inativação em models Django.

Este mixin adiciona funcionalidade de inativação aos modelos, permitindo
marcar registros como inativos e reativá-los posteriormente.
"""

from django.db import models
from django.utils.timezone import now
from .mixin_base import MixinBase


class InactivateMixin(MixinBase):
    """
    Mixin que adiciona campos e métodos para inativação em models.

    Atributos:
        is_active (bool): Indica se o registro está ativo.
        inactivated_at (datetime): Armazena a data e hora da inativação.
    """

    is_active = models.BooleanField(default=True)
    inactivated_at = models.DateTimeField(null=True, blank=True)

    def inativar(self):
        """
        Marca o registro como inativo e define a data e hora da inativação.
        """
        self.is_active = False
        self.inactivated_at = now()
        self.save()

    def reativar(self):
        """
        Restaura o registro marcado como inativo, tornando-o ativo novamente.
        """
        self.is_active = True
        self.inactivated_at = None
        self.save()

    class Meta:
        """
        Metadados para a classe modelo.

        Define que a classe é abstrata, ou seja, não será criada uma tabela
        diretamente para este modelo no banco de dados. Outras classes podem
        herdar este modelo e estender sua funcionalidade.
        """
        abstract = True
