# backend/infrastructure/repositories/historico_modificacoes_repository.py
# pylint: disable=no-member

from uuid import UUID
from typing import List, Optional
from domain.shared.plugins.entities.historico_modificacoes import (
                                            HistoricoModificacoes)
from domain.shared.plugins.repositories.historico_modificacoes import (
                                        HistoricoModificacoesRepository)
from infrastructure.models.historico_modificacoes import (
                                HistoricoModificacoesModel)


class DjangoHistoricoModificacoesRepository(HistoricoModificacoesRepository):
    """
    Implementação concreta do repositório de Histórico de Modificações
    utilizando o Django ORM.
    """

    def add(self, historico_modificacoes: HistoricoModificacoes) -> None:
        HistoricoModificacoesModel.objects.create(
            plugin_id=historico_modificacoes.plugin_id,
            data_modificacao=historico_modificacoes.data_modificacao,
            usuario=historico_modificacoes.usuario,
            descricao_modificacao=historico_modificacoes.descricao_modificacao
        )

    def get(self, historico_modificacoes_id: UUID) -> Optional[HistoricoModificacoes]:
        try:
            historico_model = HistoricoModificacoesModel.objects.get(pk=historico_modificacoes_id, is_deleted=False)  # pylint: disable=no-member
            return HistoricoModificacoes(
                id=historico_model.id,
                plugin_id=historico_model.plugin_id,
                data_modificacao=historico_model.data_modificacao,
                usuario=historico_model.usuario,
                descricao_modificacao=historico_model.descricao_modificacao
            )
        except HistoricoModificacoesModel.DoesNotExist:
            return None

    def update(self, historico_modificacoes: HistoricoModificacoes) -> None:
        historico_model = HistoricoModificacoesModel.objects.get(pk=historico_modificacoes.id, is_deleted=False)  # pylint: disable=no-member
        historico_model.plugin_id = historico_modificacoes.plugin_id
        historico_model.data_modificacao = historico_modificacoes.data_modificacao
        historico_model.usuario = historico_modificacoes.usuario
        historico_model.descricao_modificacao = historico_modificacoes.(
                                                    descricao_modificacao)
        historico_model.save()

    def delete(self, historico_modificacoes_id: UUID) -> None:
        historico_model = HistoricoModificacoesModel.objects.get(
            pk=historico_modificacoes_id)  # pylint: disable=no-member
        historico_model.is_deleted = True
        historico_model.save()

    def list(self) -> List[HistoricoModificacoes]:
        historico_models = HistoricoModificacoesModel.objects.filter(
            is_deleted=False)  # pylint: disable=no-member
        return [
            HistoricoModificacoes(
                id=historico.id,
                plugin_id=historico.plugin_id,
                data_modificacao=historico.data_modificacao,
                usuario=historico.usuario,
                descricao_modificacao=historico.descricao_modificacao
            )
            for historico in historico_models
        ]
