# backend/domain/repositories/template_plugin_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.entities.template_plugin import TemplatePlugin


class TemplatePluginRepository(ABC):
    """
    Repositório abstrato para operações relacionadas a Templates de Plugins.
    """

    @abstractmethod
    def add(self, template: TemplatePlugin) -> None:
        pass

    @abstractmethod
    def get(self, template_id: UUID) -> Optional[TemplatePlugin]:
        pass

    @abstractmethod
    def update(self, template: TemplatePlugin) -> None:
        pass

    @abstractmethod
    def delete(self, template_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[TemplatePlugin]:
        pass

    @abstractmethod
    def list_by_plugin(self, plugin_id: UUID) -> List[TemplatePlugin]:
        pass

    @abstractmethod
    def list_by_contexto(self, contexto: str) -> List[TemplatePlugin]:
        pass
