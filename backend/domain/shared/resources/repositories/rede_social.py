"""
Módulo que define o contrato abstrato para o repositório de RedeSocial.

Este contrato especifica os métodos que devem ser implementados pelo repositório
concreto para gerenciar redes sociais no sistema.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.shared.resources.entities.rede_social import RedeSocialDomain


class RedeSocialContract(ABC):
    """
    Contrato abstrato para o repositório de RedeSocial.

    Este contrato define as operações que o repositório concreto deve
    implementar
    para manipular e gerenciar as redes sociais no sistema.
    """

    @abstractmethod
    def salvar(self, rede_social: RedeSocialDomain) -> None:
        """
        Salva uma instância de RedeSocial no repositório.

        Args:
            rede_social (RedeSocialDomain): A instância de RedeSocial a ser
            salva.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, rede_social_id: int) -> Optional[RedeSocialDomain]:
        """
        Busca uma instância de RedeSocial por seu ID.

        Args:
            rede_social_id (int): O identificador único da RedeSocial.

        Returns:
            Optional[RedeSocialDomain]: A instância de RedeSocial, ou None se
            não encontrada.
        """
        pass

    @abstractmethod
    def listar_todas(self) -> List[RedeSocialDomain]:
        """
        Lista todas as instâncias de RedeSocial.

        Returns:
            List[RedeSocialDomain]: Uma lista com todas as redes sociais.
        """
        pass
