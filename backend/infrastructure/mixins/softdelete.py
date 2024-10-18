"""
Mixin para implementar soft delete em models Django.

Este mixin adiciona funcionalidade de exclusão lógica aos modelos, permitindo
marcar registros como excluídos sem removê-los fisicamente do banco de dados.
"""

from django.db import models
from django.utils.timezone import now
from .mixin_base import MixinBase
from .manager import SoftDeleteManager


class SoftDeleteMixin(MixinBase):
    """
    Mixin que adiciona a funcionalidade de exclusão lógica (soft delete) para
    modelos Django. Em vez de excluir registros do banco de dados, esta
    abordagem marca os registros como inativos.

    Atributos:
        is_deleted (bool): Indica se o registro foi marcado como excluído.
        deleted_at (datetime): Armazena a data e hora da exclusão lógica do
        registro.
    """

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False):
        """
        Sobrescreve o método delete padrão para realizar uma exclusão lógica,
        marcando o registro como excluído e armazenando a data e hora da
        exclusão.
        """
        self.is_deleted = True
        self.deleted_at = now()
        self.save()

    def restore(self):
        """
        Método para restaurar um registro que foi excluído logicamente,
        revertendo os campos is_deleted e deleted_at.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.save()

    class Meta:
        """
        Metadados para a classe modelo.

        Define que a classe é abstrata, ou seja, não será criada uma tabela
        diretamente para este modelo no banco de dados. Outras classes podem
        herdar este modelo e estender sua funcionalidade.
        """
        abstract = True
