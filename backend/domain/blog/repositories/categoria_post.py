from abc import ABC, abstractmethod
from typing import List
from domain.blog.value_objects.categoria_post import CategoriaPostDomain


class CategoriaPostRepository(ABC):
    """
    Repositório abstrato para operações de CategoriaPost.

    Define os métodos que devem ser implementados para manipular 
    categorias de postagens.
    """

    @abstractmethod
    def save(self, categoria: CategoriaPostDomain) -> CategoriaPostDomain:
        pass

    @abstractmethod
    def get_by_id(self, categoria_id: int) -> CategoriaPostDomain:
        pass

    @abstractmethod
    def list_all(self) -> List[CategoriaPostDomain]:
        pass

    @abstractmethod
    def delete(self, categoria: CategoriaPostDomain) -> None:
        pass
