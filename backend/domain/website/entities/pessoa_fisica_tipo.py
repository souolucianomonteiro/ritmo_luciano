from domain.website.entities.pessoa_fisica import PessoaFisicaDomain
from domain.website.entities.usuario_tipo import UsuarioTipoDomain
from typing import Optional


class PessoaFisicaTipoDomain:
    """
    Classe de domínio que representa a relação entre Pessoa Física e seu Tipo de Usuário.

    Atributos:
        id (Optional[int]): Identificador único da entidade.
        pessoa_fisica (PessoaFisicaDomain): A pessoa física associada.
        usuario_tipo (UsuarioTipoDomain): O tipo de usuário associado.
    """

    def __init__(self,
                 pessoa_fisica: PessoaFisicaDomain,
                 usuario_tipo: UsuarioTipoDomain,
                 id: Optional[int] = None):
        self.id = id
        self.pessoa_fisica = pessoa_fisica
        self.usuario_tipo = usuario_tipo

    def __str__(self):
        return f"{self.pessoa_fisica} - {self.usuario_tipo}"
