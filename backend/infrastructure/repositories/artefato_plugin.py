# pylint: disable=no-member:
"""
Módulo que define a implementação concreta do repositório para a entidade
`ArtefatoPlugin` na camada de infraestrutura.

Este módulo contém a classe `ArtefatoPluginRepositoryConcrete`, que provê
os métodos para interação com o banco de dados, permitindo operações de
CRUD (Create, Read, Update, Delete) para a entidade `ArtefatoPlugin`.
"""
from typing import List, Optional
from domain.shared.plugins.repositories.artefato_plugin import (
                                        ArtefatoPluginRepository)
from domain.shared.plugins.entities.artefato_plugin import ArtefatoPlugin
from infrastructure.models.artefato_plugin import ArtefatoPluginModel


class ArtefatoPluginRepositoryConcrete(ArtefatoPluginRepository):
    """Implementação concreta do repositório de ArtefatoPlugin na camada 
    de infraestrutura."""

    def obter_por_id(self, artefato_plugin_id: int) -> Optional[ArtefatoPlugin]:
        try:
            artefato_plugin_model = ArtefatoPluginModel.objects.get(
                                    id=artefato_plugin_id, ativo=True)
            return ArtefatoPlugin(
                id=artefato_plugin_model.id,
                nome=artefato_plugin_model.nome,
                descricao=artefato_plugin_model.descricao,
                versao=artefato_plugin_model.versao,
                tipo_arquivo=artefato_plugin_model.tipo_arquivo,
                caminho_arquivo=artefato_plugin_model.caminho_arquivo,
                criado_em=artefato_plugin_model.created_at,
                atualizado_em=artefato_plugin_model.updated_at,
                criado_por=artefato_plugin_model.created_by,
                atualizado_por=artefato_plugin_model.updated_by,
                ativo=artefato_plugin_model.ativo,
            )
        except ArtefatoPluginModel.DoesNotExist:
            return None

    def listar(self) -> List[ArtefatoPlugin]:
        artefato_plugins = ArtefatoPluginModel.objects.filter(ativo=True)
        return [
            ArtefatoPlugin(
                id=artefato_plugin.id,
                nome=artefato_plugin.nome,
                descricao=artefato_plugin.descricao,
                versao=artefato_plugin.versao,
                tipo_arquivo=artefato_plugin.tipo_arquivo,
                caminho_arquivo=artefato_plugin.caminho_arquivo,
                criado_em=artefato_plugin.created_at,
                atualizado_em=artefato_plugin.updated_at,
                criado_por=artefato_plugin.created_by,
                atualizado_por=artefato_plugin.updated_by,
                ativo=artefato_plugin.ativo,
            ) for artefato_plugin in artefato_plugins
        ]

    def salvar(self, artefato_plugin: ArtefatoPlugin) -> None:
        ArtefatoPluginModel.objects.update_or_create(
            id=artefato_plugin.id,
            defaults={
                'nome': artefato_plugin.nome,
                'descricao': artefato_plugin.descricao,
                'versao': artefato_plugin.versao,
                'tipo_arquivo': artefato_plugin.tipo_arquivo,
                'caminho_arquivo': artefato_plugin.caminho_arquivo,
                'criado_em': artefato_plugin.criado_em,
                'atualizado_em': artefato_plugin.atualizado_em,
                'criado_por': artefato_plugin.criado_por,
                'atualizado_por': artefato_plugin.atualizado_por,
                'ativo': artefato_plugin.ativo,
            }
        )

    def remover(self, artefato_plugin_id: int) -> None:
        try:
            artefato_plugin = ArtefatoPluginModel.objects.get(
                                        id=artefato_plugin_id)
            artefato_plugin.soft_delete()
        except ArtefatoPluginModel.DoesNotExist:
            pass  # Ou trate o erro conforme necessário
