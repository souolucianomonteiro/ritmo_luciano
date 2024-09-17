"""
Módulo responsável pela definição da model Blog.

Este módulo define a model Blog, que representa um blog no sistema.
O blog pode conter várias postagens, categorias e tags, e está
relacionado a um site específico. A model Blog inclui funcionalidades
de auditoria, inativação, exclusão lógica e gerenciamento de status
através dos mixins.

Classes:
    Blog: Model que representa um blog no sistema.
"""

from django.db import models
from django.contrib.auth.models import User
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class Blog(
            AuditMixin, InactivateMixin, SoftDeleteMixin,
            StatusMixin, models.Model
        ):
    """
    Model que representa um blog no sistema.

    Um blog pode conter várias postagens, categorias e tags. Ele também
    está relacionado a um site específico.

    Atributos:
        title (CharField): O título do blog.
        description (TextField): Uma breve descrição do blog.
        owner (ForeignKey): O proprietário do blog, relacionado ao User.
        site (ForeignKey): O site ao qual este blog pertence.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    site = models.ForeignKey('CustomSite', on_delete=models.CASCADE, related_name='blogs')

    class Meta:
        """
        Metadados para a model Blog.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        db_table = 'blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return str(self.title)
