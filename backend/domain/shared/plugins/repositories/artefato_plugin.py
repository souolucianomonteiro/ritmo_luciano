"""
Módulo que contém a implementação concreta do repositório de `ArtefatoPlugin` 
na camada de infraestrutura.

Este módulo define a classe `ArtefatoPluginRepositoryConcrete`, que provê os métodos 
necessários para interação com o banco de dados para operações CRUD (Create, Read, 
Update, Delete) em instâncias de `ArtefatoPlugin`. As operações incluem obtenção 
por ID, listagem de todos os registros ativos, salvamento e remoção lógica 
(usando soft delete).

Classes:
    ArtefatoPluginRepositoryConcrete: Implementação concreta do repositório 
    de `ArtefatoPlugin` utilizando o Django ORM.
"""
from abc import ABC, abstractmethod
from typing import Optional, List
from domain.shared.plugins.entities.artefato_plugin import ArtefatoPluginDomain

class ArtefatoPluginRepository(ABC):
    """
    Repositório abstrato para gerenciamento de ArtefatoPlugin no domínio.

    Define as operações essenciais sobre o objeto de domínio ArtefatoPluginDomain.
    """

    @abstractmethod
    def get_by_id(self, artefato_plugin_id: int) -> Optional[ArtefatoPluginDomain]:
        """
        Busca um ArtefatoPluginDomain pelo seu ID.

        Parâmetros:
            artefato_plugin_id (int): O ID do artefato plugin a ser buscado.

        Retorna:
            Optional[ArtefatoPluginDomain]: O objeto de domínio se encontrado, 
            ou None caso não exista.
        """
        pass

    @abstractmethod
    def get_all(self) -> List[ArtefatoPluginDomain]:
        """
        Busca todos os artefatos de plugin.

        Retorna:
            List[ArtefatoPluginDomain]: Lista contendo todos os artefatos de plugin.
        """
        pass

    @abstractmethod
    def save(self, artefato_plugin: ArtefatoPluginDomain) -> ArtefatoPluginDomain:
        """
        Salva ou atualiza um ArtefatoPluginDomain.

        Parâmetros:
            artefato_plugin (ArtefatoPluginDomain): O objeto de domínio a ser salvo ou atualizado.

        Retorna:
            ArtefatoPluginDomain: O objeto de domínio salvo ou atualizado.
        """
        pass

    @abstractmethod
    def delete(self, artefato_plugin_id: int) -> None:
        """
        Remove um ArtefatoPluginDomain com base no seu ID.

        Parâmetros:
            artefato_plugin_id (int): O ID do artefato a ser removido.

        Retorna:
            None
        """
        pass
