"""
    Módulo que implementa a model de visualização de post com geolocalização. 
"""
from django.db import models
from infrastructure.models.localizacao import Localizacao
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.post import Post


class VisualizacaoPost(models.Model):
    """
    Model que registra as visualizações de um post no sistema.
    
    Atributos:
        post: Referência ao post visualizado.
        localizacao: Localização de onde a visualização foi feita.
        pessoa_fisica: Referência ao usuário (opcional) que visualizou o post.
        data_visualizacao: Data e hora em que a visualização foi feita.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='visualizacoes')
    localizacao = models.ForeignKey(Localizacao, on_delete=models.SET_NULL, null=True)
    pessoa_fisica = models.ForeignKey(PessoaFisicaModel, on_delete=models.SET_NULL, null=True, blank=True)  # Campo pode ficar vazio
    data_visualizacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model UsuarioTipo.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_visualizacao_post'
        verbose_name = 'Visualização de Post'
        verbose_name_plural = 'Visualizações de Post'

    def __str__(self):
    # Verifica se a ForeignKey 'post' está disponível e acessa 'post.title'
        if self.post and hasattr(self.post, 'title'):
            return f"Visualização do post '{self.post.title}' em {self.data_visualizacao}"
        return f"Visualização sem título em {self.data_visualizacao}"

