""" Módulo implementa a entidade tipo de produto"""

from typing import Optional


class TipoProdutoDomain:
    """
    Classe de domínio que representa o Tipo de Produto.

    Atributos:
        _tipo_produto_id (Optional[int]): Identificador único do tipo de
        produto.
        _nome (str): Nome do tipo de produto.
        _descricao (Optional[str]): Descrição opcional do tipo de produto.
        _situacao (str): Situação atual do tipo de produto.
    """

    def __init__(
        self,
        tipo_produto_id: Optional[int] = None,
        nome: str = '',
        descricao: Optional[str] = None,
        situacao: str = 'criado'
    ):
        """
        Inicializa uma instância de TipoProdutoDomain com validações para o nome e situação.

        Args:
            tipo_produto_id (Optional[int]): O identificador único do tipo de produto.
            nome (str): O nome do tipo de produto.
            descricao (Optional[str]): A descrição opcional do tipo de produto.
            situacao (str): A situação inicial do tipo de produto.
        """
        self._tipo_produto_id = tipo_produto_id
        self.set_nome(nome)
        self._descricao = descricao
        self._situacao = situacao

    # Getter e setter para tipo_produto_id

    @property
    def tipo_produto_id(self) -> Optional[int]:
        return self._tipo_produto_id

    # Getter e setter com validação para nome

    @property
    def nome(self) -> str:
        return self._nome

    def set_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError("O nome do tipo de produto não pode ser vazio.")
        self._nome = nome

    # Getter e setter para descrição

    @property
    def descricao(self) -> Optional[str]:
        return self._descricao

    def set_descricao(self, descricao: Optional[str]) -> None:
        self._descricao = descricao

    # Getter e setter para situação

    @property
    def situacao(self) -> str:
        return self._situacao

    def set_situacao(self, situacao: str) -> None:
        situacoes_validas = ['criado', 'desenvolvimento', 'ativo', 'manutencao', 'inativo']
        if situacao not in situacoes_validas:
            raise ValueError(f"Situação inválida. Escolha entre {situacoes_validas}")
        self._situacao = situacao

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de TipoProdutoDomain.

        Returns:
            str: Representação textual do tipo de produto.
        """
        return f"TipoProduto: {self._nome}, Situação: {self._situacao}"
