# pylint: disable=no-member

from typing import List, Optional
from domain.shared.plugins.entities.tag_plugin import TagPlugin
from domain.shared.plugins.repositories.tag_plugin import TagPluginRepository
from infrastructure.models.tag_plugin import TagPluginModel


class DjangoTagPluginRepository(TagPluginRepository):
    """
    Implementação concreta do repositório de Tags de Plugins utilizando o
    Django ORM.
    """

    def add(self, tag_plugin: TagPlugin) -> None:
        TagPluginModel.objects.create(nome=tag_plugin.nome)

    def get(self, tag_id: int) -> Optional[TagPlugin]:
        try:
            tag_plugin_model = TagPluginModel.objects.get(pk=id, is_deleted=False)
            return TagPlugin(id=tag_plugin_model.id, nome=tag_plugin_model.nome)
        except TagPluginModel.DoesNotExist:
            return None

    def update(self, tag_plugin: TagPlugin) -> None:
        tag_plugin_model = TagPluginModel.objects.get(pk=tag_plugin.id, is_deleted=False)
        tag_plugin_model.nome = tag_plugin.nome
        tag_plugin_model.save()

    def delete(self, tag_id: int) -> None:
        tag_plugin_model = TagPluginModel.objects.get(pk=id)
        tag_plugin_model.is_deleted = True
        tag_plugin_model.save()

    def list(self) -> List[TagPlugin]:
        tag_plugin_models = TagPluginModel.objects.filter(is_deleted=False)
        return [TagPlugin(id=tag_plugin.id, nome=tag_plugin.nome) for tag_plugin in tag_plugin_models]
