"""
Módulo de repositório para a entidade Plugin.

Este módulo define a interface abstrata para o repositório da entidade Plugin,
fornecendo os métodos necessários para interação com os dados persistidos no 
banco de dados ou em outro mecanismo de armazenamento.

A interface do repositório é projetada para fornecer uma abstração que pode ser
implementada de diferentes maneiras, conforme a necessidade da camada de 
infraestrutura.
"""
# backend/domain/repositories/plugin_repository.py

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID
from domain.shared.plugins.aggregates.plugin import Plugin


class PluginRepository(ABC):
    """
    Repositório abstrato para operações relacionadas ao agregado Plugin.
    """

    @abstractmethod
    def add(self, plugin: Plugin) -> None:
        pass

    @abstractmethod
    def get(self, plugin_id: UUID) -> Optional[Plugin]:
        pass

    @abstractmethod
    def update(self, plugin: Plugin) -> None:
        pass

    @abstractmethod
    def delete(self, plugin_id: UUID) -> None:
        pass

    @abstractmethod
    def list(self) -> List[Plugin]:
        pass

    @abstractmethod
    def list_by_categoria(self, categoria_id: UUID) -> List[Plugin]:
        pass

    @abstractmethod
    def list_by_tipo(self, tipo_plugin_id: UUID) -> List[Plugin]:
        pass

