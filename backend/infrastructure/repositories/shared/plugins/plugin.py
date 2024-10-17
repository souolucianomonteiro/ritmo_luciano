# pylint: disable=no-member
"""
Módulo responsável pela implementação concreta do repositório de Plugins na
camada de infraestrutura.

Este módulo contém a classe `PluginRepositoryConcrete`, que fornece métodos
para a persistência, recuperação e remoção de agregados do tipo Plugin,
utilizando o ORM do Django para interagir com o banco de dados.
"""
# backend/infrastructure/repositories/plugin_repository.py

from uuid import UUID
from typing import List, Optional
from domain.shared.plugins.aggregates.plugin import Plugin
from domain.shared.plugins.repositories.plugin import PluginRepository
from infrastructure.models.shared.plugins.plugin import PluginModel


class DjangoPluginRepository(PluginRepository):
    """
    Implementação concreta do repositório do agregado Plugin utilizando o
    Django ORM.
    """

    def add(self, plugin: Plugin) -> None:
        try:
            PluginModel.objects.create(
                id=plugin.id,
                nome=plugin.nome,
                categoria_id=plugin.categoria_id,
                tipo_plugin_id=plugin.tipo_plugin_id,
                versao=plugin.versao,
                descricao=plugin.descricao,
                artefato_plugin_id=plugin.artefato_plugin_id,
                documentacao=plugin.documentacao,
                caminho_arquivo=plugin.caminho_arquivo
            )
        except Exception as e:
            raise ValueError(f"Erro ao adicionar o plugin: {str(e)}") from e

    def get(self, plugin_id: UUID) -> Optional[Plugin]:
        try:
            plugin_model = PluginModel.objects.get(pk=plugin_id)  # pylint: disable=no-member
            return Plugin(
                id=plugin_model.id,
                nome=plugin_model.nome,
                categoria_id=plugin_model.categoria_id,
                tipo_plugin_id=plugin_model.tipo_plugin_id,
                versao=plugin_model.versao,
                descricao=plugin_model.descricao,
                artefato_plugin_id=plugin_model.artefato_plugin_id,
                documentacao=plugin_model.documentacao,
                caminho_arquivo=plugin_model.caminho_arquivo,
                permissoes=list(plugin_model.permissoes.all()),
                historico_modificacoes=list(plugin_model.historico_modificacoes.all()),
                tags=list(plugin_model.tags.all()),
                dependencias=list(plugin_model.dependencias.all()),
                templates=list(plugin_model.templates.all())
            )
        except PluginModel.DoesNotExist:
            return None
        except Exception as e:
            raise ValueError(f"Erro ao recuperar o plugin: {str(e)}") from e

    def update(self, plugin: Plugin) -> None:
        try:
            plugin_model = PluginModel.objects.get(pk=plugin.id)  # pylint: disable=no-member
            plugin_model.nome = plugin.nome
            plugin_model.categoria_id = plugin.categoria_id
            plugin_model.tipo_plugin_id = plugin.tipo_plugin_id
            plugin_model.versao = plugin.versao
            plugin_model.descricao = plugin.descricao
            plugin_model.artefato_plugin_id = plugin.artefato_plugin_id
            plugin_model.documentacao = plugin.documentacao
            plugin_model.caminho_arquivo = plugin.caminho_arquivo
            
            # Atualizando as relações ManyToMany
            plugin_model.permissoes.set(plugin.permissoes)
            plugin_model.historico_modificacoes.set(plugin.historico_modificacoes)
            plugin_model.tags.set(plugin.tags)
            plugin_model.dependencias.set(plugin.dependencias)
            plugin_model.templates.set(plugin.templates)
            
            plugin_model.save()
        except Exception as e:
            raise ValueError(f"Erro ao atualizar o plugin: {str(e)}") from e

    def delete(self, plugin_id: UUID) -> None:
        try:
            plugin_model = PluginModel.objects.get(pk=plugin_id)  # pylint: disable=no-member
            plugin_model.delete()
        except Exception as e:
            raise ValueError(f"Erro ao deletar o plugin: {str(e)}") from e

    def list(self) -> List[Plugin]:
        try:
            plugin_models = PluginModel.objects.all()  # pylint: disable=no-member
            return [
                Plugin(
                    id=plugin_model.id,
                    nome=plugin_model.nome,
                    categoria_id=plugin_model.categoria_id,
                    tipo_plugin_id=plugin_model.tipo_plugin_id,
                    versao=plugin_model.versao,
                    descricao=plugin_model.descricao,
                    artefato_plugin_id=plugin_model.artefato_plugin_id,
                    documentacao=plugin_model.documentacao,
                    caminho_arquivo=plugin_model.caminho_arquivo,
                    permissoes=list(plugin_model.permissoes.all()),
                    historico_modificacoes=list(plugin_model.historico_modificacoes.all()),
                    tags=list(plugin_model.tags.all()),
                    dependencias=list(plugin_model.dependencias.all()),
                    templates=list(plugin_model.templates.all())
                )
                for plugin_model in plugin_models
            ]
        except Exception as e:
            raise ValueError(f"Erro ao listar os plugins: {str(e)}") from e

    def list_by_categoria(self, categoria_id: UUID) -> List[Plugin]:
        try:
            plugin_models = PluginModel.objects.filter(categoria_id=categoria_id)  # pylint: disable=no-member
            return [
                Plugin(
                    id=plugin_model.id,
                    nome=plugin_model.nome,
                    categoria_id=plugin_model.categoria_id,
                    tipo_plugin_id=plugin_model.tipo_plugin_id,
                    versao=plugin_model.versao,
                    descricao=plugin_model.descricao,
                    artefato_plugin_id=plugin_model.artefato_plugin_id,
                    documentacao=plugin_model.documentacao,
                    caminho_arquivo=plugin_model.caminho_arquivo,
                    permissoes=list(plugin_model.permissoes.all()),
                    historico_modificacoes=list(plugin_model.historico_modificacoes.all()),
                    tags=list(plugin_model.tags.all()),
                    dependencias=list(plugin_model.dependencias.all()),
                    templates=list(plugin_model.templates.all())
                )
                for plugin_model in plugin_models
            ]
        except Exception as e:
            raise ValueError(f"Erro ao listar os plugins por categoria: {str(e)}") from e

    def list_by_tipo(self, tipo_plugin_id: UUID) -> List[Plugin]:
        try:
            plugin_models = PluginModel.objects.filter(tipo_plugin_id=tipo_plugin_id)  # pylint: disable=no-member
            return [
                Plugin(
                    id=plugin_model.id,
                    nome=plugin_model.nome,
                    categoria_id=plugin_model.categoria_id,
                    tipo_plugin_id=plugin_model.tipo_plugin_id,
                    versao=plugin_model.versao,
                    descricao=plugin_model.descricao,
                    artefato_plugin_id=plugin_model.artefato_plugin_id,
                    documentacao=plugin_model.documentacao,
                    caminho_arquivo=plugin_model.caminho_arquivo,
                    permissoes=list(plugin_model.permissoes.all()),
                    historico_modificacoes=list(plugin_model.historico_modificacoes.all()),
                    tags=list(plugin_model.tags.all()),
                    dependencias=list(plugin_model.dependencias.all()),
                    templates=list(plugin_model.templates.all())
                )
                for plugin_model in plugin_models
            ]
        except Exception as e:
            raise ValueError(f"Erro ao listar os plugins por tipo: {str(e)}") from e
