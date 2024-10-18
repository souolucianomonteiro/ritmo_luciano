"""
Módulo responsável pela definição da model AtividadeEconomicaModel.

Este módulo define a model AtividadeEconomicaModel, que representa uma atividade econômica no sistema.
A model inclui campos para armazenar o código único e a descrição única de cada atividade econômica.

Mixins:
    - AuditMixin: Fornece auditoria para monitoramento de criação e modificação de registros.
    - SoftDeleteMixin: Implementa exclusão lógica dos registros.
    - InactivateMixin: Permite marcar a atividade como inativa.

Classes:
    AtividadeEconomicaModel: Model que representa uma atividade econômica no banco de dados.
"""
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin


class AtividadeEconomicaModel(AuditMixin, SoftDeleteMixin, InactivateMixin, models.Model):
    """
    Model que representa uma Atividade Econômica.

    Atributos:
        atividade_econ_codigo (str): Código da atividade econômica, tamanho máximo de 30 caracteres e único.
        atividade_econ_descricao (str): Descrição da atividade econômica, tamanho máximo de 200 caracteres e único.
    """
    atividade_econ_codigo = models.CharField(max_length=30, unique=True)
    atividade_econ_descricao = models.CharField(max_length=200, unique=True)

    class Meta:
        """
        Metadados da Model AtividadeEconomicaModel.
        """
        app_label = 'infrastructure'
        db_table = 'marketing_atividade_economica'
        verbose_name = 'Atividade Econômica'
        verbose_name_plural = 'Atividades Econômicas'

    def __str__(self):
        return f"{self.atividade_econ_codigo} - {self.atividade_econ_descricao}"
