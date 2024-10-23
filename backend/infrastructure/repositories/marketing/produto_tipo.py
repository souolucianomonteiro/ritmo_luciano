# pylint: disable=no-member

"""Módulo implementa o repositório concreto de produto_tipo"""

from typing import Optional, List
from django.db import transaction
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.entities.produto_tipo import TipoProdutoDomain
from domain.marketing.repositories.produto_tipo import TipoProdutoContract
from infrastructure.models.marketing.produto_tipo import TipoProdutoModel


class TipoProdutoRepository(TipoProdutoContract):
    """
    Repositório concreto para a entidade TipoProduto.

    Este repositório interage com o banco de dados e implementa
    as operações de CRUD para a entidade de domínio TipoProduto.
    """

    @transaction.atomic
    def get_by_id(self, tipo_produto_id: int) -> Optional[TipoProdutoDomain]:
        """
        Recupera um tipo de produto pelo ID.

        Args:
            tipo_produto_id (int): O identificador único do tipo de produto.

        Returns:
            Optional[TipoProdutoDomain]: O tipo de produto encontrado ou None.

        Raises:
            EntityNotFoundException: Se o tipo de produto não for encontrado.
            OperationFailedException: Se ocorrer um erro inesperado.
        """
        try:
            tipo_produto_model = TipoProdutoModel.objects.get(id=tipo_produto_id)
            return self._model_to_domain(tipo_produto_model)
        except TipoProdutoModel.DoesNotExist as e:
            raise EntityNotFoundException(
                f"Tipo de produto com ID {tipo_produto_id} não encontrado."
            ) from e
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao buscar o tipo de produto: {str(e)}"
            ) from e

    @transaction.atomic
    def save(self, tipo_produto: TipoProdutoDomain) -> TipoProdutoDomain:
        """
        Salva ou atualiza um tipo de produto no banco de dados.

        Args:
            tipo_produto (TipoProdutoDomain): A entidade de domínio a ser salva.

        Returns:
            TipoProdutoDomain: O tipo de produto salvo ou atualizado.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado.
        """
        try:
            tipo_produto_model, created = TipoProdutoModel.objects.update_or_create(
                id=tipo_produto.tipo_produto_id,
                defaults={
                    'nome': tipo_produto.nome,
                    'descricao': tipo_produto.descricao,
                    'situacao': tipo_produto.situacao
                }
            )
            return self._model_to_domain(tipo_produto_model)
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao salvar o tipo de produto: {str(e)}"
            ) from e

    @transaction.atomic
    def delete(self, tipo_produto_id: int) -> None:
        """
        Exclui um tipo de produto pelo ID.

        Args:
            tipo_produto_id (int): O identificador único do tipo de produto.

        Raises:
            EntityNotFoundException: Se o tipo de produto não for encontrado.
            OperationFailedException: Se ocorrer um erro inesperado.
        """
        try:
            tipo_produto_model = TipoProdutoModel.objects.get(id=tipo_produto_id)
            tipo_produto_model.delete()
        except TipoProdutoModel.DoesNotExist as e:
            raise EntityNotFoundException(
                f"Tipo de produto com ID {tipo_produto_id} não encontrado."
            ) from e
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao excluir o tipo de produto: {str(e)}"
            ) from e

    def list_all(self) -> List[TipoProdutoDomain]:
        """
        Retorna uma lista de todos os tipos de produtos.

        Returns:
            List[TipoProdutoDomain]: Lista de tipos de produtos.
        """
        try:
            tipos_produto = TipoProdutoModel.objects.all()
            return [self._model_to_domain(tipo) for tipo in tipos_produto]
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao listar os tipos de produtos: {str(e)}"
            ) from e

    def _model_to_domain(self, tipo_produto_model: TipoProdutoModel) -> TipoProdutoDomain:
        """
        Converte uma instância de TipoProdutoModel para TipoProdutoDomain.

        Args:
            tipo_produto_model (TipoProdutoModel): A instância da model de banco de dados.

        Returns:
            TipoProdutoDomain: A entidade de domínio convertida.
        """
        return TipoProdutoDomain(
            tipo_produto_id=tipo_produto_model.id,
            nome=tipo_produto_model.nome,
            descricao=tipo_produto_model.descricao,
            situacao=tipo_produto_model.situacao
        )
