# pylint: disable=no-member
"""Módulo implementa o repositório concreto de reacao_tipo"""

from typing import List, Optional
from domain.blog.repositories.reacao_tipo import ReacaoTipoRepository
from domain.blog.value_objects.reacao_tipo import ReacaoTipoDomain
from infrastructure.models.blog.reacao_tipo import ReacaoTipo


class DjangoReacaoTipoRepository(ReacaoTipoRepository):
    """
    Repositório concreto para manipulação dos dados do tipo de reação (ReacaoTipo), usando Django ORM.
    """

    def list_all(self) -> List[ReacaoTipoDomain]:
        """
        Retorna uma lista com todos os tipos de reações disponíveis.

        Retorno:
            List[ReacaoTipoDomain]: Uma lista contendo todas as instâncias de ReacaoTipoDomain.
        """
        reacoes = ReacaoTipo.objects.all()
        return [
            ReacaoTipoDomain(
                repositorio_tipo_id=reacao.id,  
                nome=reacao.nome,
                descricao=reacao.descricao,
                icone=reacao.icone
            ) for reacao in reacoes
        ]

    def get_by_id(self, reacao_tipo_id: int) -> Optional[ReacaoTipoDomain]:
        """
        Retorna um tipo de reação específico pelo ID.

        Parâmetros:
            repositorio_tipo_id (int): O ID do tipo de reação.

        Retorno:
            Optional[ReacaoTipoDomain]: O tipo de reação correspondente ou None, se não for encontrado.
        """
        try:
            reacao = ReacaoTipo.objects.get(id=reacao_tipo_id)
            return ReacaoTipoDomain(
                repositorio_tipo_id=reacao.id,
                nome=reacao.nome,
                descricao=reacao.descricao,
                icone=reacao.icone
            )
        except ReacaoTipo.DoesNotExist:
            return None

