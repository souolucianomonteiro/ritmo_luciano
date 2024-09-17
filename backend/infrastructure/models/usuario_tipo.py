from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin

class UsuarioTipo(AuditMixin, InactivateMixin, SoftDeleteMixin, StatusMixin, models.Model):
    """
    Model que representa o tipo de usuário no sistema.

    Cada tipo de usuário pode estar associado a diferentes permissões 
    dentro de um site específico, permitindo controle granular de acesso.

    Atributos:
        nome (CharField): O nome do tipo de usuário (ex: Administrador, Editor).
        descricao (TextField): Uma breve descrição do tipo de usuário.
    """

    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(null=True, blank=True)

    class Meta:
        """
        Metadados para a model UsuarioTipo.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        db_table = 'usuario_tipo'
        verbose_name = 'Tipo de Usuário'
        verbose_name_plural = 'Tipos de Usuário'

    def __str__(self):
        return self.nome
