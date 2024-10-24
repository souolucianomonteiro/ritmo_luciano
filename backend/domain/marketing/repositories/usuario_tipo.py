"""
Módulo que define o contrato abstrato para o repositório de UsuarioTipo.

Este contrato especifica os métodos que devem ser implementados pelo repositório
concreto para gerenciar tipos de usuário no sistema.
"""

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.marketing.entities.usuario_tipo import UsuarioTipoDomain


class UsuarioTipoContract(ABC):
    """
    Contrato abstrato para o repositório de UsuarioTipo.

    Este contrato define as operações que o repositório concreto deve implementar.
    """

    @abstractmethod
    def salvar(self, usuario_tipo: UsuarioTipoDomain, user) -> None:
        """
        Salva uma instância de UsuarioTipo no repositório.

        Args:
            usuario_tipo (UsuarioTipoDomain): A instância de UsuarioTipo a ser salva.
        """
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_tipo_id: int) -> Optional[UsuarioTipoDomain]:
        """
        Busca uma instância de UsuarioTipo por seu ID.

        Args:
            usuario_tipo_id (int): O identificador único do tipo de usuário.

        Returns:
            Optional[UsuarioTipoDomain]: A instância de UsuarioTipo, ou None se não encontrada.
        """
        pass

    @abstractmethod
    def listar_todos(self) -> List[UsuarioTipoDomain]:
        """
        Lista todos os tipos de usuário.

        Returns:
            List[UsuarioTipoDomain]: Uma lista com todos os tipos de usuário.
        """
        pass

