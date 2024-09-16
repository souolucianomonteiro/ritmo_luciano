"""
Módulo responsável pela definição da classe de domínio TagPlugin.

Este módulo define a classe de domínio `TagPlugin`, que representa uma tag associada a um plugin.
A classe `TagPlugin` é usada para encapsular os dados essenciais relacionados a uma tag no contexto
do domínio, focando na lógica de negócios e na estrutura de dados, sem se preocupar com detalhes de
persistência, auditoria ou exclusão lógica.

Classes:
    TagPlugin: Classe de domínio que encapsula os atributos essenciais de uma tag de plugin.
"""

from dataclasses import dataclass

@dataclass
class TagPlugin:
    """
    Classe de domínio que representa uma Tag associada a um plugin.

    Atributos:
        id (int): Identificador único da tag.
        nome (str): Nome da tag.
    """

    id: int
    nome: str
