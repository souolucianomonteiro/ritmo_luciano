from django.db import models
from infrastructure.models.post import Post
from infrastructure.models.pessoa_fisica_tipo import PessoaFisicaTipo


class PostVotacao(models.Model):
    """
    Model que representa o sistema de votação em um post por um usuário.

    Atributos:
        post (ForeignKey): O post que está sendo votado.
        autor (ForeignKey): O autor (PessoaFisicaTipo) que realizou a votação.
        valor_voto (IntegerField): O valor do voto, que pode ser um número de 1 a 5.
        data_votacao (DateTimeField): Data e hora em que o voto foi registrado.
    """

    VOTO_CHOICES = [(i, str(i)) for i in range(1, 6)]  # Define um range de 1 até 5

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='votacoes')
    autor = models.ForeignKey(PessoaFisicaTipo, on_delete=models.CASCADE, related_name='votacoes')
    valor_voto = models.IntegerField(choices=VOTO_CHOICES)
    data_votacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model PostVotacao.

        Define o comportamento da model no Django, incluindo o nome da tabela
        e a ordenação padrão.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_post_votacao'
        verbose_name = 'Votação de Post'
        verbose_name_plural = 'Votações de Posts'
        ordering = ['-data_votacao']

    def __str__(self):
        return f"{self.autor} votou {self.valor_voto} no post {self.post}"
