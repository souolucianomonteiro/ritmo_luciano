# backend/infrastructure/repositories/template_plugin_repository.py
# pylint: disable=no-member

from uuid import UUID
from typing import List, Optional
from domain.shared.plugins.repositories.template_plugin import (
                                        TemplatePluginRepository)
from domain.shared.plugins.entities.template_plugin import TemplatePlugin
from infrastructure.models.template_plugin import TemplatePluginModel


class DjangoTemplatePluginRepository(TemplatePluginRepository):
    """
    Implementação concreta do repositório de Templates de Plugins utilizando
    o Django ORM.
    """

    def add(self, template: TemplatePlugin) -> None:
        TemplatePluginModel.objects.create(
            id=template.id,
            plugin_id=template.plugin_id,
            nome_template=template.nome_template,
            caminho_arquivo=template.caminho_arquivo,
            contexto_placeholder=template.contexto_placeholder
        )

    def get(self, template_id: UUID) -> Optional[TemplatePlugin]:
        try:
            template_model = TemplatePluginModel.objects.get(pk=template_id)  # pylint: disable=no-member
            return TemplatePlugin(
                id=template_model.id,
                plugin_id=template_model.plugin_id,
                nome_template=template_model.nome_template,
                caminho_arquivo=template_model.caminho_arquivo,
                contexto_placeholder=template_model.contexto_placeholder
            )
        except TemplatePluginModel.DoesNotExist:
            return None

    def update(self, template: TemplatePlugin) -> None:
        template_model = TemplatePluginModel.objects.get(pk=template.id)  # pylint: disable=no-member
        template_model.nome_template = template.nome_template
        template_model.caminho_arquivo = template.caminho_arquivo
        template_model.contexto_placeholder = template.contexto_placeholder
        template_model.save()

    def delete(self, template_id: UUID) -> None:
        template_model = TemplatePluginModel.objects.get(pk=template_id)  # pylint: disable=no-member
        template_model.delete()

    def list(self) -> List[TemplatePlugin]:
        template_models = TemplatePluginModel.objects.all()  # pylint: disable=no-member
        return [
            TemplatePlugin(
                id=template_model.id,
                plugin_id=template_model.plugin_id,
                nome_template=template_model.nome_template,
                caminho_arquivo=template_model.caminho_arquivo,
                contexto_placeholder=template_model.contexto_placeholder
            )
            for template_model in template_models
        ]

    def list_by_plugin(self, plugin_id: UUID) -> List[TemplatePlugin]:
        template_models = TemplatePluginModel.objects.filter(plugin_id=plugin_id)  # pylint: disable=no-member
        return [
            TemplatePlugin(
                id=template_model.id,
                plugin_id=template_model.plugin_id,
                nome_template=template_model.nome_template,
                caminho_arquivo=template_model.caminho_arquivo,
                contexto_placeholder=template_model.contexto_placeholder
            )
            for template_model in template_models
        ]

    def list_by_contexto(self, contexto: str) -> List[TemplatePlugin]:
        template_models = TemplatePluginModel.objects.filter(contexto_placeholder=contexto)  # pylint: disable=no-member
        return [
            TemplatePlugin(
                id=template_model.id,
                plugin_id=template_model.plugin_id,
                nome_template=template_model.nome_template,
                caminho_arquivo=template_model.caminho_arquivo,
                contexto_placeholder=template_model.contexto_placeholder
            )
            for template_model in template_models
        ]
