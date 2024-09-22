from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class TagPostDomain:
    """
    Objeto de valor que representa uma Tag associada a um Post ou Blog.
    """
    name: str
    descricao: Optional[str] = None

