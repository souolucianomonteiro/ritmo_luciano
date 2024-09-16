# backend/domain/repositories/permissao_plugin_repository.py

# backend/domain/repositories/permissao_plugin_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.entities.permissao_plugin import PermissaoPlugin

class PermissaoPluginRepository(ABC):
    """
    Repositório abstrato para operações relacionadas às permissões de plugins.
    """

    @abstractmethod
    def add(self, permissao: PermissaoPlugin) -> None:
        pass

    @abstractmethod
    def get(self, permissao_id: UUID) -> Optional[PermissaoPlugin]:
        pass

    @abstractmethod
    def update(self, permissao: PermissaoPlugin) -> None:
        pass

    @abstractmethod
    def delete(self, permissao_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[PermissaoPlugin]:
        pass

    @abstractmethod
    def list_by_plugin(self, plugin_id: UUID) -> List[PermissaoPlugin]:
        pass
