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
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.models.blog.categoria_post import CategoriaPost
from infrastructure.models.blog.tag_post import TagPost


class Blog(
            AuditMixin, InactivateMixin, SoftDeleteMixin,
            models.Model
        ):
    """
    Model que representa um blog no sistema.

    Um blog pode conter várias postagens, categorias e tags. Ele também
    está relacionado a um site específico.

    Atributos:
        title (CharField): O título do blog.
        description (TextField): Uma breve descrição do blog.
        proprietario (ForeignKey): O proprietário do blog, relacionado à PessoaFisicaModel.
        site (ForeignKey): O site ao qual este blog pertence.
        categorias (ManyToManyField): As categorias associadas ao blog.
        tags (ManyToManyField): As tags associadas ao blog.
    """

    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    proprietario = models.ForeignKey(PessoaFisicaModel, on_delete=models.CASCADE, related_name='blogs')
    site = models.ForeignKey('CustomSite', on_delete=models.CASCADE, related_name='blogs')
    # Relacionamento com categorias e tags
    categorias = models.ManyToManyField(CategoriaPost, related_name='blogs', blank=True)
    tags = models.ManyToManyField(TagPost, related_name='blogs', blank=True)

    class Meta:
        """
        Metadados para a model Blog.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_blog'
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return str(self.title)
