"""
Módulo responsável pela definição da model RedeSocialModel.

Este módulo define a model RedeSocialModel, que armazena as redes sociais
disponíveis no sistema.
"""

from django.db import models


class RedeSocialModel(models.Model):
    """
    Model que representa uma rede social no banco de dados.

    Atributos:
        nome (str): Nome da rede social (ex: LinkedIn, Facebook).
        icone (str): Caminho ou URL do ícone da rede social.
    """
    nome = models.CharField(max_length=50, unique=True)
    icone = models.CharField(max_length=255)  # Pode ser um caminho ou URL de um ícone

    class Meta:
        """
        Metadados da model RedeSocialModel.
        """
        app_label = 'shared'
        db_table = 'shared_rede_social'
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    def __str__(self):
        return f"{self.nome} - Ícone: {self.icone}"
