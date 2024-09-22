
from domain.blog.value_objects.tag_post import TagPost
from infrastructure.models.tag_post import TagPost
from domain.blog.entities.blog import BlogDomain
from infrastructure.models.blog import BlogModel

class DjangoTagPostRepository:
    """
    Repositório concreto para a entidade TagPost.
    Implementa os métodos definidos no repositório abstrato, utilizando o Django ORM.
    """

    def save(self, tag_post: TagPostDomain) -> TagPostDomain:
        blog_model = BlogModel.objects.get(id=tag_post.blog.id)
        
        tag_post_model = TagPostModel(
            id=tag_post.id,
            nome=tag_post.nome,
            descricao=tag_post.descricao,
            blog=blog_model  # Vinculando ao blog
        )
        tag_post_model.save()
        
        tag_post.id = tag_post_model.id
        return tag_post

    def get_by_id(self, tag_post_id: int) -> Optional[TagPostDomain]:
        try:
            tag_post_model = TagPostModel.objects.get(id=tag_post_id)
            blog_domain = BlogDomain(
                id=tag_post_model.blog.id,
                titulo=tag_post_model.blog.titulo,
                descricao=tag_post_model.blog.descricao,
                # Outros atributos do blog
            )

            return TagPostDomain(
                id=tag_post_model.id,
                nome=tag_post_model.nome,
                descricao=tag_post_model.descricao,
                blog=blog_domain
            )
        except TagPostModel.DoesNotExist:
            return None
