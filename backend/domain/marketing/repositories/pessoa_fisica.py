"""
Módulo responsável pela definição do repositório abstrato de PessoaFisica.

Este módulo contém a interface abstrata PessoaFisicaRepository, que define
as operações essenciais para persistência e recuperação de dados da entidade
PessoaFisica. As implementações concretas devem herdar essa interface e
fornecer a lógica específica para a interação com o banco de dados.
"""
from abc import ABC, abstractmethod
from typing import Optional, List
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain
from infrastructure.repositories.marketing.endereco import EnderecoRepository


class PessoaFisicaContract(ABC):
    """
    Repositório abstrato para a entidade PessoaFisica.

    Define os métodos para persistir e recuperar os dados da entidade
    PessoaFisica e seus endereços.
    """

    @abstractmethod
    def get_by_id(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        """Recupera uma pessoa física pelo ID."""
        raise NotImplementedError
    
    @abstractmethod
    def save(self, pessoa: PessoaFisicaDomain, user) -> PessoaFisicaDomain:
        """Salva ou atualiza uma pessoa física no repositório."""
        raise NotImplementedError
    
    @abstractmethod
    def delete(self, pessoa_fisica_id: int, user) -> None:
        """Exclui uma pessoa física do repositório pelo ID."""
        raise NotImplementedError
    
    @abstractmethod
    def list_all(self) -> List[PessoaFisicaDomain]:
        """Retorna uma lista de todas as pessoas físicas cadastradas."""
        raise NotImplementedError

    @abstractmethod
    def alterar_status(self, pessoa_fisica_id: int, status: str) -> None:
        """Altera o status da pessoa física."""
        raise NotImplementedError
    
    @abstractmethod
    def adicionar_endereco(self, pessoa_fisica_id: int, endereco: EnderecoRepository) -> None:
        """Adiciona um novo endereço à pessoa física."""
        raise NotImplementedError
    
    @abstractmethod
    def remover_endereco(self, pessoa_fisica_id: int, endereco_id: int) -> None:
        """Remove um endereço da pessoa física usando soft delete."""
        raise NotImplementedError

    @abstractmethod
    def atualizar_situacao_projeto(self, pessoa_fisica_id: int) -> None:
        """
        Atualiza a situação de projeto da pessoa física com base em sua participação
        em projetos (ativo ou sem projeto).
        """
        raise NotImplementedError

    @abstractmethod
    def associar_usuario_rede_social(self, pessoa_fisica_id: int, rede_social_id: int, usuario: str) -> None:
        """Associa um nome de usuário a uma rede social específica para uma pessoa física."""
        raise NotImplementedError

    @abstractmethod
    def remover_usuario_rede_social(self, pessoa_fisica_id: int, rede_social_id: int) -> None:
        """Remove a associação de um nome de usuário de uma rede social."""
        raise NotImplementedError
