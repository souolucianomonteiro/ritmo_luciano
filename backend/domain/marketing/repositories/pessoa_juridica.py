"""
Módulo responsável pela definição do contrato abstrato para PessoaJuridica.

Este módulo define a interface PessoaJuridicaContract, que estabelece os
métodos essenciais para a persistência e gerenciamento da entidade de domínio 
PessoaJuridica. Ele abrange operações como recuperação, criação, atualização 
e exclusão de registros de pessoas jurídicas, além de métodos para gerenciar 
relacionamentos com administradores, atividades econômicas, endereços e redes sociais.

Classes:
    PessoaJuridicaContract: Interface abstrata para o repositório de PessoaJuridica.
"""

from abc import ABC, abstractmethod
from typing import Optional, List
from domain.marketing.entities.pessoa_juridica import PessoaJuridicaDomain


class PessoaJuridicaContract(ABC):
    """
    Repositório abstrato para a entidade PessoaJuridica.

    Define os métodos essenciais para persistir e recuperar os dados da entidade
    PessoaJuridica e gerenciar seus administradores, atividades econômicas,
    endereços e redes sociais.
    """

    @abstractmethod
    def get_by_id(self, pessoa_juridica_id: int) -> Optional[PessoaJuridicaDomain]:
        """
        Recupera uma pessoa jurídica pelo ID.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica a ser recuperada.

        Returns:
            Optional[PessoaJuridicaDomain]: A entidade de domínio da pessoa jurídica,
            ou None se não encontrada.
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, pessoa_juridica: PessoaJuridicaDomain, user) -> PessoaJuridicaDomain:
        """
        Salva ou atualiza uma pessoa jurídica no repositório.

        Args:
            pessoa_juridica (PessoaJuridicaDomain): A entidade de domínio a ser salva.

        Returns:
            PessoaJuridicaDomain: A entidade de domínio salva ou atualizada.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, pessoa_juridica_id: int, user) -> None:
        """
        Exclui uma pessoa jurídica do repositório pelo ID.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica a ser excluída.
        """
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[PessoaJuridicaDomain]:
        """
        Retorna uma lista de todas as pessoas jurídicas cadastradas.

        Returns:
            List[PessoaJuridicaDomain]: Lista de todas as entidades de domínio PessoaJuridica.
        """
        raise NotImplementedError

    @abstractmethod
    def adicionar_administrador(self, pessoa_juridica_id: int, administrador_id: int) -> None:
        """
        Adiciona um administrador a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            administrador_id (int): O ID do administrador a ser adicionado.
        """
        raise NotImplementedError

    @abstractmethod
    def remover_administrador(self, pessoa_juridica_id: int, administrador_id: int) -> None:
        """
        Remove um administrador de uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            administrador_id (int): O ID do administrador a ser removido.
        """
        raise NotImplementedError

    @abstractmethod
    def adicionar_atividade_economica(self, pessoa_juridica_id: int, atividade_id: int) -> None:
        """
        Adiciona uma atividade econômica a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            atividade_id (int): O ID da atividade econômica a ser adicionada.
        """
        raise NotImplementedError

    @abstractmethod
    def remover_atividade_economica(self, pessoa_juridica_id: int, atividade_id: int) -> None:
        """
        Remove uma atividade econômica de uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            atividade_id (int): O ID da atividade econômica a ser removida.
        """
        raise NotImplementedError

    @abstractmethod
    def adicionar_rede_social(self, pessoa_juridica_id: int, rede_social_id: int) -> None:
        """
        Adiciona uma rede social a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            rede_social_id (int): O ID da rede social a ser adicionada.
        """
        raise NotImplementedError

    @abstractmethod
    def remover_rede_social(self, pessoa_juridica_id: int, rede_social_id: int) -> None:
        """
        Remove uma rede social de uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            rede_social_id (int): O ID da rede social a ser removida.
        """
        raise NotImplementedError
