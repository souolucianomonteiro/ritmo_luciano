"""Módulo implementa a entidade Blog"""

from typing import Optional, List
from dataclasses import dataclass
from domain.blog.repositories.categoria_post import CategoriaPostRepository
from domain.blog.repositories.tag_post import TagPostRepository
from domain.website.repositories.pessoa_fisica import PessoaFisicaRepository

@dataclass
class BlogDomain:
    """
    Classe de domínio que representa um blog no sistema.

    Atributos:
        id (Optional[int]): Identificador único do blog.
        title (str): Título do blog.
        description (Optional[str]): Descrição do blog.
        proprietario (PessoaFisicaRepository): O proprietário do blog.
        site (str): O site ao qual o blog pertence.
        categorias (List[CategoriaPostRepository]): Lista de categorias associadas ao blog.
        tags (List[TagPostRepository]): Lista de tags associadas ao blog.
    """
    id: Optional[int]
    title: str
    description: Optional[str]
    proprietario: PessoaFisicaRepository
    site: str
    categorias: List[CategoriaPostRepository]
    tags: List[TagPostRepository]
