

from django.db import models
from infrastructure.mixins.audit import AuditMixin


class CategoriaPost(AuditMixin, models.Model):
    """
    Model que representa uma categoria associada a postagens no blog.

    Atributos:
        nome (CharField): O nome da categoria.
        descricao (TextField): Uma breve descrição da categoria.
        blog (ForeignKey): Relaciona a categoria ao blog específico.
    """
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)  # Adicionando a descrição
    
    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_categoria_post'
        verbose_name = 'Categoria de Post'
        verbose_name_plural = 'Categorias de Posts'

    def __str__(self):
        return str(self.nome)
