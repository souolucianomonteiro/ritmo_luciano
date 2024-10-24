"""
Módulo que define o contrato abstrato para o repositório de Profissao.

Este contrato especifica os métodos que devem ser implementados pelo repositório
concreto para gerenciar profissões no sistema.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.marketing.entities.profissao import ProfissaoDomain


class ProfissaoContract(ABC):
    """
    Contrato abstrato para o repositório de Profissao.

    Este contrato define as operações que o repositório concreto deve implementar.
    """

    @abstractmethod
    def salvar(self, profissao: ProfissaoDomain, user) -> None:
        """
        Salva uma instância de Profissao no repositório.

        Args:
            profissao (ProfissaoDomain): A instância de Profissao a ser salva.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, profissao_id: int) -> Optional[ProfissaoDomain]:
        """
        Busca uma instância de Profissao por seu ID.

        Args:
            profissao_id (int): O identificador único da profissão.

        Returns:
            Optional[ProfissaoDomain]: A instância de Profissao, ou None se não encontrada.
        """
        pass

    @abstractmethod
    def listar_todas(self) -> List[ProfissaoDomain]:
        """
        Lista todas as profissões.

        Returns:
            List[ProfissaoDomain]: Uma lista com todas as profissões.
        """
        pass
