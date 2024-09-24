"""Módulo implementa o objeto de valor reacao_tipo"""

from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class ReacaoTipoDomain:
    """
    Classe de domínio que representa um tipo de reação que pode ser associada a posts ou comentários.

    Atributos:
        id (int): O identificador único do tipo de reação.
        nome (str): O nome da reação (ex: 'curtida', 'amor', 'raiva').
        descricao (Optional[str]): Uma breve descrição da reação.
        icone (Optional[str]): O ícone associado à reação, pode ser o nome de uma classe de ícone ou o caminho para o arquivo.
    """
    repositorio_tipo_id: int
    nome: str
    descricao: Optional[str] = None
    icone: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.nome}"
