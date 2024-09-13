# shared/plugins/repositories/categoria_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from domain.shared.plugins.entities.categoria import Categoria


class CategoriaRepository(ABC):
    """
    Interface do repositório para manipulação de categorias
    no domínio.

    Este repositório define os métodos essenciais para
    acessar e manipular dados de categorias.
    """

    @abstractmethod
    def obter_todas(self) -> List[Categoria]:
        """
        Retorna uma lista com todas as categorias.

        :return: Lista de objetos Categoria.
        """
    @abstractmethod
    def salvar(self, categoria: Categoria) -> None:
        """
        Salva ou atualiza uma categoria no repositório.

        :param categoria: A categoria a ser salva ou atualizada.
        """

    @abstractmethod
    def remover(self, categoria: Categoria) -> None:
        """
        Remove uma categoria do repositório.

        :param categoria: A categoria a ser removida.
        """
      
    @abstractmethod
    def obter_por_nome(self, nome: str) -> Optional[Categoria]:
        """
        Retorna uma categoria com base no nome.

        :param nome: Nome da categoria a ser buscada.
        :return: Objeto Categoria correspondente ou None.
        """
