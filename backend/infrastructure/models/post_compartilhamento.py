from django.db import models
from infrastructure.models.post import Post
from infrastructure.models.pessoa_fisica_tipo import PessoaFisicaTipo


class PostCompartilhamento(models.Model):
    """
    Model que representa o compartilhamento de um post por um usuário (autor).

    Atributos:
        post (ForeignKey): O post que está sendo compartilhado.
        autor (ForeignKey): O autor (PessoaFisicaTipo) que compartilhou o post.
        data_compartilhamento (DateTimeField): Data e hora em que o post foi compartilhado.
    """

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='compartilhamentos')
    autor = models.ForeignKey(PessoaFisicaTipo, on_delete=models.CASCADE, related_name='compartilhamentos')
    data_compartilhamento = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model PostCompartilhamento.

        Define o comportamento da model no Django, incluindo o nome da tabela
        e a ordenação padrão.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_post_compartilhamento'
        verbose_name = 'Compartilhamento de Post'
        verbose_name_plural = 'Compartilhamentos de Posts'
        ordering = ['-data_compartilhamento']

    def __str__(self):
        return f"{self.autor} compartilhou o post {self.post}"
