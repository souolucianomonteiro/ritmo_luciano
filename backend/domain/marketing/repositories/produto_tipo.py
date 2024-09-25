"""Repositório abstrato para o gerenciamento de Tipo de Produto no domínio."""
from abc import ABC, abstractmethod
from typing import Optional
from domain.marketing.entities.produto_tipo import ProdutoTipoDomain


class TipoProdutoRepository(ABC):
    """
    Classe que define a interface para as operações essenciais de CRUD
    sobre o objeto de domínio TipoProdutoDomain. Não interage diretamente
    com a infraestrutura ou banco de dados, mantendo o foco na lógica do
    domínio.
    """

    @abstractmethod
    def get_by_id(self, tipo_produto_id: int) -> Optional[ProdutoTipoDomain]:
        """
        Busca um TipoProdutoDomain pelo seu ID.

        Parâmetros:
            tipo_produto_id (int): O ID do tipo de produto a ser buscado.

        Retorna:
            Optional[TipoProdutoDomain]: O objeto de domínio TipoProdutoDomain se encontrado, 
            ou None caso não exista.
        """
        pass

    @abstractmethod
    def get_by_name(self, nome: str) -> Optional[ProdutoTipoDomain]:
        """
        Busca um TipoProdutoDomain pelo seu nome.

        Parâmetros:
            nome (str): O nome do tipo de produto a ser buscado.

        Retorna:
            Optional[TipoProdutoDomain]: O objeto de domínio TipoProdutoDomain
            correspondente ao nome, ou None caso não exista.
        """
        pass

    @abstractmethod
    def save(self, tipo_produto: ProdutoTipoDomain) -> ProdutoTipoDomain:
        """
        Salva ou atualiza um TipoProdutoDomain.

        Parâmetros:
            tipo_produto (TipoProdutoDomain): O objeto de domínio a ser salvo
            ou atualizado.

        Retorna:
            TipoProdutoDomain: O objeto de domínio salvo ou atualizado.
        """
        pass

    @abstractmethod
    def delete(self, tipo_produto_id: int) -> None:
        """
        Remove um TipoProdutoDomain com base no seu ID.

        Parâmetros:
            tipo_produto_id (int): O ID do tipo de produto a ser removido.

        Retorna:
            None
        """
        pass
