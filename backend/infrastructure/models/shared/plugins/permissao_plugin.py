# backend/infrastructure/models/permissao_plugin_model.py

from django.contrib.auth.models import Permission
from django.db import models


class PermissaoPluginModel(Permission):
    """
    Extensão da model Permission do Django para acomodar permissões específicas de plugins.
    Herda os campos 'id' e 'name' da classe base Permission e evita conflitos.
    """

    # Adicionando uma ForeignKey para o PluginModel, sem redefinir campos existentes
    plugin = models.ForeignKey(
        'PluginModel', 
        on_delete=models.CASCADE, 
        related_name='permissao_plugin_set')
    class Meta:

        app_label = 'infrastructure'
        db_table = 'infrastructure_permissao_plugin'
        verbose_name = 'Permissão de Plugin'
        verbose_name_plural = 'Permissões de Plugin'
        app_label = 'infrastructure'

    def __str__(self):
        return f"{self.name} ({self.plugin})"
