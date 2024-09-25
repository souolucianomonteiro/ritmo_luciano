from abc import ABC, abstractmethod
from typing import Optional, List
from domain.website.entities.pessoa_juridica import PessoaJuridicaDomain
from domain.website.entities.endereco import EnderecoDomain


class PessoaJuridicaRepository(ABC):
    """
    Repositório abstrato para a entidade PessoaJuridica.

    Define os métodos para persistir e recuperar os dados da entidade
    PessoaJuridica e seus endereços.
    """

    @abstractmethod
    def save(self, pessoa_juridica: PessoaJuridicaDomain) -> PessoaJuridicaDomain:
        """
        Salva ou atualiza uma instância de PessoaJuridica no repositório.
        Deve lidar também com os endereços associados.
        """
        pass

    @abstractmethod
    def get_by_id(self, pessoa_juridica_id: int) -> Optional[PessoaJuridicaDomain]:
        """
        Recupera uma instância de PessoaJuridica por seu ID, incluindo os endereços associados.
        """
        pass

    @abstractmethod
    def delete(self, pessoa_juridica: PessoaJuridicaDomain) -> None:
        """
        Exclui uma instância de PessoaJuridica do repositório.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[PessoaJuridicaDomain]:
        """
        Lista todas as instâncias de PessoaJuridica no repositório, incluindo seus endereços.
        """
        pass

    @abstractmethod
    def add_endereco(self, pessoa_juridica_id: int, endereco: EnderecoDomain) -> None:
        """
        Adiciona um endereço a uma pessoa jurídica existente.
        """
        pass

    @abstractmethod
    def remove_endereco(self, pessoa_juridica_id: int, endereco_id: int) -> None:
        """
        Remove um endereço de uma pessoa jurídica.
        """
        pass
