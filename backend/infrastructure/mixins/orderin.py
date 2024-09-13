"""
    Garantir que todos os modelos implementem uma ordem
    padrão ao serem consultados. Este mixin adiciona um
    campo de ordenação e configura o ordenamento padrão do modelo.
    Quando usar: Em qualquer modelo onde a ordenação seja importante
    para a apresentação dos dados.
"""

from django.db import models


class OrderingMixin(models.Model):
    """
    Mixin que adiciona um campo de ordenação e define uma
    ordem padrão para os registros.
    """
    order = models.PositiveIntegerField(default=0)

    class Meta:
        """
        Metadados para a classe modelo.

        Define que a classe é abstrata, ou seja, não será criada uma tabela
        diretamente para este modelo no banco de dados. Outras classes podem
        herdar este modelo e estender sua funcionalidade.
        """
        abstract = True
        ordering = ['order']
