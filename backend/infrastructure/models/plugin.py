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
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.status import StatusMixin
from infrastructure.models.categoria_post import CategoriaModel
from infrastructure.models.tipo_plugin import TipoPluginModel
from infrastructure.models.artefato_plugin import ArtefatoPluginModel
from infrastructure.models.permissao_plugin import PermissaoPluginModel
from infrastructure.models.historico_modificacoes import (
                            HistoricoModificacoesModel)
from infrastructure.models.tag_plugin import TagPluginModel
from infrastructure.models.dependencia_plugin import DependenciaModel
from infrastructure.models.template_plugin import TemplatePluginModel

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
    documentação, permissões, histórico de modificações, tags, dependências,
    e templates.
    """
    id = models.UUIDField(primary_key=True, default=models.UUIDField, editable=False)
    nome = models.CharField(max_length=255)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    tipo_plugin = models.ForeignKey(TipoPluginModel, on_delete=models.CASCADE)
    versao = models.CharField(max_length=50)
    descricao = models.TextField(null=True, blank=True)
    artefato_plugin = models.ForeignKey(ArtefatoPluginModel, on_delete=models.CASCADE, null=True, blank=True)
    documentacao = models.TextField(null=True, blank=True)
    caminho_arquivo = models.CharField(max_length=500)
    
    permissoes = models.ManyToManyField(PermissaoPluginModel, related_name='plugins')
    historico_modificacoes = models.ManyToManyField(HistoricoModificacoesModel, related_name='plugins')
    tags = models.ManyToManyField(TagPluginModel, related_name='plugins')
    dependencias = models.ManyToManyField(DependenciaModel, related_name='plugins')
    templates = models.ManyToManyField(TemplatePluginModel, related_name='plugins')

    class Meta:
        app_label = 'infrastructure'
        db_table = 'infrastructure_plugin'
        verbose_name = 'Plugin'
        verbose_name_plural = 'Plugins'

