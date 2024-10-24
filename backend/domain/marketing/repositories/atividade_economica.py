"""
Módulo responsável pela definição do contrato de repositório para a entidade
AtividadeEconomicaDomain.

Este contrato define as operações básicas que devem ser implementadas para
interagir com a entidade AtividadeEconomicaDomain no repositório, seguindo o
padrão de Domain-Driven Design (DDD).

Classes:
    AtividadeEconomicaContract: Interface abstrata de repositório para a
    entidade AtividadeEconomicaDomain.
"""
from abc import ABC, abstractmethod
from typing import List
from domain.marketing.entities.atividade_economica import (
                                    AtividadeEconomicaDomain)


class AtividadeEconomicaContract(ABC):
    """
    Contrato abstrato de repositório para a entidade AtividadeEconomicaDomain.

    Esta classe abstrata define os métodos que devem ser implementados pelos
    repositórios concretos para manipular dados relacionados à entidade de
    Atividade Econômica. As operações incluem criação, leitura, atualização e
    exclusão (CRUD) de registros no banco de dados.

    Métodos:
        get_by_id: Retorna uma atividade econômica pelo ID.
        list_all: Retorna todas as atividades econômicas cadastradas.
        save: Salva ou atualiza uma atividade econômica.
        delete: Remove uma atividade econômica do repositório pelo ID.
    """

    @abstractmethod
    def get_by_id(self, atividade_econ_id: int,) -> AtividadeEconomicaDomain:
        """
        Recupera uma entidade AtividadeEconomicaDomain pelo seu ID.

        Args:
            atividade_econ_id (int): O identificador único da atividade econômica.

        Returns:
            AtividadeEconomicaDomain: A entidade de atividade econômica associada
            ao ID fornecido.

        Raises:
            EntityNotFoundException: Se a atividade econômica com o ID fornecido
            não for encontrada no repositório.
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[AtividadeEconomicaDomain]:
        """
        Retorna uma lista com todas as entidades de AtividadeEconomicaDomain.

        Returns:
            List[AtividadeEconomicaDomain]: Lista de todas as atividades econômicas
            cadastradas no repositório.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao listar as
            atividades econômicas.
        """
        pass

    @abstractmethod
    def save(self, atividade_economica: AtividadeEconomicaDomain, user) -> None:
        """
        Salva ou atualiza uma entidade de AtividadeEconomicaDomain.

        Args:
            atividade_economica (AtividadeEconomicaDomain): A entidade de atividade
            econômica a ser salva ou atualizada no repositório.

        Returns:
            None

        Raises:
            ValidationException: Se os dados da entidade não forem válidos.
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        pass

    @abstractmethod
    def delete(self, atividade_econ_id: int, user) -> None:
        """
        Remove uma entidade AtividadeEconomicaDomain do repositório pelo ID.

        Args:
            atividade_econ_id (int): O identificador único da atividade econômica
            a ser removida.

        Returns:
            None

        Raises:
            EntityNotFoundException: Se a atividade econômica com o ID fornecido
            não for encontrada no repositório.
            OperationFailedException: Se ocorrer um erro inesperado ao remover
            a entidade.
        """
        pass
