# pylint: disable=no-member

from typing import List, Optional
from domain.blog.value_objects.tag_post import TagPostDomain
from domain.blog.repositories.tag_post import TagPostRepository
from infrastructure.models.tag_post import TagPost


class DjangoTagPostRepository(TagPostRepository):
    """
    Repositório concreto para a entidade TagPost.
    Implementa os métodos definidos no repositório abstrato, utilizando o Django ORM.
    """

    def list_all(self) -> List[TagPostDomain]:
        tags = TagPost.objects.all()
        return [self._to_domain(tag) for tag in tags]

    def get_by_name(self, name: str) -> Optional[TagPostDomain]:
        try:
            tag = TagPost.objects.get(name=name)
            return self._to_domain(tag)
        except TagPost.DoesNotExist:
            return None

    def save(self, tag_post: TagPostDomain) -> TagPostDomain:
        tag_model, created = TagPost.objects.get_or_create(
            name=tag_post.name,
            defaults={'descricao': tag_post.descricao}
        )
        if not created:
            tag_model.descricao = tag_post.descricao
            tag_model.save()
        return self._to_domain(tag_model)

    def delete(self, name: str) -> None:
        TagPost.objects.filter(name=name).delete()

    def _to_domain(self, tag_model: TagPost) -> TagPostDomain:
        """
        Converte um modelo TagPost em um objeto de valor TagPostDomain.
        """
        return TagPostDomain(
            name=tag_model.name,
            descricao=tag_model.descricao
        )
