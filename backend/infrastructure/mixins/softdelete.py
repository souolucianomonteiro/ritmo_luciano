"""
Mixin para implementar soft delete e auditoria de exclusões em models Django.

Este mixin adiciona funcionalidade de exclusão lógica aos modelos, permitindo
marcar registros como excluídos sem removê-los fisicamente do banco de dados.
Além disso, registra o usuário que realizou a exclusão e a data e hora da
operação. Também permite restaurar registros previamente excluídos.

Classes:
    SoftDeleteMixin: Mixin que implementa a exclusão lógica e auditoria de
    exclusões, adicionando os campos is_deleted, deleted_at e deleted_by.

Atributos:
    is_deleted (bool): Indica se o registro foi marcado como excluído.
    deleted_at (datetime): Armazena a data e hora da exclusão lógica do
    registro.
    deleted_by (ForeignKey): Referencia o usuário que realizou a exclusão
    lógica.

Métodos:
    delete(user=None): Realiza a exclusão lógica, marcando o registro como
    excluído,
    preenchendo os campos is_deleted, deleted_at e deleted_by.
    
    restore(): Restaura um registro que foi excluído logicamente, revertendo os
    campos is_deleted, deleted_at e deleted_by.
"""
from django.db import models
from django.utils.timezone import now
from django.contrib.auth import get_user_model
from .mixin_base import MixinBase
from .manager import SoftDeleteManager

User = get_user_model()  # Obtém o modelo de usuário correto (padrão ou personalizado)


class SoftDeleteMixin(MixinBase):
    """
    Mixin que adiciona a funcionalidade de exclusão lógica (soft delete) para
    modelos Django. Em vez de excluir registros do banco de dados, esta
    abordagem marca os registros como inativos.

    Atributos:
        is_deleted (bool): Indica se o registro foi marcado como excluído.
        deleted_at (datetime): Armazena a data e hora da exclusão lógica do
        registro.
        deleted_by (ForeignKey): Referencia o usuário que realizou a exclusão
        lógica.
    """

    is_deleted = models.BooleanField(default=False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.ForeignKey(
        User,  # Obtém o modelo de usuário diretamente
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='deleted_%(class)s_set'
    )

    objects = SoftDeleteManager()

    def delete(self, using=None, keep_parents=False, user=None):
        """
        Sobrescreve o método delete padrão para realizar uma exclusão lógica,
        marcando o registro como excluído, armazenando a data e hora da
        exclusão e o usuário responsável pela exclusão.

        Args:
            user: O usuário autenticado que está realizando a exclusão.
        """
        self.is_deleted = True
        self.deleted_at = now()
        if user and getattr(user, 'is_authenticated', False):  # Verifica se o usuário está autenticado
            self.deleted_by = user
        self.save()

    def restore(self):
        """
        Método para restaurar um registro que foi excluído logicamente,
        revertendo os campos is_deleted, deleted_at e deleted_by.
        """
        self.is_deleted = False
        self.deleted_at = None
        self.deleted_by = None  # Limpa o campo deleted_by na restauração
        self.save()

    class Meta:
        abstract = True
