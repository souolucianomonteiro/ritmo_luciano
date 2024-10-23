"""Repositório abstrato para o gerenciamento de Tipo de Produto no domínio."""
from abc import ABC, abstractmethod
from typing import Optional, List
from domain.marketing.entities.produto_tipo import TipoProdutoDomain


class TipoProdutoContract(ABC):
    """
    Interface abstrata que define os métodos essenciais para o repositório
    de TipoProduto.

    Métodos:
        get_by_id: Recupera um tipo de produto pelo ID.
        save: Salva ou atualiza um tipo de produto.
        delete: Exclui um tipo de produto pelo ID.
        list_all: Lista todos os tipos de produtos.
    """

    @abstractmethod
    def get_by_id(self, tipo_produto_id: int) -> Optional[TipoProdutoDomain]:
        """
        Recupera um tipo de produto pelo seu identificador único.

        Args:
            tipo_produto_id (int): O identificador único do tipo de produto.

        Returns:
            Optional[TipoProdutoDomain]: O tipo de produto, ou None se não encontrado.
        """
        raise NotImplementedError

    @abstractmethod
    def save(self, tipo_produto: TipoProdutoDomain) -> TipoProdutoDomain:
        """
        Salva ou atualiza um tipo de produto.

        Args:
            tipo_produto (TipoProdutoDomain): O tipo de produto a ser salvo.

        Returns:
            TipoProdutoDomain: O tipo de produto salvo ou atualizado.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, tipo_produto_id: int) -> None:
        """
        Exclui um tipo de produto pelo seu identificador único.

        Args:
            tipo_produto_id (int): O identificador único do tipo de produto.
        """
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[TipoProdutoDomain]:
        """
        Retorna uma lista de todos os tipos de produtos cadastrados.

        Returns:
            List[TipoProdutoDomain]: A lista de tipos de produtos.
        """
        raise NotImplementedError
