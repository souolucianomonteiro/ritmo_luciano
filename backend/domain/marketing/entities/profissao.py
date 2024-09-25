from dataclasses import dataclass
from typing import Optional

@dataclass
class Profissao:
    """
    Classe de domínio que representa uma profissão no sistema.

    Atributos:
        codigo (str): Código único da profissão.
        descricao (str): Descrição da profissão.
    """
    id: Optional[int]
    codigo: str
    descricao: str
