# backend/infrastructure/models/tag_plugin_model.py

"""
Módulo responsável pela definição da model TagModel.

Este módulo define o modelo de infraestrutura `TagModel`, que representa uma
tag associada a um plugin na aplicação. A classe `TagModel` é utilizada para
persistir as informações de tags no banco de dados, utilizando o Django ORM.

Classes:
    TagModel: Model que representa uma tag associada a um plugin, com todos os
    seus atributos e funcionalidades associadas.
"""
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin


class TagPluginModel(AuditMixin, SoftDeleteMixin, InactivateMixin, models.
                     Model):
    """
    Model de infraestrutura para representar a entidade Tag associada a
    um plugin.

    Atributos:
        nome (str): Nome da tag.
    """

    nome = models.CharField(max_length=50)

    class Meta:
        """
        Metadados do modelo TagPluginModel.

        Define o nome da tabela no banco de dados (`tags_plugin`), além de 
        configurar o nome
        singular e plural das instâncias do modelo para exibição no Django
        Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_tag_plugin'
        verbose_name = 'Tag de Plugin'
        verbose_name_plural = 'Tags de Plugin'
