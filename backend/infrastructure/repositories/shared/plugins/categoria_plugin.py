# pylint: disable=no-member:

from typing import Optional, List
from domain.shared.plugins.entities.categoria_plugin import (
                                        CategoriaPluginDomain)
from domain.shared.plugins.repositories.categoria_plugin import (
                                        CategoriaPluginRepository)
from infrastructure.models.shared.plugins.categoria_plugin import CategoriaPlugin


class DjangoCategoriaPluginRepository(CategoriaPluginRepository):
    """
    Repositório concreto para a entidade CategoriaPlugin.

    Implementa os métodos definidos no repositório abstrato,
    utilizando o Django ORM.
    """
    
    def save(self, categoria_plugin: CategoriaPluginDomain) -> (
                                        CategoriaPluginDomain):
        categoria_plugin_model = CategoriaPlugin(
            id=categoria_plugin.id,
            nome=categoria_plugin.nome
        )
        categoria_plugin_model.save()
        categoria_plugin.id = categoria_plugin_model.id
        return CategoriaPluginDomain(id=categoria_plugin_model.id,
                                     nome=categoria_plugin_model.nome)
    
    def get_by_id(self, categoria_plugin_id: int) -> Optional[
                                        CategoriaPluginDomain]:
        try:
            categoria_plugin_model = CategoriaPlugin.objects.get(
                                            id=categoria_plugin_id)
            return CategoriaPluginDomain(id=categoria_plugin_model.id,
                                         nome=categoria_plugin_model.nome)
        except CategoriaPlugin.DoesNotExist:
            return None
    
    def list_all(self) -> List[CategoriaPluginDomain]:
        categoria_plugins = CategoriaPlugin.objects.all()
        return [CategoriaPluginDomain(id=categoria.id, nome=categoria.nome)
                for categoria in categoria_plugins]

    def delete(self, categoria_plugin: CategoriaPluginDomain) -> None:
        CategoriaPlugin.objects.filter(id=categoria_plugin.id).delete()
