"""
Módulo que define a entidade ArtefatoPlugin.

Esta entidade representa o artefato de um plugin, incluindo informações
como nome, versão, descrição e outros atributos relacionados ao ciclo
de vida do artefato.
"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class ArtefatoPluginDomain:
    """
    Representa um Artefato Plugin no domínio.

    Atributos:
        id (Optional[int]): Identificador único do artefato.
        nome (str): Nome do artefato plugin.
        descricao (Optional[str]): Descrição do artefato plugin.
        versao (str): Versão do artefato plugin.
        tipo_arquivo (str): Tipo de arquivo do artefato plugin.
        caminho_arquivo (str): Caminho do arquivo do artefato plugin.
        criado_em (datetime): Data e hora da criação do artefato.
        atualizado_em (datetime): Data e hora da última atualização do
        artefato.
        criado_por (Optional[str]): Usuário que criou o artefato.
        atualizado_por (Optional[str]): Usuário que atualizou o artefato pela
        última vez.
        ativo (bool): Indica se o artefato está ativo.
    """
    artefato_plugin_id: Optional[int]
    nome: str
    descricao: Optional[str]
    versao: str
    tipo_arquivo: str
    caminho_arquivo: str
    criado_em: datetime
    atualizado_em: datetime
    criado_por: Optional[str]
    atualizado_por: Optional[str]
    ativo: bool
