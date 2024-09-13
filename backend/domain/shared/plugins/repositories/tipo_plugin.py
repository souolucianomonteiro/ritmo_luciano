"""
Módulo que define o repositório para a entidade `TipoPlugin`.

O repositório encapsula a lógica de persistência e recuperação dos dados
relacionados ao TipoPlugin no banco de dados.
"""
from typing import List, Optional  # Import da biblioteca padrão
from abc import ABC, abstractmethod
from domain.shared.plugins.entities.tipo_plugin import TipoPlugin


class TipoPluginRepository(ABC):
    """
    Interface para o repositório de TipoPlugin.

    Define os métodos que devem ser implementados para manipulação dos tipos
    de plugin no banco de dados.
    """

    @abstractmethod
    def adicionar(self, tipo_plugin: TipoPlugin) -> None:
        """
        Adiciona um novo TipoPlugin ao repositório.

        Args:
            tipo_plugin (TipoPlugin): O tipo de plugin a ser adicionado.
        """
        ...

    @abstractmethod
    def obter_por_id(self, tipo_plugin_id: int) -> Optional[TipoPlugin]:
        """
        Obtém um TipoPlugin pelo seu ID.

        Args:
            tipo_plugin_id (int): O ID do tipo de plugin a ser obtido.

        Returns:
            Optional[TipoPlugin]: O tipo de plugin encontrado ou None.
        """
        ...

    @abstractmethod
    def listar_todos(self) -> List[TipoPlugin]:
        """
        Lista todos os Tipos de Plugin do repositório.

        Returns:
            List[TipoPlugin]: Uma lista com todos os tipos de plugin.
        """
        ...

    @abstractmethod
    def remover(self, tipo_plugin_id: int) -> None:
        """
        Remove um TipoPlugin do repositório pelo seu ID.

        Args:
            tipo_plugin_id (int): O ID do tipo de plugin a ser removido.
        """
        ...

    # Métodos adicionais para operações CRUD podem ser adicionados aqui.
