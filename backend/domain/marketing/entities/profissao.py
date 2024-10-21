"""
Módulo de domínio responsável pela entidade ProfissaoDomain.

Esta classe de domínio representa uma profissão no sistema, como médicos, engenheiros,
advogados, etc. A classe encapsula a lógica de negócio e validações relacionadas à profissão.
"""
from typing import Optional


class ProfissaoDomain:
    """
    Classe de domínio que representa uma profissão no sistema.

    Atributos:
        id (Optional[int]): Identificador único da profissão.
        _codigo (str): Código único da profissão.
        _descricao (str): Descrição da profissão.
    """

    def __init__(self, codigo: str, descricao: str, profissao_id: Optional[int] = None):
        """
        Inicializa a classe ProfissaoDomain com os atributos obrigatórios e
        opcionais.

        Args:
            codigo (str): O código da profissão.
            descricao (str): A descrição da profissão.
            profissao_id (Optional[int]): O identificador único da profissão.
        """
        self.profissao_id = profissao_id
        self.set_codigo(codigo)
        self.set_descricao(descricao)

    @property
    def codigo(self) -> str:
        """Retorna o código da profissão."""
        return self._codigo

    def set_codigo(self, codigo: str) -> None:
        """Define o código da profissão com validação."""
        if not codigo:
            raise ValueError("O código da profissão não pode ser vazio.")
        self._codigo = codigo

    @property
    def descricao(self) -> str:
        """Retorna a descrição da profissão."""
        return self._descricao

    def set_descricao(self, descricao: str) -> None:
        """Define a descrição da profissão com validação."""
        if not descricao:
            raise ValueError("A descrição da profissão não pode ser vazia.")
        self._descricao = descricao

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de ProfissaoDomain.

        Returns:
            str: Código e descrição da profissão.
        """
        return f"Profissão: {self.codigo} - Descrição: {self.descricao}"
