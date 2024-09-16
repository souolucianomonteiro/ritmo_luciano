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
    Implementação concreta do repositório de Permissões de Plugins utilizando
    o Django ORM.
    """

    def add(self, permissao: PermissaoPlugin) -> None:
        PermissaoPluginModel.objects.create(
            id=permissao.id,
            plugin_id=permissao.plugin_id,
            codename=permissao.codename,
            name=permissao.name
        )

    def get(self, permissao_id: UUID) -> Optional[PermissaoPlugin]:
        try:
            permissao_model = PermissaoPluginModel.objects.get(pk=permissao_id) # pylint: disable=no-member
            return PermissaoPlugin(
                id=permissao_model.id,
                plugin_id=permissao_model.plugin_id,
                codename=permissao_model.codename,
                name=permissao_model.name
            )
        except PermissaoPluginModel.DoesNotExist:
            return None

    def update(self, permissao: PermissaoPlugin) -> None:
        permissao_model = PermissaoPluginModel.objects.get(pk=permissao.id)  # pylint: disable=no-member
        permissao_model.codename = permissao.codename
        permissao_model.name = permissao.name
        permissao_model.save()

    def delete(self, permissao_id: UUID) -> None:
        permissao_model = PermissaoPluginModel.objects.get(pk=permissao_id)  # pylint: disable-no-member
        permissao_model.delete()

    def list(self) -> List[PermissaoPlugin]:
        permissao_models = PermissaoPluginModel.objects.all()  # pylint: disable=no-member
        return [
            PermissaoPlugin(
                id=permissao.id,
                plugin_id=permissao.plugin_id,
                codename=permissao.codename,
                name=permissao.name
            )
            for permissao in permissao_models
        ]
