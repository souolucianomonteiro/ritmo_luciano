"""
Módulo responsável pela definição da model PluginModel.

Este módulo define a model PluginModel, que representa um plugin na aplicação.
A model inclui campos para armazenar informações sobre o nome, tipo, categoria,
artefato, template, configuração, versão, documentação, permissões, histórico
de modificações, tags, dependências e estado de ativação. Além disso, ela
utiliza mixins para fornecer funcionalidades adicionais como auditoria,
exclusão lógica, inativação e controle de status.

Classes:
    PluginModel: Model que representa um plugin, com todos os seus atributos e
    funcionalidades associadas.
"""
import uuid
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.status import StatusMixin
from infrastructure.models.categoria import CategoriaModel
from infrastructure.models.tipo_plugin import TipoPluginModel
from infrastructure.models.artefato_plugin import ArtefatoPluginModel


class PluginModel(
    AuditMixin,
    SoftDeleteMixin,
    InactivateMixin,
    StatusMixin,
    models.Model
):
    """
    Model para a persistência do agregado Plugin no banco de dados.
    Inclui informações essenciais sobre o plugin, como nome, versão, status,
    documentação, permissões, histórico de modificações, tags e dependências.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    tipo_plugin = models.ForeignKey(TipoPluginModel, on_delete=models.CASCADE)
    versao = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    artefato_plugin = models.ForeignKey(ArtefatoPluginModel, on_delete=models.
                                        CASCADE, null=True, blank=True)
    documentacao = models.TextField(null=True, blank=True)
    permissoes = models.JSONField(default=list)
    historico_modificacoes = models.JSONField(default=list)
    tags = models.JSONField(default=list)
    dependencias = models.JSONField(default=list)

    class Meta:
        """
        Metadados para a model PluginModel.

        Define o rótulo da aplicação, o nome singular e plural para exibição
        no Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_plugin'
        verbose_name = 'Plugin'
        verbose_name_plural = 'Plugins'
