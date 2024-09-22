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
from djangocms_text_ckeditor.fields import HTMLField
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin
from infrastructure.models.pessoa_fisica_tipo import PessoaFisicaTipo
from infrastructure.models.comentario_post import ComentarioPost
from infrastructure.models.tag_post import TagPost


class Post(
            AuditMixin, SoftDeleteMixin, StatusMixin,
            models.Model
        ):
    """
    Model que representa uma postagem de blog.

    Atributos:
        title (CharField): O título da postagem.
        slug (SlugField): O slug da postagem usado na URL.
        content (TextField): O conteúdo da postagem.
        published_date (DateTimeField): A data de publicação da postagem.
        autor (ForeignKey): O autor da postagem, relacionado ao
        PessoaFisicaTipo.
        blog (ForeignKey): O blog ao qual esta postagem pertence.
        comentarios (ManyToManyField): Relacionamento com ComentárioPost.
        reacoes (ManyToManyField): Relacionamento para reações (a implementar).
        numero_compartilhamentos (IntegerField): Número de vezes que o post
        foi compartilhado.
        compartilhado (BooleanField): Indica se o post foi compartilhado.
        status (CharField): Estado da postagem (rascunho, concluído, publicado,
        removido).
    """

    STATUS_CHOICES = [
        ('rascunho', 'Rascunho'),
        ('concluido', 'Concluído'),
        ('publicado', 'Publicado'),
        ('removido', 'Removido'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    content = HTMLField()
    published_date = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(PessoaFisicaTipo, on_delete=models.CASCADE, related_name='posts')
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, related_name='posts')
    comentarios = models.ManyToManyField(ComentarioPost, related_name='posts', blank=True)
    reacoes = models.ManyToManyField('ReacaoDetalhe', related_name='posts', blank=True)  # A implementar
    numero_compartilhamentos = models.IntegerField(default=0)
    compartilhado = models.BooleanField(default=False)
    tags = models.ManyToManyField(TagPost, related_name='posts', blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='rascunho')

    class Meta:
        """
        Metadados para a model Post.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_post'
        verbose_name = 'Postagem de Blog'
        verbose_name_plural = 'Postagens de Blog'
        ordering = ['-published_date']

    def __str__(self):
        return str(self.title)

    def get_status_choices(self):
        """
        Retorna as opções de status definidas na model Post.
        Isso é necessário para o funcionamento correto do StatusMixin.
        """
        return self.STATUS_CHOICES
