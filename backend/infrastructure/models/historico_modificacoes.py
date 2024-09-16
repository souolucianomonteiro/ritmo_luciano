# backend/infrastructure/models/historico_modificacoes_model.py

# backend/infrastructure/models/historico_modificacoes_model.py

from uuid import uuid4
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin


class HistoricoModificacoesModel(AuditMixin, SoftDeleteMixin, InactivateMixin, models.Model):
    """
    Model de infraestrutura para representar o histórico de modificações de um plugin.

    Atributos:
        plugin (ForeignKey): Referência ao plugin modificado.
        data_modificacao (DateTimeField): Data e hora da modificação.
        usuario (str): Nome do usuário que realizou a modificação.
        descricao_modificacao (TextField): Descrição da modificação realizada.
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    plugin = models.ForeignKey('PluginModel', on_delete=models.CASCADE)
    data_modificacao = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=255)
    descricao_modificacao = models.TextField()

    class Meta:
        """
        Metadados do modelo HistoricoModificacoesModel.

        Define o nome da tabela no banco de dados (`historico_modificacoes`), além de configurar o nome
        singular e plural das instâncias do modelo para exibição no Django Admin.
        """
        db_table = 'historico_modificacoes'
        verbose_name = 'Histórico de Modificações'
        verbose_name_plural = 'Históricos de Modificações'
