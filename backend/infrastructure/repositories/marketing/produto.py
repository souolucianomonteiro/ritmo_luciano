# pylint: disable=no-member

"""Implmenta o repositório do conceito produto"""

from typing import List, Optional
from django.db import transaction
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.entities.produto import ProdutoDomain
from domain.marketing.repositories.produto import ProdutoContract
from infrastructure.models.marketing.produto import ProdutoModel
from infrastructure.repositories.marketing.produto_tipo import (
                                            TipoProdutoRepository)


class ProdutoRepository(ProdutoContract):
    """
    Repositório concreto para a entidade Produto.

    Este repositório gerencia as operações de persistência e recuperação
    de Produto no banco de dados, interagindo também com o repositório de
    TipoProduto para garantir que o tipo de produto esteja corretamente
    associado.
    """

    def __init__(self, tipo_produto_repository: TipoProdutoRepository):
        self.tipo_produto_repository = tipo_produto_repository

    @transaction.atomic
    def get_by_id(self, produto_id: str) -> Optional[ProdutoDomain]:
        """
        Recupera um produto pelo ID no banco de dados.

        Args:
            produto_id (str): O identificador único do produto.

        Returns:
            Optional[ProdutoDomain]: A entidade de domínio do produto
            ou None se não encontrado.

        Raises:
            EntityNotFoundException: Se o produto não for encontrado.
        """
        try:
            produto_model = ProdutoModel.objects.get(id=produto_id)
            return self._model_to_domain(produto_model)
        except ProdutoModel.DoesNotExist as e:
            raise EntityNotFoundException(f"Produto com ID {produto_id} não encontrado.") from e
        except Exception as e:
            raise OperationFailedException(f"Erro ao buscar o produto: {str(e)}") from e

    @transaction.atomic
    def save(self, produto: ProdutoDomain, user) -> str:
        """
        Salva ou atualiza um produto no banco de dados.

        Args:
            produto (ProdutoDomain): A entidade de domínio a ser salva.

        Returns:
            str: Mensagem de sucesso indicando se o produto foi criado ou
            atualizado.

        Raises:
            EntityNotFoundException: Se o tipo de produto não for encontrado.
            OperationFailedException: Se ocorrer um erro ao salvar o produto.
        """
        try:
            # Verifica se o tipo de produto existe usando o repositório apropriado
            tipo_produto_model = self.tipo_produto_repository.get_by_id(produto.tipo_produto_id)

            if not tipo_produto_model:
                raise EntityNotFoundException(f"Tipo de Produto com ID {produto.tipo_produto_id} não encontrado.")

            # Criando ou atualizando o produto no banco de dados
            produto_model, created = ProdutoModel.objects.update_or_create(
                id=produto.produto_id,
                defaults={
                    'nome': produto.nome,
                    'descricao': produto.descricao,
                    'tipo_produto': tipo_produto_model,  # Associa o tipo de produto ao produto
                }
            )

            # Garantir que os campos de auditoria sejam preenchidos passando o user
            produto_model.save(user=user)
            
            # Retorna uma mensagem de acordo com a operação realizada
            if created:
                return "Produto criado com sucesso."
            else:
                return "Produto atualizado com sucesso."

        except EntityNotFoundException as e:
            raise e  # Propaga a exceção de entidade não encontrada
        except Exception as e:
            raise OperationFailedException(f"Erro ao salvar o produto: {str(e)}") from e

    @transaction.atomic
    def delete(self, produto_id: str, user) -> str:
        """
        Exclui um produto do banco de dados pelo ID.

        Args:
            produto_id (str): O identificador único do produto.

        Returns:
            str: Mensagem de sucesso da exclusão.

        Raises:
            EntityNotFoundException: Se o produto não for encontrado.
            OperationFailedException: Se ocorrer um erro inesperado.
        """
        try:
            produto_model = ProdutoModel.objects.get(id=produto_id)
            produto_model.delete(user=user)
            return "Produto excluído com sucesso."
        except ProdutoModel.DoesNotExist as e:
            raise EntityNotFoundException(f"Produto com ID {produto_id} não encontrado.") from e
        except Exception as e:
            raise OperationFailedException(f"Erro ao excluir o produto: {str(e)}") from e

    def list_all(self) -> List[ProdutoDomain]:
        """
        Retorna uma lista de todos os produtos do banco de dados.

        Returns:
            List[ProdutoDomain]: Lista de todas as entidades Produto.

        Raises:
            OperationFailedException: Se ocorrer um erro ao listar os produtos.
        """
        try:
            produtos_model = ProdutoModel.objects.all()
            return [self._model_to_domain(produto) for produto in produtos_model]
        except Exception as e:
            raise OperationFailedException(f"Erro ao listar produtos: {str(e)}") from e

    # Métodos auxiliares privados

    def _model_to_domain(self, produto_model: ProdutoModel) -> ProdutoDomain:
        """
        Converte uma instância de ProdutoModel para ProdutoDomain.

        Args:
            produto_model (ProdutoModel): A instância do modelo de banco de dados.

        Returns:
            ProdutoDomain: A entidade de domínio do produto.
        """
        return ProdutoDomain(
            produto_id=produto_model.id,
            nome=produto_model.nome,
            descricao=produto_model.descricao,
            tipo_produto_id=produto_model.tipo_produto.id
        )
