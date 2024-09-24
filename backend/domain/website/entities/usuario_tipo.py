from dataclasses import dataclass
from typing import Optional

@dataclass
class UsuarioTipoDomain:
    """
    Classe de domínio que representa o tipo de usuário no sistema.

    Atributos:
        id (Optional[int]): Identificador único do tipo de usuário.
        nome (str): O nome do tipo de usuário (ex: Administrador, Editor).
        descricao (Optional[str]): Uma breve descrição do tipo de usuário.
    """
    usuario_tipo_id: Optional[int]
    nome: str
    descricao: Optional[str]
