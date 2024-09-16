# backend/domain/plugins/dependencia.py

# backend/domain/plugins/dependencia.py

from dataclasses import dataclass
from uuid import UUID

@dataclass
class Dependencia:
    """
    Classe de domínio que representa uma dependência entre plugins.

    Atributos:
        id (UUID): Identificador único da dependência.
        plugin_id (UUID): Identificador do plugin que possui a dependência.
        tipo_dependencia (str): Tipo da dependência (plugin, biblioteca, serviço, etc.).
        dependencia_plugin_id (UUID, opcional): Identificador do plugin do qual o plugin depende.
        nome_dependencia (str, opcional): Nome da dependência (para bibliotecas ou serviços).
        url_dependencia (str, opcional): URL da dependência (para serviços ou recursos externos).
    """

    id: UUID
    plugin_id: UUID
    tipo_dependencia: str
    dependencia_plugin_id: UUID = None
    nome_dependencia: str = None
    url_dependencia: str = None
