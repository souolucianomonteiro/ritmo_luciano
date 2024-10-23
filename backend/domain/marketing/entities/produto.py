"""Implementa a classe de domínio do conceito produto"""

from typing import Optional
from uuid import UUID


class ProdutoDomain:
    """
    Entidade de domínio para Produto.

    Atributos:
        _id (UUID): Identificador único do produto.
        _nome (str): Nome do produto.
        _descricao (Optional[str]): Descrição do produto.
        _tipo_produto_id (UUID): Identificador único do tipo de produto.
    """
    def __init__(self, produto_id: UUID, nome: str, tipo_produto_id: UUID, descricao: Optional[str] = None):
        self._id = produto_id
        self._nome = nome
        self._descricao = descricao
        self._tipo_produto_id = tipo_produto_id

    @property
    def produto_id(self) -> UUID:
        return self._id

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def descricao(self) -> Optional[str]:
        return self._descricao

    @property
    def tipo_produto_id(self) -> UUID:
        return self._tipo_produto_id

    def set_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError("O nome do produto não pode ser vazio.")
        self._nome = nome

    def set_descricao(self, descricao: Optional[str]) -> None:
        self._descricao = descricao

    def set_tipo_produto_id(self, tipo_produto_id: UUID) -> None:
        if not tipo_produto_id:
            raise ValueError("O tipo de produto deve ser informado.")
        self._tipo_produto_id = tipo_produto_id

    def __str__(self):
        return f"Produto: {self._nome} (ID: {self._id})"
