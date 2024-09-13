"""
Este módulo define a entidade TipoPluginModel, que representa os diferentes
tipos de plugins disponíveis no sistema. A entidade utiliza mixins para
auditoria e gerenciamento de inatividade, garantindo que cada tipo de plugin
seja registrado com informações completas de criação, modificação e status.
"""
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin


class TipoPluginModel(AuditMixin, InactivateMixin, models.Model):
    """
    Entidade que representa o Tipo de Plugin. Cada tipo de plugin tem um nome
    único e é registrado com informações de auditoria e um status de
    inatividade.

    Atributos:
        nome (str): Nome do tipo de plugin, que deve ser único.
    """

    nome = models.CharField(max_length=100, unique=True)

    class Meta:
        """
        Metadados para a model TipoPluginModel.

        Define o rótulo da aplicação, o nome singular e plural para exibição
        no Django Admin.
        """
        app_label = 'infrastructure'
        verbose_name = 'Tipo de Plugin'
        verbose_name_plural = 'Tipos de Plugin'

    def __str__(self):
        """
        Retorna a representação em string do Tipo de Plugin, que é o nome.
        """
        return str(self.nome)
