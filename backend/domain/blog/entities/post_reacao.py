from dataclasses import dataclass
from datetime import datetime
from typing import Optional
from domain.blog.repositories.reacao_tipo import ReacaoTipoRepository
from domain.website.repositories.localizacao import Localizacao

@dataclass
class PostReacao:
    post: Post
    reacao_tipo: ReacaoTipoRepository
    localizacao: Optional[Localizacao] = None
    ip_origem: Optional[str] = None
    data_reacao: datetime = datetime.now()

    def __str__(self):
        return f"Reação {self.reacao_tipo.nome} no post '{self.post.titulo}'"
