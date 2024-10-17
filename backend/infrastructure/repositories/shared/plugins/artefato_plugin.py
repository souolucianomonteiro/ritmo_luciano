# pylint: disable=no-member:
"""
Módulo que define a implementação concreta do repositório para a entidade
`ArtefatoPlugin` na camada de infraestrutura.

Este módulo contém a classe `ArtefatoPluginRepositoryConcrete`, que provê
os métodos para interação com o banco de dados, permitindo operações de
CRUD (Create, Read, Update, Delete) para a entidade `ArtefatoPlugin`.
"""
from typing import Optional, List
from domain.shared.plugins.repositories.artefato_plugin import (
                                        ArtefatoPluginRepository)
from domain.shared.plugins.entities.artefato_plugin import ArtefatoPluginDomain
from infrastructure.models.shared.plugins.artefato_plugin import ArtefatoPluginModel


class ArtefatoPluginRepositoryConcrete(ArtefatoPluginRepository):
    """
    Implementação concreta do repositório de ArtefatoPlugin.
    Faz a conversão entre o ArtefatoPluginDomain e ArtefatoPluginModel,
    garantindo
    que as operações sejam abstraídas e interajam corretamente com
    o banco de dados.
    """

    def get_by_id(self, artefato_plugin_id: int) -> Optional[
                                        ArtefatoPluginDomain]:
        """
        Busca um ArtefatoPluginDomain pelo seu ID no banco de dados.
        """
        try:
            model = ArtefatoPluginModel.objects.get(id=artefato_plugin_id)
            return self._model_to_domain(model)
        except ArtefatoPluginModel.DoesNotExist:
            return None

    def get_all(self) -> List[ArtefatoPluginDomain]:
        """
        Busca todos os artefatos de plugin no banco de dados.
        """
        models = ArtefatoPluginModel.objects.all()
        return [self._model_to_domain(model) for model in models]

    def save(self, artefato_plugin: ArtefatoPluginDomain) -> ArtefatoPluginDomain:
        """
        Salva ou atualiza um ArtefatoPluginDomain no banco de dados.
        """
        model = self._domain_to_model(artefato_plugin)
        model.save()
        return self._model_to_domain(model)

    def delete(self, artefato_plugin_id: int) -> None:
        """
        Remove um ArtefatoPluginDomain do banco de dados pelo seu ID.
        """
        ArtefatoPluginModel.objects.filter(id=artefato_plugin_id).delete()

    def _model_to_domain(self, model: ArtefatoPluginModel) -> (
                                            ArtefatoPluginDomain):
        """
        Converte um ArtefatoPluginModel para ArtefatoPluginDomain.
        """
        return ArtefatoPluginDomain(
            artefato_plugin_id=model.artefato_plugin_id,
            nome=model.nome,
            descricao=model.descricao,
            versao=model.versao,
            tipo_arquivo=model.tipo_arquivo,
            caminho_arquivo=model.caminho_arquivo,
            criado_em=model.created_at,
            atualizado_em=model.updated_at,
            criado_por=model.created_by,
            atualizado_por=model.updated_by,
            ativo=model.ativo
        )

    def _domain_to_model(self, domain: ArtefatoPluginDomain) -> (
                                                ArtefatoPluginModel):
        """
        Converte um ArtefatoPluginDomain para ArtefatoPluginModel.
        """
        return ArtefatoPluginModel(
            artefato_plugin_id=domain.artefato_plugin_id,
            nome=domain.nome,
            descricao=domain.descricao,
            versao=domain.versao,
            tipo_arquivo=domain.tipo_arquivo,
            caminho_arquivo=domain.caminho_arquivo,
            created_at=domain.criado_em,
            updated_at=domain.atualizado_em,
            created_by=domain.criado_por,
            updated_by=domain.atualizado_por,
            ativo=domain.ativo
        )
