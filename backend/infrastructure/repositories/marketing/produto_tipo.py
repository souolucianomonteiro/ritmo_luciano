# pylint: disable=no-member

"""Módulo implementa o repositório concreto de produto_tipo"""

from typing import Optional
from domain.marketing.repositories.produto_tipo import TipoProdutoRepository
from domain.marketing.entities.produto_tipo import TipoProdutoDomain
from infrastructure.models.marketing.produto_tipo import TipoProdutoModel


class TipoProdutoRepositoryConcrete(TipoProdutoRepository):
    """
    Implementação concreta do repositório de Tipo de Produto.
    Faz a conversão entre o TipoProdutoDomain e TipoProdutoModel, garantindo
    que as operações sejam abstraídas e interajam corretamente com o
    banco de dados.
    """

    def get_by_id(self, tipo_produto_id: int) -> Optional[TipoProdutoDomain]:
        """
        Busca um TipoProdutoDomain pelo seu ID no banco de dados.
        """
        try:
            model = TipoProdutoModel.objects.get(id=tipo_produto_id)
            return self._model_to_domain(model)
        except TipoProdutoModel.DoesNotExist:
            return None

    def get_by_name(self, nome: str) -> Optional[TipoProdutoDomain]:
        """
        Busca um TipoProdutoDomain pelo seu nome no banco de dados.
        """
        model = TipoProdutoModel.objects.filter(nome=nome).first()
        return self._model_to_domain(model) if model else None

    def save(self, tipo_produto: TipoProdutoDomain) -> TipoProdutoDomain:
        """
        Salva ou atualiza um TipoProdutoDomain no banco de dados.
        """
        model = self._domain_to_model(tipo_produto)
        model.save()
        return self._model_to_domain(model)

    def delete(self, tipo_produto_id: int) -> None:
        """
        Remove um TipoProdutoDomain do banco de dados pelo seu ID.
        """
        TipoProdutoModel.objects.filter(id=tipo_produto_id).delete()

    def _model_to_domain(self, model: TipoProdutoModel) -> TipoProdutoDomain:
        """
        Converte um TipoProdutoModel para TipoProdutoDomain.
        """
        return TipoProdutoDomain(
            tipo_produto_id=model.id,
            nome=model.nome,
            descricao=model.descricao
        )

    def _domain_to_model(self, domain: TipoProdutoDomain) -> TipoProdutoModel:
        """
        Converte um TipoProdutoDomain para TipoProdutoModel.
        """
        return TipoProdutoModel(
            id=domain.tipo_produto_id,
            nome=domain.nome,
            descricao=domain.descricao
        )
