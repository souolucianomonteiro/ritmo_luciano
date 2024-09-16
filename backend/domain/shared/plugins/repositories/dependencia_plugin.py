# backend/domain/repositories/dependencia_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.entities.dependencia_plugin import Dependencia


class DependenciaRepository(ABC):
    """
    Repositório abstrato para operações relacionadas a Dependências.
    """

    @abstractmethod
    def add(self, dependencia: Dependencia) -> None:
        pass

    @abstractmethod
    def get(self, dependencia_id: UUID) -> Optional[Dependencia]:
        pass

    @abstractmethod
    def update(self, dependencia: Dependencia) -> None:
        pass

    @abstractmethod
    def delete(self, dependencia_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[Dependencia]:
        pass

    @abstractmethod
    def list_by_tipo(self, tipo_dependencia: str) -> List[Dependencia]:
        pass
