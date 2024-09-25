from abc import ABC, abstractmethod
from typing import List, Optional
from domain.website.entities.profissao import Profissao


class ProfissaoRepository(ABC):
    """
    Interface para o repositório de Profissão.

    Define os métodos que devem ser implementados no repositório concreto.
    """

    @abstractmethod
    def save(self, profissao: 'Profissao') -> 'Profissao':
        pass

    @abstractmethod
    def find_by_id(self, profissao_id: int) -> Optional['Profissao']:
        pass

    @abstractmethod
    def find_all(self) -> List['Profissao']:
        pass

    @abstractmethod
    def delete(self, profissao_id: int) -> None:
        pass

