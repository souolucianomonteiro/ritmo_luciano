# backend/domain/plugins/permissao_plugin.py

from uuid import UUID
from dataclasses import dataclass


@dataclass
class PermissaoPlugin:
    """
    Classe de domínio que representa uma permissão associada a um plugin.

    Atributos:
        id (UUID): Identificador único da permissão.
        plugin_id (UUID): Identificador do plugin ao qual a permissão
        está associada.
        codename (str): Código único da permissão.
        name (str): Nome descritivo da permissão.
    """

    id: UUID
    plugin_id: UUID
    codename: str
    name: str
