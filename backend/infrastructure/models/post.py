"""
Módulo responsável pela definição da model Post.

Este módulo define a model Post, que representa uma postagem de blog.
Cada postagem pertence a um blog e inclui funcionalidades de auditoria,
inativação, exclusão lógica e gerenciamento de status através dos mixins.
A model Post também gerencia o título, slug, conteúdo e data de publicação.

Classes:
    Post: Model que representa uma postagem de blog.
"""

from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class Post(
            AuditMixin, InactivateMixin, SoftDeleteMixin, StatusMixin,
            models.Model
            ):
    """
    Model que representa uma postagem de blog.

    Atributos:
        title (CharField): O título da postagem.
        slug (SlugField): O slug da postagem usado na URL.
        content (TextField): O conteúdo da postagem.
        published_date (DateTimeField): A data de publicação da postagem.
        author (ForeignKey): O autor da postagem, relacionado ao User.
        blog (ForeignKey): O blog ao qual esta postagem pertence.
    """

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='posts')

    class Meta:
        """
        Metadados para a model Post.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        db_table = 'post'
        verbose_name = 'Postagem de Blog'
        verbose_name_plural = 'Postagens de Blog'
        ordering = ['-published_date']

    def __str__(self):
        return str(self.title)
