"""
Módulo responsável pela definição do repositório abstrato de UsuarioTipo.

Este módulo define a interface para o repositório de UsuarioTipo, especificando
os métodos que devem ser implementados por repositórios concretos que utilizam
esta entidade.

Classes:
    UsuarioTipoRepository: Classe abstrata que define as operações de persistência
    e recuperação de dados relacionadas à entidade UsuarioTipo.
"""
from abc import ABC, abstractmethod
from typing import Optional, List
from domain.website.entities.usuario_tipo import UsuarioTipoDomain


class UsuarioTipoRepository(ABC):
    """
    Repositório abstrato para a entidade UsuarioTipo.

    Define os métodos para persistir e recuperar os dados da entidade UsuarioTipo.
    """

    @abstractmethod
    def save(self, usuario_tipo: UsuarioTipoDomain) -> UsuarioTipoDomain:
        """
        Salva ou atualiza uma instância de UsuarioTipo no repositório.
        
        Args:
            usuario_tipo (UsuarioTipoDomain): Instância de dominio a ser salva.
            
        Returns:
            UsuarioTipoDomain: A instância salva ou atualizada.
        """
        pass

    @abstractmethod
    def get_by_id(self, usuario_tipo_id: int) -> Optional[UsuarioTipoDomain]:
        """
        Recupera uma instância de UsuarioTipo por seu ID.
        
        Args:
            usuario_tipo_id (int): ID do tipo de usuário a ser recuperado.
        
        Returns:
            Optional[UsuarioTipoDomain]: A instância encontrada ou None.
        """
        pass

    @abstractmethod
    def delete(self, usuario_tipo: UsuarioTipoDomain) -> None:
        """
        Exclui uma instância de UsuarioTipo do repositório.
        
        Args:
            usuario_tipo (UsuarioTipoDomain): A instância a ser excluída.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[UsuarioTipoDomain]:
        """
        Lista todas as instâncias de UsuarioTipo no repositório.
        
        Returns:
            List[UsuarioTipoDomain]: Lista de instâncias de tipos de usuários.
        """
        pass
