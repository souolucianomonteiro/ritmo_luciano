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
from domain.shared.plugins.repositories.plugin import PluginRepository
from domain.shared.plugins.aggregates.plugin import Plugin
from infrastructure.models.plugin import PluginModel

class DjangoPluginRepository(PluginRepository):
    """
    Implementação concreta do repositório do agregado Plugin utilizando o Django ORM.
    """

    def add(self, plugin: Plugin) -> None:
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
<<<<<<< HEAD
                permissoes=plugin_model.permissoes,
                historico_modificacoes=plugin_model.historico_modificacoes,
                tags=plugin_model.tags,
                dependencias=plugin_model.dependencias,
                criado_em=plugin_model.created_at,
                atualizado_em=plugin_model.updated_at,
                ativo=plugin_model.ativo,
=======
                permissoes=list(plugin_model.permissoes.all()),
                historico_modificacoes=list(plugin_model.historico_modificacoes.all()),
                tags=list(plugin_model.tags.all()),
                dependencias=list(plugin_model.dependencias.all()),
                templates=list(plugin_model.templates.all())
>>>>>>> models
            )
        except PluginModel.DoesNotExist:
            return None

    def update(self, plugin: Plugin) -> None:
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

    def delete(self, plugin_id: UUID) -> None:
        plugin_model = PluginModel.objects.get(pk=plugin_id)  # pylint: disable=no-member
        plugin_model.delete()

    def list(self) -> List[Plugin]:
        plugin_models = PluginModel.objects.all()  # pylint: disable=no-member
        return [
            Plugin(
<<<<<<< HEAD
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
=======
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

    def list_by_categoria(self, categoria_id: UUID) -> List[Plugin]:
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
>>>>>>> models

    def list_by_tipo(self, tipo_plugin_id: UUID) -> List[Plugin]:
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
