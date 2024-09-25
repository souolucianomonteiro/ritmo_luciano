from abc import ABC, abstractmethod
from typing import List, Optional
from domain.website.entities.endereco import EnderecoDomain


class EnderecoRepository(ABC):
    """
    Repositório abstrato para a entidade EnderecoDomain.

    Define os métodos que as implementações concretas devem fornecer para a
    manipulação de endereços no sistema.
    """

    @abstractmethod
    def save(self, endereco: EnderecoDomain) -> EnderecoDomain:
        """
        Salva ou atualiza um endereço no banco de dados.

        Args:
            endereco (EnderecoDomain): Instância do domínio que será salva ou atualizada.

        Returns:
            EnderecoDomain: Instância do domínio salva ou atualizada.
        """
        pass

    @abstractmethod
    def find_by_id(self, endereco_id: int) -> Optional[EnderecoDomain]:
        """
        Busca um endereço pelo ID.

        Args:
            endereco_id (int): Identificador único do endereço.

        Returns:
            Optional[EnderecoDomain]: Instância do domínio se encontrada, caso contrário None.
        """
        pass

    @abstractmethod
    def find_all(self) -> List[EnderecoDomain]:
        """
        Retorna todos os endereços cadastrados no sistema.

        Returns:
            List[EnderecoDomain]: Lista contendo todas as instâncias de endereços.
        """
        pass

    @abstractmethod
    def delete(self, endereco_id: int) -> None:
        """
        Remove um endereço pelo ID.

        Args:
            endereco_id (int): Identificador único do endereço que será removido.
        """
        pass
