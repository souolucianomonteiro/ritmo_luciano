"""
Módulo responsável pela definição da model Tag.

Este módulo define a model Tag, que representa uma tag associada a
postagens de blog. As tags ajudam a organizar e categorizar postagens
de maneira flexível. Cada tag está relacionada a um blog específico e
inclui um nome para identificação.

Classes:
    Tag: Model que representa uma tag de postagens de blog.
"""
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class Tag(AuditMixin, InactivateMixin,
          SoftDeleteMixin, StatusMixin, models.Model
          ):
    """
    Model que representa uma tag de postagens de blog.

    Atributos:
        name (CharField): O nome da tag.
        blog (ForeignKey): O blog ao qual esta tag pertence.
    """

    name = models.CharField(max_length=255)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='tags')

    class Meta:
        """
        Metadados para a model Tag.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        db_table = 'tag'
        verbose_name = 'Tag de Blog'
        verbose_name_plural = 'Tags de Blog'

    def __str__(self):
        return self.name