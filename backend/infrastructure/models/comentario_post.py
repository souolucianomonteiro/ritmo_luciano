"""
    Módulo responsável pela definição da model ComentarioPost.

    Este módulo define a model ComentarioPost, que representa um comentário
    feito por um usuário em uma postagem no blog.

    Classes:
    ComentarioPost: Model que representa um comentário em uma postagem de blog.
"""

from django.db import models
from infrastructure.models.post import Post
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.status import StatusMixin


class ComentarioPost(AuditMixin, SoftDeleteMixin, InactivateMixin, StatusMixin, models.Model):
    """
    Model que representa um comentário em uma postagem de blog.

    Atributos:
        post (ForeignKey): Referência ao post associado ao comentário.
        autor (ForeignKey): Referência ao autor do comentário (presumidamente uma pessoa física).
        texto (TextField): O conteúdo do comentário.
        data_comentario (DateTimeField): Data e hora do comentário.
        status (CharField): Estado do comentário (aguardando, aprovado, publicado).
    """

    STATUS_CHOICES = [
        ('aguardando', 'Aguardando Aprovação'),
        ('aprovado', 'Aprovado'),
        ('publicado', 'Publicado'),
    ]

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(PessoaFisicaModel, on_delete=models.CASCADE)
    texto = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aguardando')

    class Meta:
        """
        Metadados para a model ComentarioPost.

        Define o comportamento da model no Django, incluindo o nome da tabela
        e as opções de ordenação padrão.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_comentario_post'
        verbose_name = 'Comentário do Post'
        verbose_name_plural = 'Comentários dos Posts'
        ordering = ['-data_comentario']

    def __str__(self):
        """
        Retorna a representação do comentário em formato de string.
        """
        return f"Comentário por {self.autor} em {self.post}"
