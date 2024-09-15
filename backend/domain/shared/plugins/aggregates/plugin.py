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
from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from domain.shared.plugins.entities.categoria import Categoria
from domain.shared.plugins.entities.tipo_plugin import TipoPlugin
from domain.shared.plugins.entities.artefato_plugin import ArtefatoPlugin


@dataclass
class Plugin:
    """
    Classe de domínio que representa o agregado Plugin.

    Atributos:
        id (Optional[int]): Identificador único do plugin.
        nome (str): Nome do plugin.
        versao (str): Versão do plugin.
        descricao (Optional[str]): Descrição do plugin.
        status (str): Status atual do plugin.
        documentacao (Optional[str]): Documentação associada ao plugin.
        permissoes (List[str]): Lista de permissões necessárias para o uso do
        plugin.
        historico_modificacoes (List[str]): Histórico de modificações do
        plugin.
        tags (List[str]): Tags associadas ao plugin para classificação.
        dependencias (List[str]): Dependências de outros plugins ou pacotes.
        criado_em (datetime): Data de criação do plugin.
        atualizado_em (datetime): Data de última atualização do plugin.
        ativo (bool): Indica se o plugin está ativo.
    """

    id: Optional[int]
    categoria: Categoria
    tipo_plugin: TipoPlugin
    nome: str
    versao: str
    descricao: Optional[str]
    artefato_plugin: ArtefatoPlugin
    status: str
    documentacao: Optional[str]
    permissoes: List[str] = field(default_factory=list)
    historico_modificacoes: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    dependencias: List[str] = field(default_factory=list)
    criado_em: datetime
    atualizado_em: datetime
    ativo: bool
