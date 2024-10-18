"""
Módulo responsável pela definição do contrato de repositório para a entidade
EnderecoDomain.

Este contrato define as operações básicas que devem ser implementadas para
interagir com a entidade EnderecoDomain no repositório, seguindo o padrão de
Domain-Driven Design (DDD). Ele especifica as operações de persistência e
consulta associadas a endereços.

Classes:
    EnderecoContract: Interface abstrata de repositório para a entidade 
    EnderecoDomain.
"""
from abc import ABC, abstractmethod
from typing import List
from domain.marketing.entities.endereco import EnderecoDomain


class EnderecoContract(ABC):
    """
    Contrato abstrato de repositório para a entidade EnderecoDomain.

    Esta classe abstrata define os métodos que devem ser implementados pelos
    repositórios concretos para manipular dados relacionados à entidade de
    Endereço. As operações incluem criação, leitura, atualização e exclusão (CRUD)
    de registros no banco de dados, bem como outras operações relacionadas à
    persistência de endereços.
    """

    @abstractmethod
    def get_by_id(self, endereco_id: int) -> EnderecoDomain:
        """
        Recupera um endereço pelo seu ID.

        Args:
            endereco_id (int): O identificador único do endereço.

        Returns:
            EnderecoDomain: A entidade de endereço correspondente ao ID fornecido.

        Raises:
            EntityNotFoundException: Se o endereço com o ID fornecido não for
            encontrado no repositório.
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[EnderecoDomain]:
        """
        Retorna uma lista com todos os endereços cadastrados.

        Returns:
            List[EnderecoDomain]: Lista de todas as entidades de EnderecoDomain
            cadastradas no repositório.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao listar os
            endereços.
        """
        pass

    @abstractmethod
    def save(self, endereco: EnderecoDomain) -> None:
        """
        Salva ou atualiza um endereço no repositório.

        Args:
            endereco (EnderecoDomain): A entidade de endereço a ser salva ou
            atualizada no repositório.

        Returns:
            None

        Raises:
            ValidationException: Se os dados do endereço não forem válidos.
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        pass

    @abstractmethod
    def delete(self, endereco_id: int) -> None:
        """
        Remove um endereço do repositório pelo ID.

        Args:
            endereco_id (int): O identificador único do endereço a ser removido.

        Returns:
            None

        Raises:
            EntityNotFoundException: Se o endereço com o ID fornecido não for
            encontrado no repositório.
            OperationFailedException: Se ocorrer um erro inesperado ao remover
            o endereço.
        """
        pass

    @abstractmethod
    def list_by_pessoa_fisica(self, pessoa_fisica_id: int) -> List[EnderecoDomain]:
        """
        Retorna uma lista de endereços associados a uma pessoa física.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.

        Returns:
            List[EnderecoDomain]: Lista de endereços associados à pessoa física.

        Raises:
            EntityNotFoundException: Se não forem encontrados endereços
            associados à pessoa física.
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        pass

    @abstractmethod
    def list_by_pessoa_juridica(self, pessoa_juridica_id: int) -> List[EnderecoDomain]:
        """
        Retorna uma lista de endereços associados a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O identificador único da pessoa jurídica.

        Returns:
            List[EnderecoDomain]: Lista de endereços associados à pessoa jurídica.

        Raises:
            EntityNotFoundException: Se não forem encontrados endereços
            associados à pessoa jurídica.
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        pass
