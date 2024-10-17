# pylint: disable=no-member:

from typing import List, Optional
from domain.blog.repositories.blog import BlogRepository
from domain.blog.entities.blog import BlogDomain
from infrastructure.models.blog import Blog 
from infrastructure.models.blog.categoria_post import CategoriaPost
from infrastructure.models.blog.tag_post import TagPost


class DjangoBlogRepository(BlogRepository):
    """
    Repositório concreto para a entidade Blog.

    Implementa os métodos definidos no repositório abstrato, utilizando o Django ORM.
    """

    def save(self, blog: BlogDomain) -> BlogDomain:
        blog_model, created = Blog.objects.update_or_create(
            id=blog.id,
            defaults={
                'title': blog.title,
                'description': blog.description,
                'proprietario_id': blog.proprietario.id,
                'site_id': blog.site.id,
            }
        )

        # Atualizando categorias e tags
        if blog.categorias:
            categoria_models = [CategoriaPost.objects.get(id=categoria.id) for categoria in blog.categorias]
            blog_model.categorias.set(categoria_models)

        if blog.tags:
            tag_models = [TagPost.objects.get(id=tag.id) for tag in blog.tags]
            blog_model.tags.set(tag_models)

        blog.id = blog_model.id
        return blog

    def get_by_id(self, blog_id: int) -> Optional[BlogDomain]:
        try:
            blog_model = Blog.objects.get(id=blog_id)

            categorias = [
                CategoriaPost(id=categoria.id, nome=categoria.nome, descricao=categoria.descricao)
                for categoria in blog_model.categorias.all()
            ]

            tags = [
                Tag(id=tag.id, nome=tag.nome)
                for tag in blog_model.tags.all()
            ]

            return BlogDomain(
                id=blog_model.id,
                title=blog_model.title,
                description=blog_model.description,
                proprietario=blog_model.proprietario,
                site=blog_model.site,
                categorias=categorias,
                tags=tags
            )
        except Blog.DoesNotExist:
            return None

    def delete(self, blog: BlogDomain) -> None:
        Blog.objects.filter(id=blog.id).delete()

    def list_all(self) -> List[BlogDomain]:
        blogs = Blog.objects.all()
        return [
            BlogDomain(
                id=blog.id,
                title=blog.title,
                description=blog.description,
                proprietario=blog.proprietario,
                site=blog.site,
                categorias=[
                    CategoriaPost(id=categoria.id, nome=categoria.nome, descricao=categoria.descricao)
                    for categoria in blog.categorias.all()
                ],
                tags=[
                    TagPost(id=tag.id, nome=tag.nome)
                    for tag in blog.tags.all()
                ]
            )
            for blog in blogs
        ]
