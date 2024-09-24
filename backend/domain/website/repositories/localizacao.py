from abc import ABC, abstractmethod
from typing import Optional
from domain.website.entities.localizacao import Localizacao

class LocalizacaoRepositoryInterface(ABC):
    """
    Interface de repositório para Localizacao.
    Define as operações que qualquer implementação concreta deve fornecer.
    """

    @abstractmethod
    def save(self, localizacao: Localizacao) -> Localizacao:
        """Persiste uma localização no banco de dados."""
        pass

    @abstractmethod
    def find_by_ip(self, ip_address: str) -> Optional[Localizacao]:
        """Retorna a localização associada a um endereço IP."""
        pass
