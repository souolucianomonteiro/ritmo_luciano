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
    usuario_tipo_id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255, unique=True)
    descricao = models.TextField(null=True, blank=True)

    STATUS_CHOICES = [
        ('ativo', 'Ativo'),
        ('inativo', 'Inativo'),
    ]

    def get_status_choices(self):
        return self.STATUS_CHOICES

    class Meta:
        """
        Metadados para a model UsuarioTipo.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_usuario_tipo'
        verbose_name = 'Tipo de Usuário'
        verbose_name_plural = 'Tipos de Usuário'

    def __str__(self):
        return str(self.nome)
