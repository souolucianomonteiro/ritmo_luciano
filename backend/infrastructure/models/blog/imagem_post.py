
from django.db import models


class ImagemPost(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='imagens')
    nome = models.CharField(max_length=255, null=False, blank=False)  # Nome da imagem
    imagem = models.ImageField(upload_to='uploads/posts/')
    legenda = models.CharField(max_length=255, null=True, blank=True)
    data_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model ImagemPost.

        Define o nome da tabela no banco de dados, e opções de ordenação.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_imagem_post'
        verbose_name = 'Imagem do Post'
        verbose_name_plural = 'Imagens do Post'

    def __str__(self):
        return str(self.nome)  # Retorna o nome da imagem como representação
