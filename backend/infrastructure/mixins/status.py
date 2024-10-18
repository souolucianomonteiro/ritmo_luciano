"""
Módulo que define o mixin StatusMixin para adicionar um campo de status
a modelos Django.

Este módulo contém o mixin `StatusMixin`, que fornece um campo de status
com opções definidas pela classe que herda este mixin.
"""

from django.db import models
from .mixin_base import MixinBase


class StatusMixin(MixinBase):
    """
    Mixin que adiciona um campo de status a um modelo Django.

    Este mixin fornece um campo `status` que pode ser usado para
    rastrear o estado de uma instância do modelo. As opções de status devem
    ser definidas pela classe que herda este mixin.

    Atributos:
        status (models.CharField): Campo de caractere que armazena o status
        da instância do modelo. As opções e o valor padrão são definidos na
        classe filha.
    """

    status = models.CharField(max_length=20, choices=[], default=None, null=True, blank=True)

    class Meta:
        """
        Metadados para a classe modelo.

        Define que a classe é abstrata, o que significa que não será criada
        uma tabela diretamente para este modelo no banco de dados. Outras
        classes podem herdar este modelo e estender sua funcionalidade.

        Além disso, o campo `status` deve ser configurado dinamicamente com
        as opções de status fornecidas pela classe que herda o mixin.
        """
    abstract = True

    def get_status_choices(self):
        """
        Sobrescreva este método na classe que herda o StatusMixin para definir
        as opções de status. Ele deve retornar uma lista de tuplas para o campo
        'choices' de CharField.
        """
        raise NotImplementedError("Defina 'get_status_choices' na sua model para fornecer opções de status.")

    def save(self, *args, **kwargs):
        """
        No momento de salvar a instância, o mixin irá checar se a model filha
        tem opções de status definidas e atribuirá um status padrão se não
        houver um já definido.
        """
        # Obtém as opções de status da classe filha
        status_choices = self.get_status_choices()

        # Atribui as opções de status ao campo 'choices'
        self._meta.get_field('status').choices = status_choices

        # Se o status não foi definido, atribui o primeiro valor como padrão
        if not self.status and status_choices:
            self.status = status_choices[0][0]  # Define o primeiro valor como padrão

        super().save(*args, **kwargs)
