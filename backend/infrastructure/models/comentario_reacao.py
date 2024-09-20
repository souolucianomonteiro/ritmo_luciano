from django.db import models
from infrastructure.models.comentario_post import ComentarioPost
from infrastructure.models.pessoa_fisica_tipo import PessoaFisicaTipo
from infrastructure.models.reacao_detalhe import ReacaoDetalhe


class ComentarioReacao(models.Model):
    """
    Model que representa a reação de um usuário a um comentário em um post.

    Atributos:
        comentario (ForeignKey): Referência ao comentário associado à reação.
        autor (ForeignKey): Referência ao autor (PessoaFisicaTipo) que realizou a reação.
        reacao (ForeignKey): Referência ao tipo de reação (detalhada em ReacaoDetalhe).
        data_reacao (DateTimeField): Data e hora da reação.
    """
    comentario = models.ForeignKey(ComentarioPost, on_delete=models.CASCADE, related_name='reacoes')
    autor = models.ForeignKey(PessoaFisicaTipo, on_delete=models.CASCADE, related_name='reacoes_comentario')
    reacao = models.ForeignKey(ReacaoDetalhe, on_delete=models.CASCADE, related_name='reacoes_comentario')
    data_reacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model ComentarioReacao.

        Define o comportamento da model no Django, incluindo o nome da tabela
        e a ordenação padrão.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_comentario_reacao'
        verbose_name = 'Reação ao Comentário'
        verbose_name_plural = 'Reações aos Comentários'
        ordering = ['-data_reacao']

    def __str__(self):
        return f"{self.autor} reagiu com {self.reacao} no comentário {self.comentario}"
