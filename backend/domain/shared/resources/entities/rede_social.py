"""
Módulo de domínio responsável pela entidade RedeSocialDomain.

Esta classe de domínio representa uma rede social no sistema, que pode ser associada
a pessoas físicas. As redes sociais incluem um nome e um ícone.
"""

from typing import Optional


class RedeSocialDomain:
    """
    Classe de domínio que representa uma rede social no sistema.

    Atributos:
        id (Optional[int]): Identificador único da rede social.
        _nome (str): Nome da rede social (ex: LinkedIn, Facebook).
        _icone (str): Caminho ou URL do ícone da rede social.
    """

    def __init__(self, nome: str, icone: str, rede_social_id: Optional[int] = None):
        """
        Inicializa a classe RedeSocialDomain com os atributos obrigatórios e opcionais.

        Args:
            nome (str): Nome da rede social.
            icone (str): Caminho ou URL do ícone da rede social.
            rede_social_id (Optional[int]): O identificador único da rede social.
        """
        self.rede_social_id = rede_social_id
        self.set_nome(nome)
        self.set_icone(icone)

    @property
    def nome(self) -> str:
        """Retorna o nome da rede social."""
        return self._nome

    def set_nome(self, nome: str) -> None:
        """Define o nome da rede social com validação."""
        if not nome:
            raise ValueError("O nome da rede social não pode ser vazio.")
        self._nome = nome

    @property
    def icone(self) -> str:
        """Retorna o ícone da rede social."""
        return self._icone

    def set_icone(self, icone: str) -> None:
        """Define o ícone da rede social com validação."""
        if not icone:
            raise ValueError("O ícone da rede social não pode ser vazio.")
        self._icone = icone

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de RedeSocialDomain.

        Returns:
            str: Nome e ícone da rede social.
        """
        return f"Rede Social: {self.nome} - Ícone: {self.icone}"
