"""
Módulo que define o contrato abstrato para o repositório de Localizacao.

Este contrato especifica os métodos que devem ser implementados pelo repositório
concreto para gerenciar dados de geolocalização no sistema.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.shared.resources.entities.localizacao import Localizacao


class LocalizacaoContract(ABC):
    """
    Contrato abstrato para o repositório de Localizacao.

    Este contrato define as operações que o repositório concreto deve
    implementar
    para manipular e gerenciar as localizações no sistema.
    """

    @abstractmethod
    def salvar(self, localizacao: Localizacao) -> None:
        """
        Salva uma instância de Localizacao no repositório.

        Args:
            localizacao (Localizacao): A instância de Localizacao a ser salva.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, localizacao_id: int) -> Optional[Localizacao]:
        """
        Busca uma instância de Localizacao por seu ID.

        Args:
            localizacao_id (int): O identificador único da Localizacao.

        Returns:
            Optional[Localizacao]: A instância de Localizacao, ou None se não
            encontrada.
        """
        pass

    @abstractmethod
    def listar_todas(self) -> List[Localizacao]:
        """
        Lista todas as instâncias de Localizacao.

        Returns:
            List[Localizacao]: Uma lista com todas as instâncias de
            Localizacao.
        """
        pass
