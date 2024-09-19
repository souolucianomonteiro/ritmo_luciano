"""
Módulo responsável pela definição do repositório abstrato de PessoaFisica.

Este módulo contém a interface abstrata PessoaFisicaRepository, que define
as operações essenciais para persistência e recuperação de dados da entidade
PessoaFisica. As implementações concretas devem herdar essa interface e
fornecer a lógica específica para a interação com o banco de dados.
"""
from abc import ABC, abstractmethod
from typing import Optional, List
from domain.website.entities.pessoa_fisica import PessoaFisicaDomain
from domain.website.entities.endereco import EnderecoDomain


class PessoaFisicaRepository(ABC):
    """
    Repositório abstrato para a entidade PessoaFisica.

    Define os métodos para persistir e recuperar os dados da entidade
    PessoaFisica e seus endereços.
    """

    @abstractmethod
    def save(self, pessoa_fisica: PessoaFisicaDomain) -> PessoaFisicaDomain:
        """
        Salva ou atualiza uma instância de PessoaFisica no repositório.
        Deve lidar também com os endereços associados.
        """
        pass

    @abstractmethod
    def get_by_id(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        """
        Recupera uma instância de PessoaFisica por seu ID, 
        incluindo os endereços associados.
        """
        pass

    @abstractmethod
    def delete(self, pessoa_fisica: PessoaFisicaDomain) -> None:
        """
        Exclui uma instância de PessoaFisica do repositório.
        """
        pass

    @abstractmethod
    def list_all(self) -> List[PessoaFisicaDomain]:
        """
        Lista todas as instâncias de PessoaFisica no repositório, incluindo
        seus endereços.
        """
        pass

    @abstractmethod
    def add_endereco(self, pessoa_fisica_id: int, endereco: EnderecoDomain) -> None:
        """
        Adiciona um endereço a uma pessoa física existente.
        """
        pass

    @abstractmethod
    def remove_endereco(self, pessoa_fisica_id: int, endereco_id: int) -> None:
        """
        Remove um endereço de uma pessoa física.
        """
        pass


