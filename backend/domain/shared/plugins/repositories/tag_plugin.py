# backend/domain/repositories/tag_plugin_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.shared.plugins.entities.tag_plugin import TagPlugin


class TagPluginRepository(ABC):
    """
    Repositório abstrato para operações relacionadas a Tags de Plugins.
    """

    @abstractmethod
    def add(self, tag_plugin: TagPlugin) -> None:
        pass

    @abstractmethod
    def get(self, tag_id: int) -> Optional[TagPlugin]:
        pass

    @abstractmethod
    def update(self, tag_plugin: TagPlugin) -> None:
        pass

    @abstractmethod
    def delete(self, tag_id: int) -> None:
        pass

    @abstractmethod
    def list(self) -> List[TagPlugin]:
        pass
