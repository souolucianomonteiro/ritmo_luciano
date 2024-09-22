from typing import List, Optional
from domain.blog.entities.blog import BlogDomain


class BlogRepository:
    def save(self, blog: BlogDomain) -> BlogDomain:
        raise NotImplementedError

    def get_by_id(self, blog_id: int) -> Optional[BlogDomain]:
        raise NotImplementedError

    def delete(self, blog: BlogDomain) -> None:
        raise NotImplementedError

    def list_all(self) -> List[BlogDomain]:
        raise NotImplementedError
