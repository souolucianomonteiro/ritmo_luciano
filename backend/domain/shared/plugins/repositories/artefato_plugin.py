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
from typing import List, Optional
from domain.shared.plugins.entities.artefato_plugin import ArtefatoPlugin


class ArtefatoPluginRepository(ABC):
    """
    Interface de repositório para ArtefatoPlugin.

    Define os métodos que qualquer implementação concreta de um repositório de
    ArtefatoPlugin deve possuir.
    """

    @abstractmethod
    def obter_por_id(self, artefato_plugin_id: int) -> Optional[ArtefatoPlugin]:
        """
        Obtém um ArtefatoPlugin pelo seu ID.

        :param artefato_plugin_id: O ID do ArtefatoPlugin a ser obtido.
        :return: O ArtefatoPlugin correspondente, ou None se não encontrado.
        """
        pass

    @abstractmethod
    def listar(self) -> List[ArtefatoPlugin]:
        """
        Lista todos os ArtefatoPlugins ativos.

        :return: Uma lista de ArtefatoPlugins.
        """
        pass

    @abstractmethod
    def salvar(self, artefato_plugin: ArtefatoPlugin) -> None:
        """
        Salva ou atualiza um ArtefatoPlugin.

        :param artefato_plugin: O ArtefatoPlugin a ser salvo ou atualizado.
        """
        pass

    @abstractmethod
    def remover(self, artefato_plugin_id: int) -> None:
        """
        Remove um ArtefatoPlugin logicamente (soft delete).

        :param artefato_plugin_id: O ID do ArtefatoPlugin a ser removido.
        """
        pass

