# backend/infrastructure/models/template_plugin_model.py

from django.db import models
from uuid import uuid4

class TemplatePluginModel(models.Model):
    """
    Model para representar templates associados a plugins.

    Atributos:
        id (UUID): Identificador único do template.
        plugin (ForeignKey): Referência ao plugin ao qual o template está associado.
        nome_template (CharField): Nome descritivo do template.
        caminho_arquivo (CharField): Caminho do arquivo de template no sistema de arquivos.
        contexto_placeholder (CharField, opcional): Contexto específico para o qual o template foi criado.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    plugin = models.ForeignKey('PluginModel', on_delete=models.CASCADE, related_name='templates')
    nome_template = models.CharField(max_length=255)
    caminho_arquivo = models.CharField(max_length=255)
    contexto_placeholder = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'template_plugin'
        verbose_name = 'Template de Plugin'
        verbose_name_plural = 'Templates de Plugin'

    def __str__(self):
        return f"{self.nome_template} ({self.plugin})"
