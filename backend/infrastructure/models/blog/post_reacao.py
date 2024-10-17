# pylint: disable=no-member
"""
Módulo que implementa a model da relação postagens x reações. 

"""
from django.db import models
from infrastructure.models.blog.post import Post


class PostReacao(models.Model):
    """
    Model que representa as reações diretas ao post.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='reacoes')
    reacao_tipo = models.CharField(max_length=20)  
    ip_origem = models.GenericIPAddressField(null=True, blank=True)
    localizacao = models.CharField(max_length=100, null=True, blank=True)
    data_reacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_post_reacao'
        verbose_name = 'Reação ao Post'
        verbose_name_plural = 'Reações aos Posts'
        ordering = ['-data_reacao']

    def __str__(self):
        return f"Reação {self.reacao_tipo} no post"
