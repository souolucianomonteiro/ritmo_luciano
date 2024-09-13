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


class StatusMixin(models.Model):
    """
    Mixin que adiciona um campo de status a um modelo Django.

    Este mixin fornece um campo `status` que pode ser usado para
    rastrear o estado
    de uma instância do modelo. Ele oferece uma lista de escolhas padrão
    para o campo,
    incluindo 'active', 'inactive', 'pending' e 'completed'. O valor padrão
    é 'active'.

    Atributos:
        STATUS_CHOICES (list): Lista de tuplas que define as opções
        disponíveis para o campo `status`.
        status (models.CharField): Campo de caractere que armazena o status
        da instância do modelo.

    Métodos:
        save(*args, **kwargs): (Herdado de models.Model) Salva a instância
        atual do modelo,
        aplicando validações e gerenciando a lógica do status.
    """

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]

    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES, default='active')

    class Meta:
        """
        Classe Meta para definir que este é um modelo abstrato.

        Atributos:
            abstract (bool): Define que esta classe não será utilizada
            para criar tabelas no banco de dados.
        """
        abstract = True
