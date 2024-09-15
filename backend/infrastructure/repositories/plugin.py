# pylint: disable=no-member
"""
Módulo responsável pela implementação concreta do repositório de Plugins na
camada de infraestrutura.

Este módulo contém a classe `PluginRepositoryConcrete`, que fornece métodos
para a persistência, recuperação e remoção de agregados do tipo Plugin,
utilizando o ORM do Django para interagir com o banco de dados.
"""
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.repositories.plugin import PluginRepository
from domain.shared.plugins.aggregates.plugin import Plugin
from infrastructure.models.plugin import PluginModel


class PluginRepositoryConcrete(PluginRepository):
    """
    Implementação concreta do repositório de Plugin na camada de
    infraestrutura.
    """

    def obter_por_id(self, plugin_id: int) -> Optional[Plugin]:
        try:
            plugin_model = PluginModel.objects.get(id=plugin_id, ativo=True)
            return Plugin(
                id=plugin_model.id,
                uuid=plugin_model.uuid,
                categoria=plugin_model.categoria,
                tipo_plugin=plugin_model.tipo_plugin,
                nome=plugin_model.nome,
                descricao=plugin_model.descricao,
                artefato_plugin=plugin_model.artefato_plugin,
                versao=plugin_model.versao,
                status=plugin_model.status,
                documentacao=plugin_model.documentacao,
                caminho_arquivo=plugin_model.caminho_arquivo,
                permissoes=plugin_model.permissoes,
                historico_modificacoes=plugin_model.historico_modificacoes,
                tags=plugin_model.tags,
                dependencias=plugin_model.dependencias,
                criado_em=plugin_model.created_at,
                atualizado_em=plugin_model.updated_at,
                ativo=plugin_model.ativo,
            )
        except PluginModel.DoesNotExist:
            return None

    def obter_por_uuid(self, uuid: UUID) -> Optional[Plugin]:
        try:
            plugin_model = PluginModel.objects.get(uuid=uuid, ativo=True)
            return self._model_para_entidade(plugin_model)
        except PluginModel.DoesNotExist:
            return None

    def listar(self) -> List[Plugin]:
        plugins = PluginModel.objects.filter(ativo=True)
        return [
            Plugin(
                id=plugin.id,
                uuid=plugin.uuid,
                categoria=plugin.categoria,
                tipo_plugin=plugin.tipo_plugin,
                nome=plugin.nome,
                descricao=plugin.descricao,
                artefato_plugin=plugin.artefato_plugin,
                versao=plugin.versao,
                status=plugin.status,
                documentacao=plugin.documentacao,
                caminho_arquivo=plugin.caminho_arquivo,
                permissoes=plugin.permissoes,
                historico_modificacoes=plugin.historico_modificacoes,
                tags=plugin.tags,
                dependencias=plugin.dependencias,
                criado_em=plugin.created_at,
                atualizado_em=plugin.updated_at,
                ativo=plugin.ativo,
            ) for plugin in plugins
        ]

    def salvar(self, plugin: Plugin) -> None:
        PluginModel.objects.update_or_create(
            id=plugin.id,
            defaults={
                'uuid': plugin.uuid,
                'nome': plugin.nome,
                'categoria': plugin.categoria,
                'tipo_plugin': plugin.tipo_plugin,
                'descricao': plugin.descricao,
                'artefato_plugin': plugin.artefato_plugin,
                'versao': plugin.versao,
                'status': plugin.status,
                'documentacao': plugin.documentacao,
                'caminho_arquivo': plugin.caminho_arquivo,
                'permissoes': plugin.permissoes,
                'historico_modificacoes': plugin.historico_modificacoes,
                'tags': plugin.tags,
                'dependencias': plugin.dependencias,
                'ativo': plugin.ativo,
            }
        )

    def remover(self, plugin_id: int) -> None:
        try:
            plugin = PluginModel.objects.get(id=plugin_id)
            plugin.soft_delete()
        except PluginModel.DoesNotExist:
            pass
