"""
Módulo de repositório para a entidade Plugin.

Este módulo define a interface abstrata para o repositório da entidade Plugin,
fornecendo os métodos necessários para interação com os dados persistidos no 
banco de dados ou em outro mecanismo de armazenamento.

A interface do repositório é projetada para fornecer uma abstração que pode ser
implementada de diferentes maneiras, conforme a necessidade da camada de 
infraestrutura.
"""
from abc import ABC, abstractmethod
from uuid import UUID
from typing import List, Optional
from domain.shared.plugins.aggregates.plugin import Plugin


class PluginRepository(ABC):
    """
    Interface abstrata para o repositório de Plugin.

    Esta classe define os métodos essenciais que qualquer implementação
    concreta
    de repositório de Plugin deve fornecer. Esses métodos incluem a
    recuperação,
    listagem, armazenamento e remoção de instâncias de Plugin.

    Métodos:
        obter_por_id(id: int) -> Optional[Plugin]:
                
        listar() -> List[Plugin]:
           
        salvar(plugin: Plugin) -> None:
            
        remover(plugin_id: int) -> None:

        """

    @abstractmethod
    def obter_por_id(self, plugin_id: int) -> Optional[Plugin]:
        """
         Recupera um Plugin pelo seu ID
        """
        pass

    @abstractmethod
    def obter_por_uuid(self, uuid: UUID) -> Optional[Plugin]:
        """Obtém um plugin pelo seu UUID."""
        pass

    @abstractmethod
    def listar(self) -> List[Plugin]:
        """
         Lista todos os Plugins disponíveis.
        """
        pass

    @abstractmethod
    def salvar(self, plugin: Plugin) -> None:
        """
         Salva ou atualiza um Plugin no repositório.
        """
        pass

    @abstractmethod
    def remover(self, plugin_id: int) -> None:
        """
          Remove logicamente um Plugin do repositório.
        """
        pass
