"""
Módulo de domínio responsável pela entidade UsuarioTipoDomain.

Esta classe de domínio representa o tipo de usuário no sistema, como Administrador,
Colaborador, ou Editor. Ela encapsula a lógica de negócio relacionada ao tipo de
usuário, incluindo a validação dos atributos.
"""
from typing import Optional


class UsuarioTipoDomain:
    """
    Classe de domínio que representa um tipo de usuário no sistema.

    Atributos:
        usuario_tipo_id (Optional[int]): Identificador único do tipo de 
        usuário.
        _nome (str): O nome do tipo de usuário (ex: Administrador, Editor).
        _descricao (Optional[str]): Uma breve descrição do tipo de usuário.
    """

    def __init__(self, usuario_tipo_id: Optional[int], nome: str, descricao: Optional[str] = None):
        """
        Inicializa a classe UsuarioTipoDomain com os atributos obrigatórios e opcionais.

        Args:
            usuario_tipo_id (Optional[int]): O identificador único do tipo de usuário.
            nome (str): O nome do tipo de usuário.
            descricao (Optional[str]): A descrição do tipo de usuário.
        """
        self.usuario_tipo_id = usuario_tipo_id
        self.set_nome(nome)
        self.descricao = descricao

    @property
    def nome(self) -> str:
        """Retorna o nome do tipo de usuário."""
        return self._nome

    def set_nome(self, nome: str) -> None:
        """Define o nome do tipo de usuário com validação."""
        if not nome:
            raise ValueError("O nome do tipo de usuário não pode ser vazio.")
        self._nome = nome

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de UsuarioTipoDomain.

        Returns:
            str: Nome do tipo de usuário e sua descrição.
        """
        return f"Tipo de Usuário: {self.nome} - Descrição: {self.descricao or 'Sem descrição'}"
