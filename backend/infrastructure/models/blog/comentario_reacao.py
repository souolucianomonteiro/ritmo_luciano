from django.db import models


class ComentarioReacaoModel(models.Model):
    """
    Model que representa as reações feitas aos comentários de um post.
    """
    reacao_tipo = models.CharField(max_length=20)  # Tipo de reação (curtir, não curtir, etc.)
    ip_origem = models.GenericIPAddressField(null=True, blank=True)
    localizacao = models.CharField(max_length=100, null=True, blank=True)
    data_reacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_reacao_comentario'
        verbose_name = 'Reação ao Comentário'
        verbose_name_plural = 'Reações aos Comentários'
        ordering = ['-data_reacao']

    def __str__(self):
        return f"Reação {self.reacao_tipo} no comentário"
