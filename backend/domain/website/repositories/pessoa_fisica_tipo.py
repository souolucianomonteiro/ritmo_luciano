
from abc import ABC, abstractmethod
from typing import List
from domain.website.entities.pessoa_fisica import PessoaFisicaDomain
from domain.website.entities.usuario_tipo import UsuarioTipoDomain


class PessoaFisicaTipoRepository(ABC):
    """
    Repositório abstrato para a associação entre PessoaFisica e UsuarioTipo.
    """

    @abstractmethod
    def save(self, pessoa_fisica_tipo: PessoaFisicaDomain) -> PessoaFisicaDomain:
        """
        Salva a associação entre pessoa física e tipo de usuário no repositório.
        """
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, pessoa_fisica_tipo_id: int) -> PessoaFisicaDomain:
        """
        Busca uma associação entre pessoa física e tipo de usuário pelo ID.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, pessoa_fisica_tipo: PessoaFisicaDomain) -> None:
        """
        Exclui uma associação entre pessoa física e tipo de usuário do repositório.
        """
        raise NotImplementedError

    @abstractmethod
    def list_all(self) -> List[PessoaFisicaDomain]:
        """
        Lista todas as associações entre pessoas físicas e tipos de usuário.
        """
        raise NotImplementedError

    @abstractmethod
    def associate_usuario_tipo(self, pessoa_fisica: PessoaFisicaDomain, usuario_tipos: List[UsuarioTipoDomain]) -> None:
        """
        Associa uma lista de tipos de usuário à pessoa física.
        """
        raise NotImplementedError
