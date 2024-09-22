from abc import ABC, abstractmethod
from typing import List, Optional
from domain.blog.value_objects.tag_post import TagPostDomain


class TagPostRepository(ABC):
    """
    Interface de repositório para manipulação de tags associadas a posts ou blogs.
    """

    @abstractmethod
    def list_all(self) -> List[TagPostDomain]:
        pass

    @abstractmethod
    def get_by_name(self, name: str) -> Optional[TagPostDomain]:
        pass

    @abstractmethod
    def save(self, tag_post: TagPostDomain) -> TagPostDomain:
        pass

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
