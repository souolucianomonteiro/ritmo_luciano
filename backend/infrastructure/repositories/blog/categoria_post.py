# pylint: disable=no-member

from typing import List, Optional
from domain.blog.repositories.categoria_post import CategoriaPostRepository
from domain.blog.value_objects.categoria_post import CategoriaPostDomain
from infrastructure.models.blog.categoria_post import CategoriaPost


class DjangoCategoriaPostRepository(CategoriaPostRepository):
    """
    Repositório concreto para o objeto de valor CategoriaPost.

    Implementa os métodos definidos no repositório abstrato, utilizando o Django ORM.
    """

    def save(self, categoria: CategoriaPostDomain) -> CategoriaPostDomain:
        """
        Salva ou atualiza uma categoria no banco de dados.

        Args:
            categoria (CategoriaPostDomain): Objeto de valor representando a categoria.

        Returns:
            CategoriaPostDomain: A categoria salva.
        """
        categoria_model, created = CategoriaPost.objects.get_or_create(
            nome=categoria.nome,
            defaults={'descricao': categoria.descricao}
        )
        if not created:
            categoria_model.descricao = categoria.descricao
            categoria_model.save()

        return CategoriaPostDomain(nome=categoria_model.nome, descricao=categoria_model.descricao)

    def get_by_id(self, categoria_id: int) -> Optional[CategoriaPostDomain]:
        """
        Busca uma categoria pelo seu ID.

        Args:
            categoria_id (int): O ID da categoria.

        Returns:
            Optional[CategoriaPostDomain]: A categoria encontrada, ou None se não existir.
        """
        try:
            categoria_model = CategoriaPost.objects.get(id=categoria_id)
            return CategoriaPostDomain(nome=categoria_model.nome, descricao=categoria_model.descricao)
        except CategoriaPost.DoesNotExist:
            return None

    def list_all(self) -> List[CategoriaPostDomain]:
        """
        Retorna todas as categorias do banco de dados.

        Returns:
            List[CategoriaPostDomain]: Lista de todas as categorias.
        """
        categorias = CategoriaPost.objects.all()
        return [CategoriaPostDomain(nome=categoria.nome, descricao=categoria.descricao) for categoria in categorias]

    def delete(self, categoria: CategoriaPostDomain) -> None:
        """
        Exclui uma categoria do banco de dados.

        Args:
            categoria (CategoriaPostDomain): A categoria a ser excluída.
        """
        CategoriaPost.objects.filter(nome=categoria.nome, descricao=categoria.descricao).delete()
