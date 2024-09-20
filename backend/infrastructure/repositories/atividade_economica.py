"""
Módulo responsável pela implementação do repositório concreto DjangoAtividadeEconomicaRepository.

Este módulo define o repositório concreto para manipulação da model AtividadeEconomicaModel
utilizando o Django ORM. Ele implementa as operações de CRUD (Create, Read, Update, Delete)
e outras funcionalidades necessárias para a persistência da entidade Atividade Econômica no banco de dados.

Classes:
    DjangoAtividadeEconomicaRepository: Repositório concreto que implementa os métodos de persistência
    para a entidade Atividade Econômica utilizando o Django ORM.
"""
from typing import List, Optional
from domain.website.entities.atividade_economica import (
                                AtividadeEconomicaDomain)
from domain.website.repositories.atividade_economica import (
                                AtividadeEconomicaRepository)
from infrastructure.models.atividade_economica import AtividadeEconomicaModel


class DjangoAtividadeEconomicaRepository(AtividadeEconomicaRepository):
    """
    Repositório concreto para manipular a model AtividadeEconomica no Django ORM.
    """

    def save(self, atividade_economica: AtividadeEconomicaDomain) -> (
        AtividadeEconomicaDomain:)
        atividade_model = AtividadeEconomicaModel.objects.update_or_create(
            id=atividade_economica.id,
            defaults={
                'atividade_econ_codigo': atividade_economica.atividade_econ_codigo,
                'atividade_econ_descricao': atividade_economica.atividade_econ_descricao
            }
        )[0]
        return AtividadeEconomicaDomain(
            id=atividade_model.id,
            atividade_econ_codigo=atividade_model.atividade_econ_codigo,
            atividade_econ_descricao=atividade_model.atividade_econ_descricao
        )

    def find_by_id(self, id: int) -> Optional[AtividadeEconomicaDomain]:
        try:
            atividade_model = AtividadeEconomicaModel.objects.get(id=id)
            return AtividadeEconomicaDomain(
                id=atividade_model.id,
                atividade_econ_codigo=atividade_model.atividade_econ_codigo,
                atividade_econ_descricao=atividade_model.atividade_econ_descricao
            )
        except AtividadeEconomicaModel.DoesNotExist:
            return None

    def find_all(self) -> List[AtividadeEconomicaDomain]:
        atividades = AtividadeEconomicaModel.objects.all()
        return [
            AtividadeEconomicaDomain(
                id=atividade.id,
                atividade_econ_codigo=atividade.atividade_econ_codigo,
                atividade_econ_descricao=atividade.atividade_econ_descricao
            ) for atividade in atividades
        ]

    def delete(self, id: int) -> None:
        AtividadeEconomicaModel.objects.filter(id=id).delete()
