
from abc import ABC, abstractmethod
from typing import List, Optional
from domain.website.entities.pessoa_fisica_tipo import PessoaFisicaTipoDomain


class PessoaFisicaTipoRepository(ABC):
    """
    Interface para o repositório de PessoaFisicaTipo no domínio.
    Define os métodos que devem ser implementados pelos repositórios concretos.
    """

    @abstractmethod
    def find_by_id(self, pessoa_fisica_tipo_id: int) -> Optional[PessoaFisicaTipoDomain]:
        """Busca uma instância de PessoaFisicaTipo pelo ID."""
        pass

    @abstractmethod
    def save(self, pessoa_fisica_tipo: PessoaFisicaTipoDomain) -> PessoaFisicaTipoDomain:
        """Salva uma instância de PessoaFisicaTipo."""
        pass

    @abstractmethod
    def delete(self, pessoa_fisica_tipo_id: int) -> None:
        """Deleta uma instância de PessoaFisicaTipo pelo ID."""
        pass

    @abstractmethod
    def find_all(self) -> List[PessoaFisicaTipoDomain]:
        """Retorna todas as instâncias de PessoaFisicaTipo."""
        pass

