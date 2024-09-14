"""
Classe base para importação de models.Models
"""
from django.db import models


class MixinBase(models.Model):
    """
    Mixin base que herda de models.Model para evitar múltiplas heranças
    diretas de models.Model.
    """

    class Meta:
        """
        Metadados para a classe Mixin Base.

        Define que a classe é abstrata, ou seja, não será criada uma tabela
        diretamente para este modelo no banco de dados. Outras classes podem
        herdar este modelo e estender sua funcionalidade.
        """
        abstract = True
