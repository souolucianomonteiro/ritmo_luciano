"""
Módulo que define a estrutura do agregado Plugin.

Este módulo contém a definição da classe Plugin, que representa o agregado
principal no contexto da aplicação, juntamente com seus repositórios
e outras operações associadas. A classe Plugin encapsula os conceitos
relacionados a um plugin, como artefatos, documentação, permissões, histórico
de modificações, tags e dependências.

Classes:
    Plugin: Representa o agregado Plugin com seus atributos e métodos.
    PluginRepository: Interface para o repositório do agregado Plugin.
    PluginRepositoryConcrete: Implementação concreta do repositório do
    agregado Plugin.
"""
# backend/domain/plugins/plugin.py

from dataclasses import dataclass
from typing import List, Optional
from uuid import UUID

@dataclass
class Plugin:
    """
    Classe de domínio que representa o agregado Plugin.

    Atributos:
        id (UUID): Identificador único do plugin.
        nome (str): Nome do plugin.
        categoria_id (UUID): Identificador da categoria do plugin.
        tipo_plugin_id (UUID): Identificador do tipo do plugin.
        versao (str): Versão do plugin.
        descricao (str, opcional): Descrição do plugin.
        artefato_plugin_id (UUID, opcional): Identificador do artefato 
        associado ao plugin.
        documentacao (str, opcional): Documentação do plugin.
        caminho_arquivo (str): Caminho do arquivo principal do plugin.
        permissoes (List[UUID], opcional): Lista de identificadores das
        permissões associadas ao plugin.
        historico_modificacoes (List[UUID], opcional): Lista de
        identificadores de históricos de modificações do plugin.
        tags (List[UUID], opcional): Lista de identificadores de tags
        associadas ao plugin.
        dependencias (List[UUID], opcional): Lista de identificadores de
        dependências do plugin.
        templates (List[UUID], opcional): Lista de identificadores dos 
        templates associados ao plugin.
    """

    id: UUID
    nome: str
    categoria_id: UUID
    tipo_plugin_id: UUID
    versao: str
    descricao: Optional[str] = None
    artefato_plugin_id: Optional[UUID] = None
    documentacao: Optional[str] = None
    caminho_arquivo: str
    permissoes: Optional[List[UUID]] = None
    historico_modificacoes: Optional[List[UUID]] = None
    tags: Optional[List[UUID]] = None
    dependencias: Optional[List[UUID]] = None
    templates: Optional[List[UUID]] = None
