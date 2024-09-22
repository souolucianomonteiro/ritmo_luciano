from dataclasses import dataclass

@dataclass(frozen=True)
class TagPost:
    """
    Representa uma Tag associada a um Post no domínio do Blog.
    A classe é um Objeto de Valor, pois não possui identidade própria,
    e sua comparação é baseada nos atributos.
    """
    nome: str
    blog: str
