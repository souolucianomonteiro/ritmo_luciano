"""
    Módulo responsável pela definição da model ComentarioPost.

    Este módulo define a model ComentarioPost, que representa um comentário
    feito por um usuário em uma postagem no blog.

    Classes:
    ComentarioPost: Model que representa um comentário em uma postagem de blog.
"""

from django.db import models
from infrastructure.models.shared.resources.localizacao import Localizacao  


class ComentarioPost(models.Model):
    """
    Model que representa um comentário em uma postagem de blog.
    """

    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comentarios')
    comentario = models.TextField()
    data_comentario = models.DateTimeField(auto_now_add=True)
    ip_origem = models.GenericIPAddressField(null=True, blank=True)  # Armazena o IP de origem do comentário
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True, blank=True, related_name='comentarios')
    status = models.CharField(max_length=20, default='aguardando')

    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_comentario_post'
        verbose_name = 'Comentário do Post'
        verbose_name_plural = 'Comentários dos Posts'
        ordering = ['-data_comentario']

    def __str__(self):
        return f"Comentário {str(self.comentario)[:50]} no post {getattr(self.post, 'title', 'Título não disponível')}"
