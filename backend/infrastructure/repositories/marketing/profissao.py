# pylint: disable=no-member
from typing import List, Optional
from domain.website.entities.profissao import Profissao
from domain.website.repositories.profissao import ProfissaoRepository
from infrastructure.models.marketing.profissao import ProfissaoModel


class DjangoProfissaoRepository(ProfissaoRepository):
    """
    Repositório concreto para manipular a model Profissao no Django ORM.
    """

    def save(self, profissao: 'Profissao') -> 'Profissao':
        profissao_model, _ = ProfissaoModel.objects.update_or_create(
            id=profissao.id,
            defaults={
                'codigo': profissao.codigo,
                'descricao': profissao.descricao
            }
        )
        return Profissao(
            id=profissao_model.id,
            codigo=profissao_model.codigo,
            descricao=profissao_model.descricao
        )

    def find_by_id(self, profissao_id: int) -> Optional['Profissao']:  # Renomeie o id
        try:
            profissao_model = ProfissaoModel.objects.get(id=profissao_id)
            return Profissao(
                id=profissao_model.id,
                codigo=profissao_model.codigo,
                descricao=profissao_model.descricao
            )
        except ProfissaoModel.DoesNotExist:
            return None

    def find_all(self) -> List['Profissao']:
        profissoes = ProfissaoModel.objects.all()
        return [
            Profissao(
                id=profissao.id,
                codigo=profissao.codigo,
                descricao=profissao.descricao
            ) for profissao in profissoes
        ]

    def delete(self, profissao_id: int) -> None:  # Renomeie o id
        ProfissaoModel.objects.filter(id=profissao_id).delete()
