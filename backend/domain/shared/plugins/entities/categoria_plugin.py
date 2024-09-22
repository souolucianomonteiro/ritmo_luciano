# shared/plugins/value_objects/categoria.py

from dataclasses import dataclass
from typing import Optional

@dataclass
class CategoriaPluginDomain:
    """
    Classe de domínio que representa uma categoria de plugin.

    Atributos:
        id (Optional[int]): Identificador único da categoria.
        nome (str): Nome da categoria.
    """
    id: Optional[int]
    nome: str
