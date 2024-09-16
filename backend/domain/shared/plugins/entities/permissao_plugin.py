# backend/domain/plugins/permissao_plugin.py

from uuid import UUID
from dataclasses import dataclass


@dataclass
class PermissaoPlugin:
    """
    Classe de domínio que representa uma permissão associada a um plugin.

    Atributos:
        id (UUID): Identificador único da permissão.
        name (str): Nome da permissão.
        codename (str): Codinome da permissão.
        content_type_id (UUID): Identificador do tipo de conteúdo associado à permissão.
        plugin_id (UUID): Identificador do plugin associado à permissão.
    """
    id: UUID
    name: str
    codename: str
    content_type_id: UUID
    plugin_id: UUID

