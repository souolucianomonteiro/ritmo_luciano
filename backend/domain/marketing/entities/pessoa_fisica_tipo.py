"""
Módulo que define a classe de domínio PessoaFisicaTipoDomain.

Essa classe representa a associação entre uma Pessoa Física e o Tipo de Usuário no domínio.
Ela encapsula os dados e comportamentos relacionados à associação, fornecendo métodos para
acessar e modificar os atributos de maneira controlada.
"""

from datetime import datetime
from typing import Optional


class PessoaFisicaTipoDomain:
    """
    Classe de domínio que representa a associação entre Pessoa Física e o Tipo de Usuário.

    Atributos:
        pessoa_fisica_tipo_id (Optional[int]): Identificador único da associação.
        pessoa_fisica_id (int): Identificador da pessoa física associada.
        usuario_tipo_id (int): Identificador do tipo de usuário associado.
        data_criacao (datetime): Data de criação da associação.
        ativo (bool): Status indicando se a associação está ativa.
    """

    def __init__(self, 
                 pessoa_fisica_tipo_id: Optional[int] = None,
                 pessoa_fisica_id: int = None,
                 usuario_tipo_id: int = None,
                 data_criacao: datetime = None,
                 ativo: bool = True):
        """
        Inicializa uma instância de PessoaFisicaTipoDomain.

        Parâmetros:
            pessoa_fisica_tipo_id (Optional[int]): Identificador único da associação.
            pessoa_fisica_id (int): Identificador da pessoa física associada.
            usuario_tipo_id (int): Identificador do tipo de usuário associado.
            data_criacao (datetime): Data de criação da associação. Padrão é a data atual.
            ativo (bool): Status indicando se a associação está ativa. Padrão é True.
        """
        self._pessoa_fisica_tipo_id = pessoa_fisica_tipo_id
        self._pessoa_fisica_id = pessoa_fisica_id
        self._usuario_tipo_id = usuario_tipo_id
        self._data_criacao = data_criacao or datetime.now()
        self._ativo = ativo

    # Getters
    def get_pessoa_fisica_tipo_id(self) -> Optional[int]:
        """
        Retorna o identificador único da associação PessoaFisicaTipo.

        Retorna:
            Optional[int]: O identificador da associação ou None se não estiver definido.
        """
        return self._pessoa_fisica_tipo_id

    def get_pessoa_fisica_id(self) -> int:
        """
        Retorna o identificador da Pessoa Física associada.

        Retorna:
            int: O identificador da pessoa física associada.
        """
        return self._pessoa_fisica_id

    def get_usuario_tipo_id(self) -> int:
        """
        Retorna o identificador do Tipo de Usuário associado.

        Retorna:
            int: O identificador do tipo de usuário associado.
        """
        return self._usuario_tipo_id

    def get_data_criacao(self) -> datetime:
        """
        Retorna a data de criação da associação.

        Retorna:
            datetime: A data e hora de criação da associação.
        """
        return self._data_criacao

    def is_ativo(self) -> bool:
        """
        Verifica se a associação está ativa.

        Retorna:
            bool: True se a associação estiver ativa, False caso contrário.
        """
        return self._ativo

    # Setters
    def set_pessoa_fisica_tipo_id(self, pessoa_fisica_tipo_id: int) -> None:
        """
        Define o identificador único da associação PessoaFisicaTipo.

        Parâmetros:
            pessoa_fisica_tipo_id (int): O novo identificador da associação.
        """
        self._pessoa_fisica_tipo_id = pessoa_fisica_tipo_id

    def set_pessoa_fisica_id(self, pessoa_fisica_id: int) -> None:
        """
        Define o identificador da Pessoa Física associada.

        Parâmetros:
            pessoa_fisica_id (int): O novo identificador da pessoa física.
        """
        self._pessoa_fisica_id = pessoa_fisica_id

    def set_usuario_tipo_id(self, usuario_tipo_id: int) -> None:
        """
        Define o identificador do Tipo de Usuário associado.

        Parâmetros:
            usuario_tipo_id (int): O novo identificador do tipo de usuário.
        """
        self._usuario_tipo_id = usuario_tipo_id

    def set_data_criacao(self, data_criacao: datetime) -> None:
        """
        Define a data de criação da associação.

        Parâmetros:
            data_criacao (datetime): A nova data de criação.
        """
        self._data_criacao = data_criacao

    def set_ativo(self, ativo: bool) -> None:
        """
        Define o status ativo/inativo da associação.

        Parâmetros:
            ativo (bool): O novo status da associação.
        """
        self._ativo = ativo

    def __str__(self):
        """
        Retorna uma representação em string da instância de PessoaFisicaTipoDomain.

        Retorna:
            str: Representação textual da instância, mostrando os principais atributos.
        """
        return f"PessoaFisicaTipoDomain(pessoa_fisica_id={self._pessoa_fisica_id}, usuario_tipo_id={self._usuario_tipo_id}, ativo={self._ativo})"
