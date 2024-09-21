# pylint: disable=no-member
"""
Módulo que implementa a model da relação reações X comentário.

"""
from django.db import models
from infrastructure.models.comentario_post import ComentarioPost
from infrastructure.models.reacao_detalhe import ReacaoDetalhe
from infrastructure.models.localizacao import Localizacao
from infrastructure.models.pessoa_fisica import PessoaFisicaModel


class ReacaoComentario(models.Model):
    """
    Model que registra as reações em comentários de posts.
    
    Atributos:
        comentario: Referência ao comentário que recebeu a reação.
        reacao: Detalhes da reação (exemplo: curtir, gostar, etc.).
        localizacao: Localização de onde a reação foi feita.
        pessoa_fisica: Referência ao usuário que realizou a reação.
        data_reacao: Data e hora em que a reação foi feita.
    """
    comentario_post = models.ForeignKey(ComentarioPost, on_delete=models.CASCADE)
    reacao = models.ForeignKey(ReacaoDetalhe, on_delete=models.SET_NULL, null=True)
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True)
    pessoa_fisica = models.ForeignKey(PessoaFisicaModel, on_delete=models.SET_NULL, null=True, blank=True)
    data_reacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model Reação_Detalhe.

        Define o nome da tabela no banco de dados e os nomes legíveis no
        Django Admin.
        """     
        app_label = 'infrastructure'
        db_table = 'infrastructure_reacao_comentario'
        verbose_name = 'Reação em Comentário'
        verbose_name_plural = 'Reações em Comentários'

    def __str__(self):
        if hasattr(self, 'comentario_post') and self.comentario_post is not None:
            return f"Reação ao comentário '{self.comentario_post.comentario}' em {self.data_reacao}"
        return f"Reação sem título em {self.data_reacao}"

