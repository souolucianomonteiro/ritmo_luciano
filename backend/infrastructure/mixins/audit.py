"""
Mixin para auditoria de alterações em models Django.

Este mixin adiciona campos para rastrear a data de criação, a data da última
modificação e os usuários responsáveis pelas operações de criação e alteração
dos registros no banco de dados.
"""

from django.db import models
from django.utils.timezone import now
from django.conf import settings


class AuditMixin(models.Model):
    """
    Mixin que adiciona campos de auditoria para rastreamento de criação e
    modificação de registros, incluindo os usuários responsáveis.

    Atributos:
        created_at (datetime): Armazena a data e hora da criação do registro.
        updated_at (datetime): Armazena a data e hora da última modificação
        do registro.
        created_by (ForeignKey): Referencia o usuário que criou o registro.
        updated_by (ForeignKey): Referencia o usuário que fez a última
        modificação no registro.
    """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='created_%(class)s_set',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='updated_%(class)s_set',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para atualizar o campo updated_at e o
        usuário responsável (updated_by) sempre que o registro for salvo.
        """
        request = kwargs.pop('request', None)
        if request and request.user.is_authenticated:
            if not self.pk:  # Registro está sendo criado
                self.created_by = request.user
            self.updated_by = request.user
        self.updated_at = now()
        super().save(*args, **kwargs)

    class Meta:
        """
        Metadados para a classe modelo.

        Define que a classe é abstrata, ou seja, não será criada uma tabela
        diretamente para este modelo no banco de dados. Outras classes podem
        herdar este modelo e estender sua funcionalidade.
        """
        abstract = True
