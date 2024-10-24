
"""
Mixin para auditoria de alterações em models Django.

Este mixin adiciona campos para rastrear a data de criação, a data da última
modificação e os usuários responsáveis pelas operações de criação e alteração
dos registros no banco de dados.
"""
from django.db import models
from django.conf import settings
from infrastructure.mixins.mixin_base import MixinBase


class AuditMixin(MixinBase):
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
        Sobrescreve o método save para registrar o usuário que criou ou 
        atualizou o registro. O usuário deve ser passado nos kwargs.

        Args:
            user (User): O usuário autenticado que está criando ou atualizando 
            o registro.
        """
        user = kwargs.pop('user', None)  # Obtém o usuário autenticado dos kwargs
        if user and user.is_authenticated:
            if not self.pk:  # Registro está sendo criado pela primeira vez
                self.created_by = user  # Registra quem criou
            self.updated_by = user  # Atualiza quem fez a última modificação

        super().save(*args, **kwargs)  # Chama o save da classe pai

    class Meta:
        abstract = True  # Define que este é um mixin abstrato
