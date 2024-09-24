"""Módulo que implementa o repositório abstrato de reacao_tipo"""

from typing import List, Optional
from abc import ABC, abstractmethod
from domain.blog.value_objects.reacao_tipo import ReacaoTipoDomain


class ReacaoTipoRepository(ABC):
    """
    Repositório abstrato para manipulação dos dados relacionados ao tipo de reação (ReacaoTipo).

    Métodos:
        list_all(): Retorna uma lista com todos os tipos de reações.
        get_by_id(id: int): Retorna um tipo de reação específico pelo ID.
    """

    @abstractmethod
    def list_all(self) -> List[ReacaoTipoDomain]:
        """Retorna uma lista com todos os tipos de reações."""
        pass

    @abstractmethod
    def get_by_id(self, reacao_tipo_id: int) -> Optional[ReacaoTipoDomain]:
        """Retorna um tipo de reação específico pelo ID."""
        pass
