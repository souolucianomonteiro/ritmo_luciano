# backend/infrastructure/repositories/dependencia_repository.py
# pylint: disable=no-member


from uuid import UUID
from typing import List, Optional
from domain.shared.plugins.entities.dependencia_plugin import Dependencia
from domain.shared.plugins.repositories.dependencia_plugin import (
                                                DependenciaRepository)
from infrastructure.models.shared.plugins.dependencia_plugin import DependenciaModel


class DjangoDependenciaRepository(DependenciaRepository):
    """
    Implementação concreta do repositório de Dependências utilizando o Django ORM.
    """

    def add(self, dependencia: Dependencia) -> None:
        DependenciaModel.objects.create(
            plugin_id=dependencia.plugin_id,
            tipo_dependencia=dependencia.tipo_dependencia,
            dependencia_plugin_id=dependencia.dependencia_plugin_id,
            nome_dependencia=dependencia.nome_dependencia,
            url_dependencia=dependencia.url_dependencia
        )

    def get(self, dependencia_id: UUID) -> Optional[Dependencia]:
        try:
            dependencia_model = DependenciaModel.objects.get(pk=dependencia_id,
                                                             is_deleted=False) # pylint: disable=no-member
            return Dependencia(
                id=dependencia_model.id,
                plugin_id=dependencia_model.plugin_id,
                tipo_dependencia=dependencia_model.tipo_dependencia,
                dependencia_plugin_id=dependencia_model.dependencia_plugin_id,
                nome_dependencia=dependencia_model.nome_dependencia,
                url_dependencia=dependencia_model.url_dependencia
            )
        except DependenciaModel.DoesNotExist:
            return None

    def update(self, dependencia: Dependencia) -> None:
        dependencia_model = DependenciaModel.objects.get(pk=dependencia.id, 
                                                         is_deleted=False)  # pylint: disable=no-member
        dependencia_model.plugin_id = dependencia.plugin_id
        dependencia_model.tipo_dependencia = dependencia.tipo_dependencia
        dependencia_model.dependencia_plugin_id = (
                dependencia.dependencia_plugin_id)
        dependencia_model.nome_dependencia = dependencia.nome_dependencia
        dependencia_model.url_dependencia = dependencia.url_dependencia
        dependencia_model.save()

    def delete(self, dependencia_id: UUID) -> None:
        dependencia_model = DependenciaModel.objects.get(pk=dependencia_id)  # pylint: disable=no-member
        dependencia_model.is_deleted = True
        dependencia_model.save()

    def list(self) -> List[Dependencia]:
        dependencia_models = DependenciaModel.objects.filter(is_deleted=False)  # pylint: disable=no-member
        return [
            Dependencia(
                id=dependencia.id,
                plugin_id=dependencia.plugin_id,
                tipo_dependencia=dependencia.tipo_dependencia,
                dependencia_plugin_id=dependencia.dependencia_plugin_id,
                nome_dependencia=dependencia.nome_dependencia,
                url_dependencia=dependencia.url_dependencia
            )
            for dependencia in dependencia_models
        ]

    def list_by_tipo(self, tipo_dependencia: str) -> List[Dependencia]:
        dependencia_models = DependenciaModel.objects.filter(
            tipo_dependencia=tipo_dependencia, is_deleted=False)  # pylint: disable=no-member
        return [
            Dependencia(
                id=dependencia.id,
                plugin_id=dependencia.plugin_id,
                tipo_dependencia=dependencia.tipo_dependencia,
                dependencia_plugin_id=dependencia.dependencia_plugin_id,
                nome_dependencia=dependencia.nome_dependencia,
                url_dependencia=dependencia.url_dependencia
            )
            for dependencia in dependencia_models
        ]
