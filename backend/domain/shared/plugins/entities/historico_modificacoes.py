# backend/domain/plugins/historico_modificacoes.py

from dataclasses import dataclass
from datetime import datetime
from uuid import UUID

@dataclass
class HistoricoModificacoes:
    """
    Classe de domínio que representa o histórico de modificações de um plugin.

    Atributos:
        id (int): Identificador único do histórico de modificações.
        plugin_id (int): Identificador do plugin ao qual este histórico pertence.
        data_modificacao (datetime): Data e hora da modificação.
        usuario (str): Nome do usuário que realizou a modificação.
        descricao_modificacao (str): Descrição da modificação realizada.
    """
  
    id: UUID
    plugin_id: UUID
    data_modificacao: datetime
    usuario: str
    descricao_modificacao: str
