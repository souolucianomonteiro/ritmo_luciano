# backend/domain/plugins/template_plugin.py

from dataclasses import dataclass
from uuid import UUID

@dataclass
class TemplatePlugin:
    """
    Classe de domínio que representa um template associado a um plugin.

    Atributos:
        id (UUID): Identificador único do template.
        plugin_id (UUID): Identificador do plugin ao qual o template está associado.
        nome_template (str): Nome descritivo do template.
        caminho_arquivo (str): Caminho do arquivo de template no sistema de arquivos.
        contexto_placeholder (str, opcional): Contexto específico para o qual o template foi criado.
    """

    id: UUID
    plugin_id: UUID
    nome_template: str
    caminho_arquivo: str
    contexto_placeholder: str = None
