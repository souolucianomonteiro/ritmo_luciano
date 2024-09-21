"""
Módulo que define o mixin StatusMixin para adicionar um campo de status
a modelos Django.

Este módulo contém o mixin `StatusMixin`, que fornece um campo de status
com opções
definidas e uma implementação padrão para ser utilizado em qualquer modelo
Django.

Classes:
    StatusMixin: Mixin que adiciona um campo de status a um modelo Django.
"""

from django.db import models
from .mixin_base import MixinBase


class StatusMixin(MixinBase):
    """
    Mixin que adiciona um campo de status a um modelo Django.

    Este mixin fornece um campo `status` que pode ser usado para
    rastrear o estado de uma instância do modelo. Ele oferece uma lista 
    de escolhas padrão para o campo, incluindo 'active', 'inactive', 
    'pending' e 'completed'. O valor padrão é 'active'.

    Atributos:
        STATUS_CHOICES (list): Lista de tuplas que define as opções
        disponíveis para o campo `status`.
        status (models.CharField): Campo de caractere que armazena o status
        da instância do modelo.

    Métodos:
        save(*args, **kwargs): (Herdado de models.Model) Salva a instância
        atual do modelo, aplicando validações e gerenciando a lógica do status.
    """

    status = models.CharField(max_length=20, choices=[], default=None, null=True, blank=True)

    class Meta:
        abstract = True

    def get_status_choices(self):
        """
        Sobrescreva este método na classe que herda o StatusMixin para definir as opções de status.
        """
        raise NotImplementedError("Defina 'get_status_choices' na sua model para fornecer opções de status.")

    def save(self, *args, **kwargs):
        """
        No momento de salvar a instância, o mixin irá checar se a model filha tem opções de status definidas.
        """
        if not self.status:
            # Checa se o status foi fornecido, senão aplica o primeiro valor disponível.
            status_choices = self.get_status_choices()
            if status_choices:
                self.status = status_choices[0][0]  # Aplica o primeiro valor da tupla de choices
        super().save(*args, **kwargs)
