# shared/plugins/models/categoria_model.py

from django.db import models


class CategoriaModel(models.Model):
    """
    Model que representa uma categoria no banco de dados.

    Esta model é usada pela infraestrutura para a persistência
    de dados, mapeando os atributos de uma categoria para as
    """

    nome = models.CharField(max_length=50, unique=True)

    def __str__(self):
        """
        Retorna uma representação em string da categoria.

        :return: String representando a categoria.
        """
        return f"Categoria: {self.nome}"
    
    class Meta:
        """
        Metadados para a model TipoPluginModel.

        Define o rótulo da aplicação, o nome singular e plural para exibição
        no Django Admin.
        """
        app_label = 'infrastructure'
        verbose_name = 'Categoria do Plugin'
        verbose_name_plural = 'Categoria do Plugin'

