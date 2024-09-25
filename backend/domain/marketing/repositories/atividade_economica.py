"""
Módulo responsável pela definição da interface do repositório
AtividadeEconomicaRepository.

Este módulo define a interface do repositório abstrato para a entidade
Atividade Econômica.
A interface descreve os métodos que devem ser implementados pelos repositórios
concretos
para persistência e recuperação de dados relacionados à atividade econômica.

Classes:
    AtividadeEconomicaRepository: Interface que define os métodos do
    repositório de Atividade Econômica.
"""
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.marketing.entities.atividade_economica import (
                                    AtividadeEconomicaDomain)


class AtividadeEconomicaRepository(ABC):
    """
    Interface para o repositório de Atividade Econômica.

    Define os métodos que devem ser implementados no repositório concreto.
    """

    @abstractmethod
    def save(self, atividade_economica: AtividadeEconomicaDomain) -> (
                                            AtividadeEconomicaDomain):
        pass

    @abstractmethod
    def find_by_id(self, id: int) -> Optional[AtividadeEconomicaDomain]:
        pass

    @abstractmethod
    def find_all(self) -> List[AtividadeEconomicaDomain]:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass
