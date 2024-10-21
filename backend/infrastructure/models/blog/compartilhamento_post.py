# pylint: disable=no-member
""""Módulo que implementa a model da relação compartilhamento x post"""

from django.db import models
from infrastructure.models.blog.post import Post
from infrastructure.models.shared.resources.localizacao import Localizacao
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel


class CompartilhamentoPost(models.Model):
    """
    Model que registra o compartilhamento de posts.
    
    Atributos:
        post: Referência ao post compartilhado.
        localizacao: Localização de onde o compartilhamento foi feito.
        pessoa_fisica: Referência ao usuário que compartilhou o post.
        data_compartilhamento: Data e hora em que o compartilhamento foi feito.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True)
    pessoa_fisica = models.ForeignKey(PessoaFisicaModel, on_delete=models.SET_NULL, null=True, blank=True)
    data_compartilhamento = models.DateTimeField(auto_now_add=True)
    total_compartilhamentos = models.IntegerField(default=0)

    def incrementar_compartilhamentos(self):
        """ atualiza o total de compartilhamentos"""
        self.total_compartilhamentos += 1
        self.save()
    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_compartilhamento_post'
        verbose_name = 'Compartilhamento de Post'
        verbose_name_plural = 'Compartilhamentos de Post'

    def __str__(self):
        return f"Compartilhamento de {self.post.title} por {self.pessoa_fisica}"
