# pylint: disable=no-member
"""Módulo implmenta a model da relação votacao x post"""

from django.db import models
from infrastructure.models.blog.post import Post
from infrastructure.models.shared.resources.localizacao import Localizacao
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel


class VotacaoPost(models.Model):
    """
    Model que registra as votações em posts (curtir, não curtir, etc.).
    
    Atributos:
        post: Referência ao post votado.
        localizacao: Localização de onde a votação foi feita.
        pessoa_fisica: Referência ao usuário que votou no post.
        voto: Indica se o voto foi positivo ou negativo.
        data_votacao: Data e hora em que a votação foi feita.
    """
    VOTE_CHOICES = [
        ('positivo', 'Positivo'),
        ('negativo', 'Negativo')
    ]
    
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True)
    pessoa_fisica = models.ForeignKey(PessoaFisicaModel, on_delete=models.SET_NULL, null=True, blank=True)
    voto = models.CharField(max_length=10, choices=VOTE_CHOICES, default='positivo')
    data_votacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_votacao_post'
        verbose_name = 'Votação de Post'
        verbose_name_plural = 'Votações de Post'

    def __str__(self):
        return f"Votação de {self.post.title} - {self.voto}"
