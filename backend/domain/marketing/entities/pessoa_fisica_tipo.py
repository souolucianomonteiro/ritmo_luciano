from dataclasses import dataclass
from typing import Optional

@dataclass
class PessoaFisicaTipoDomain:
    """
    Classe de domínio que representa a relação entre Pessoa Física e seu Tipo de Usuário.

    Atributos:
        pessoa_fisica_tipo_id (Optional[int]): Identificador único da relação.
        pessoa_fisica_id (int): O ID da pessoa física associada.
        usuario_tipo_id (int): O ID do tipo de usuário associado.
    """

    pessoa_fisica_tipo_id: Optional[int] = None  # ID da relação
    pessoa_fisica_id: int  # ID da PessoaFisica
    usuario_tipo_id: int  # ID do UsuarioTipo

    def __str__(self):
        return f"PessoaFisicaTipo(pessoa_fisica_tipo_id={self.pessoa_fisica_tipo_id}, pessoa_fisica_id={self.pessoa_fisica_id}, usuario_tipo_id={self.usuario_tipo_id})"
