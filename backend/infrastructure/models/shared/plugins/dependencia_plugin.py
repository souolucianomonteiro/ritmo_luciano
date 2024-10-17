# backend/infrastructure/models/dependencia_model.py
# type: ignore

from uuid import uuid4
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin


class DependenciaModel (
            AuditMixin, SoftDeleteMixin, InactivateMixin, models.Model):

    """
    Model de infraestrutura para representar a entidade Dependência 
    entre plugins.

    Atributos:
        plugin (ForeignKey): Referência ao plugin que possui a dependência.
        dependencia_plugin (ForeignKey): Referência ao plugin que
        é a dependência.
    """

    PLUGIN = 'plugin'
    BIBLIOTECA = 'biblioteca'
    SERVICO = 'serviço'
    OUTRO = 'outro'

    TIPO_DEPENDENCIA_CHOICES = [
        (PLUGIN, 'Plugin'),
        (BIBLIOTECA, 'Biblioteca'),
        (SERVICO, 'Serviço'),
        (OUTRO, 'Outro'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    plugin = models.ForeignKey(
        'PluginModel', 
        on_delete=models.CASCADE, 
        related_name='dependencia_plugin_set')  
    tipo_dependencia = models.CharField(max_length=50, choices=TIPO_DEPENDENCIA_CHOICES, default=PLUGIN)
    dependencia_plugin = models.ForeignKey('PluginModel', null=True, blank=True, on_delete=models.CASCADE)
    nome_dependencia = models.CharField(max_length=255, null=True, blank=True)
    url_dependencia = models.URLField(null=True, blank=True)

    class Meta:
        """
        Metadados para a model PluginModel.

        Define o rótulo da aplicação, o nome singular e plural para exibição
        no Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_dependencia_plugin'
        verbose_name = 'Dependência do Plugin'
        verbose_name_plural = 'Dependências do Plugin'
