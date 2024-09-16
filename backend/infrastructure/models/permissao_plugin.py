# backend/infrastructure/models/permissao_plugin_model.py

from uuid import uuid4
from django.contrib.auth.models import Permission
from django.db import models


class PermissaoPluginModel(Permission):
    """
    Extensão da model Permission do Django para acomodar permissões
    específicas de plugins.

    Atributos:
        id (UUID): Identificador único da permissão.
        plugin (ForeignKey): Referência ao plugin associado a essa permissão.
        codename (CharField): Código único da permissão.
        name (CharField): Nome descritivo da permissão.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    plugin = models.ForeignKey('PluginModel', on_delete=models.CASCADE,
                               related_name='permissoes')
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        """
        Metadados do modelo PermissaoPluginModel.

        Define o nome da tabela no banco de dados (`permissoes_plugin`), além
        de configurar o nome
        singular e plural das instâncias do modelo para exibição no Django
        Admin.
        """
        db_table = 'permissoes_plugin'
        unique_together = ('plugin', 'codename')
        verbose_name = 'Permissão de Plugin'
        verbose_name_plural = 'Permissões de Plugin'

    def __str__(self):
        return f"{self.plugin} - {self.codename}"
