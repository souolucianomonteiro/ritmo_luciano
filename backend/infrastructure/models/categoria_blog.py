"""
Módulo responsável pela definição da model Category.

Este módulo define a model Category, que representa uma categoria de
postagens de blog. As categorias ajudam a organizar as postagens
dentro de um blog. Cada categoria está relacionada a um blog específico
e inclui um nome e um slug para identificação.

Classes:
    Category: Model que representa uma categoria de postagens de blog.
"""
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class Category(
                AuditMixin, InactivateMixin, SoftDeleteMixin,
                StatusMixin, models.Model
            ):
    """
    Model que representa uma categoria de postagens de blog.

    Atributos:
        name (CharField): O nome da categoria.
        slug (SlugField): O slug da categoria usado na URL.
        blog (ForeignKey): O blog ao qual esta categoria pertence.
    """

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE,
                             related_name='categories')

    class Meta:
        """
        Metadados para a model Category.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_categoria_blog'
        verbose_name = 'Categoria de Blog'
        verbose_name_plural = 'Categorias de Blog'
    
    def __str__(self):
        return str(self.name)
