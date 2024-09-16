# backend/domain/repositories/permissao_plugin_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.entities.permissao_plugin import PermissaoPlugin


class PermissaoPluginRepository(ABC):
    """
    Repositório abstrato para operações relacionadas a Permissões de Plugins.
    """

    @abstractmethod
    def add(self, permissao: PermissaoPlugin) -> None:
        """
        Adiciona uma nova permissão de plugin ao repositório.
        """
        pass

    @abstractmethod
    def get(self, permissao_id: UUID) -> Optional[PermissaoPlugin]:
        """
        Recupera uma permissão de plugin pelo seu ID.
        """
        pass

    @abstractmethod
    def update(self, permissao: PermissaoPlugin) -> None:
        """
        Atualiza uma permissão de plugin existente no repositório.
        """
        pass

    @abstractmethod
    def delete(self, permissao_id: UUID) -> None:
        """
        Remove uma permissão de plugin pelo seu ID.
        """
        pass

    @abstractmethod
    def list(self) -> List[PermissaoPlugin]:
        """
        Retorna uma lista de todas as permissões de plugins no repositório.
        """
        pass
