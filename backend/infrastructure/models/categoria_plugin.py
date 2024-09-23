from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin

class CategoriaPlugin(AuditMixin, InactivateMixin, models.Model):
    """
    Model que representa uma categoria de plugin.
    
    Atributos:
        id (AutoField): Identificador único da categoria.
        nome (CharField): Nome da categoria.
    """
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)

    class Meta:
        """
        Metadados para a model CategoriaPlugin.
        
        Define o nome da tabela no banco de dados e outros comportamentos.
        """
        app_label = 'infrastructure'  # Nome do aplicativo onde a model está
        db_table = 'infrastructure_categoria_plugin'  # Nome da tabela no banco de dados
        verbose_name = 'Categoria de Plugin'
        verbose_name_plural = 'Categorias de Plugin'

    def __str__(self):
        return str(self.nome)
