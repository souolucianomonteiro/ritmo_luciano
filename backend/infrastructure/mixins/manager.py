"""
Manager customizado para implementar exclusão lógica (soft delete).

Este manager filtra automaticamente os registros excluídos (soft delete) em
consultas normais e oferece métodos para acessar registros excluídos ou
ativos conforme a necessidade.
"""

from django.db import models


class SoftDeleteManager(models.Manager):
    """
    Manager customizado que retorna apenas registros não excluídos
    (is_deleted=False) por padrão.
    """

    def get_queryset(self):
        """
        Sobrescreve o método get_queryset para retornar apenas registros que
        não foram excluídos logicamente (is_deleted=False).
        """
        return super().get_queryset().filter(is_deleted=False)

    def deleted(self):
        """
        Retorna apenas os registros que foram marcados como excluídos
        (is_deleted=True).
        """
        return super().get_queryset().filter(is_deleted=True)

    def with_deleted(self):
        """
        Retorna todos os registros, incluindo os excluídos (is_deleted=True).
        """
        return super().get_queryset()
