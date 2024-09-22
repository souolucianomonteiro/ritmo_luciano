from dataclasses import dataclass

@dataclass(frozen=True)
class CategoriaPostDomain:
    """
    Classe que representa o objeto de valor CategoriaPost no domínio.

    Atributos:
        nome (str): O nome da categoria.
        descricao (str): A descrição da categoria.
    """
    nome: str
    descricao: str
