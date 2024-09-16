# backend/infrastructure/repositories/permissao_plugin_repository.py
# pylint: disable=no-member

from uuid import UUID
from typing import List, Optional
from domain.shared.plugins.repositories.permissao_plugin import (
                                        PermissaoPluginRepository)
from domain.shared.plugins.entities.permissao_plugin import PermissaoPlugin
from infrastructure.models.permissao_plugin import PermissaoPluginModel


class DjangoPermissaoPluginRepository(PermissaoPluginRepository):
    """
    Implementação concreta do repositório de permissões de plugins utilizando o Django ORM.
    """

    def add(self, permissao: PermissaoPlugin) -> None:
        PermissaoPluginModel.objects.create(
            id=permissao.id,
            name=permissao.name,
            codename=permissao.codename,
            content_type_id=permissao.content_type_id,
            plugin_id=permissao.plugin_id
        )

    def get(self, permissao_id: UUID) -> Optional[PermissaoPlugin]:
        try:
            permissao_model = PermissaoPluginModel.objects.get(pk=permissao_id)  # pylint: disable=no-member
            return PermissaoPlugin(
                id=permissao_model.id,
                name=permissao_model.name,
                codename=permissao_model.codename,
                content_type_id=permissao_model.content_type_id,
                plugin_id=permissao_model.plugin_id
            )
        except PermissaoPluginModel.DoesNotExist:
            return None

    def update(self, permissao: PermissaoPlugin) -> None:
        permissao_model = PermissaoPluginModel.objects.get(pk=permissao.id)  # pylint: disable=no-member
        permissao_model.name = permissao.name
        permissao_model.codename = permissao.codename
        permissao_model.content_type_id = permissao.content_type_id
        permissao_model.plugin_id = permissao.plugin_id
        permissao_model.save()

    def delete(self, permissao_id: UUID) -> None:
        permissao_model = PermissaoPluginModel.objects.get(pk=permissao_id)  # pylint: disable=no-member
        permissao_model.delete()

    def list(self) -> List[PermissaoPlugin]:
        permissao_models = PermissaoPluginModel.objects.all()  # pylint: disable=no-member
        return [
            PermissaoPlugin(
                id=permissao_model.id,
                name=permissao_model.name,
                codename=permissao_model.codename,
                content_type_id=permissao_model.content_type_id,
                plugin_id=permissao_model.plugin_id
            )
            for permissao_model in permissao_models
        ]

    def list_by_plugin(self, plugin_id: UUID) -> List[PermissaoPlugin]:
        permissao_models = PermissaoPluginModel.objects.filter(plugin_id=plugin_id)  # pylint: disable=no-member
        return [
            PermissaoPlugin(
                id=permissao_model.id,
                name=permissao_model.name,
                codename=permissao_model.codename,
                content_type_id=permissao_model.content_type_id,
                plugin_id=permissao_model.plugin_id
            )
            for permissao_model in permissao_models
        ]

