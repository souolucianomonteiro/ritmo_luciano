# backend/domain/repositories/historico_modificacoes_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.entities.historico_modificacoes import (
                                            HistoricoModificacoes)


class HistoricoModificacoesRepository(ABC):
    """
    Repositório abstrato para operações relacionadas ao Histórico de Modificações.
    """

    @abstractmethod
    def add(self, historico_modificacoes: HistoricoModificacoes) -> None:
        pass

    @abstractmethod
    def get(self, historico_modificacoes_id: UUID) -> Optional[
                                        HistoricoModificacoes]:
        pass

    @abstractmethod
    def update(self, historico_modificacoes: HistoricoModificacoes) -> None:
        pass

    @abstractmethod
    def delete(self, historico_modificacoes_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[HistoricoModificacoes]:
        pass
