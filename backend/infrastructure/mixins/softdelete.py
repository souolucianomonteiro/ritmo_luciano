"""
Mixin para implementar soft delete em models Django.

Este mixin adiciona funcionalidade de exclusão lógica aos modelos, permitindo
marcar registros como excluídos sem removê-los fisicamente do banco de dados.
"""

from django.db import models
from django.utils.timezone import now


class SoftDeleteMixin(models.Model):
    """
    Mixin que adiciona campos e métodos para exclusão lógica em models.

    Atributos:
        is_deleted (bool): Indica se o registro foi excluído.
        deleted_at (datetime): Armazena a data e hora da exclusão.
    """

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def marcar_como_excluido(self):
        """
        Marca o registro como excluído e define a data e hora da exclusão.
        """
        self.is_deleted = True
        self.deleted_at = now()
        self.save()

    def restaurar(self):
        """
        Restaura o registro marcado como excluído, removendo a marcação.
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
