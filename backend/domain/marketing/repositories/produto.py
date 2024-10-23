"""Implementa o contrato do repositório produto """

from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID
from domain.marketing.entities.produto import ProdutoDomain


class ProdutoContract(ABC):
    """
    Contrato de repositório para a entidade Produto.

    Define as operações essenciais para manipulação da entidade Produto.
    """

    @abstractmethod
    def get_by_id(self, produto_id: UUID) -> Optional[ProdutoDomain]:
        """
        Recupera um produto pelo seu ID.

        Args:
            produto_id (UUID): O ID do produto.

        Returns:
            Optional[ProdutoDomain]: O produto recuperado ou None se não encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, produto: ProdutoDomain) -> ProdutoDomain:
        """
        Salva ou atualiza um produto no repositório.

        Args:
            produto (ProdutoDomain): A entidade de domínio a ser salva.

        Returns:
            ProdutoDomain: A entidade de domínio salva ou atualizada.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, produto_id: UUID) -> None:
        """
        Exclui um produto pelo ID.

        Args:
            produto_id (UUID): O ID do produto a ser excluído.
        """
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[ProdutoDomain]:
        """
        Lista todos os produtos do repositório.

        Returns:
            List[ProdutoDomain]: Lista de todas as entidades de domínio Produto.
        """
        raise NotImplementedError
