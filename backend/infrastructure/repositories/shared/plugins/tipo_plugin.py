# pylint: disable=no-member
"""
Este módulo contém a implementação concreta do repositório para a
entidade TipoPlugin, que lida com operações de CRUD e inclui métodos
específicos para inativar e reativar instâncias da entidade.

Classes:
    TipoPluginRepositoryConcrete: Implementação concreta do repositório
    para a entidade TipoPlugin.

Métodos:
    inativar: Inativa uma instância de TipoPlugin.
    reativar: Reativa uma instância de TipoPlugin.
"""
from typing import List, Optional
from domain.shared.plugins.entities.tipo_plugin import TipoPlugin
from domain.shared.plugins.repositories.tipo_plugin import TipoPluginRepository
from infrastructure.models.shared.plugins.tipo_plugin import TipoPluginModel
from infrastructure.mixins.softdelete import SoftDeleteMixin


class TipoPluginRepositoryConcrete(TipoPluginRepository, SoftDeleteMixin):
    """
    Implementação concreta do repositório para o TipoPlugin com
    suporte a soft delete.

    Métodos:
        obter_todos(): Retorna todos os tipos de plugin não excluídos.
        obter_por_id(tipo_plugin_id: int): Retorna o tipo de plugin
        pelo ID, se não estiver excluído.
        adicionar(tipo_plugin: TipoPlugin): Adiciona um novo tipo de plugin.
        atualizar(tipo_plugin: TipoPlugin): Atualiza um tipo de plugin
        existente.
        remover(tipo_plugin_id: int): Realiza soft delete no tipo de plugin
        pelo ID.
    """

    def obter_todos(self) -> List[TipoPlugin]:
        """Retorna todos os tipos de plugin que não foram excluídos."""
        return TipoPluginModel.objects.filter(deleted_at__isnull=True)

    def obter_por_id(self, tipo_plugin_id: int) -> Optional[TipoPlugin]:
        """Retorna um tipo de plugin pelo ID, se não estiver excluído."""
        return TipoPluginModel.objects.filter(id=tipo_plugin_id,
                                              deleted_at__isnull=True).first()

    def adicionar(self, tipo_plugin: TipoPlugin) -> TipoPlugin:
        """Adiciona um novo tipo de plugin."""
        tipo_plugin_model = TipoPluginModel(
            nome=tipo_plugin.nome,
            # Outros campos aqui, se existirem
        )
        tipo_plugin_model.save()
        return tipo_plugin_model

    def atualizar(self, tipo_plugin: TipoPlugin) -> TipoPlugin:
        """Atualiza um tipo de plugin existente."""
        tipo_plugin_model = TipoPluginModel.objects.get(id=tipo_plugin.id)
        tipo_plugin_model.nome = tipo_plugin.nome
        # Atualizar outros campos, se necessário
        tipo_plugin_model.save()
        return tipo_plugin_model

    def remover(self, tipo_plugin_id: int) -> None:
        """
        Realiza soft delete no tipo de plugin pelo ID.

        Em vez de remover o registro do banco de dados, o campo `deleted_at`
        é atualizado.
        """
        tipo_plugin_model = TipoPluginModel.objects.get(id=tipo_plugin_id)
        tipo_plugin_model.soft_delete()  # Utilizando o SoftDeleteMixin
