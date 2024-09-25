""" Módulo implementa a entidade tipo de produto"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class TipoProdutoDomain:
    """
    Entidade de domínio para Tipo de Produto.
    """
    tipo_produto_id: Optional[int] = None
    nome: str = ''
    descricao: Optional[str] = None

