# shared/plugins/repositories/categoria_repository_django.py
# pylint: disable=no-member

from typing import List, Optional
from domain.shared.plugins.entities.categoria import Categoria
from domain.shared.plugins.repositories.categoria import CategoriaRepository
from infrastructure.models.categoria import CategoriaModel


class CategoriaRepositoryDjango(CategoriaRepository):
    """
    Implementação concreta do repositório de categorias
    usando o Django ORM.

    Este repositório é responsável pela interação com o
    banco de dados para a persistência de dados de
    categorias.
    """

    def obter_todas(self) -> List[Categoria]:
        """
        Retorna uma lista com todas as categorias usando o
        Django ORM.

        :return: Lista de instâncias de Categoria.
        """
        categorias = CategoriaModel.objects.all()
        return [Categoria(cat.nome) for cat in categorias]

    def salvar(self, categoria: Categoria) -> None:
        """
        Salva ou atualiza uma categoria no banco de dados.

        :param categoria: A categoria a ser salva ou atualizada.
        """
        CategoriaModel.objects.update_or_create(
            nome=categoria.nome
        )

    def remover(self, categoria: Categoria) -> None:
        """
        Remove uma categoria do banco de dados.

        :param categoria: A categoria a ser removida.
        """
        CategoriaModel.objects.filter(nome=categoria.nome).delete()

    def obter_por_nome(self, nome: str) -> Optional[Categoria]:
        """
        Retorna uma categoria com base no nome usando o
        Django ORM.

        :param nome: Nome da categoria a ser buscada.
        :return: Objeto Categoria correspondente ou None.
        """
        try:
            categoria_model = CategoriaModel.objects.get(nome=nome)
            return Categoria(categoria_model.nome)
        except CategoriaModel.DoesNotExist:
            return None
