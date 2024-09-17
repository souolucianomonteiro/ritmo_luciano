from django.db import models
from django.contrib.auth.models import Permission
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class PermissaoWebsite(AuditMixin, InactivateMixin, SoftDeleteMixin, StatusMixin, models.Model):
    """
    Model que estende as permissões do Django para sites específicos.

    Cada permissão pode ser associada a um tipo de usuário e a um site 
    específico, permitindo controle granular sobre o que cada usuário pode fazer.

    Atributos:
        permission (ForeignKey): A permissão nativa do Django.
        site (ForeignKey): O site ao qual esta permissão se aplica.
        usuario_tipo (ForeignKey): O tipo de usuário ao qual esta permissão se aplica.
    """

    permission = models.ForeignKey(Permission, on_delete=models.CASCADE, related_name='website_permissions')
    site = models.ForeignKey('CustomSite', on_delete=models.CASCADE, related_name='site_permissions')
    usuario_tipo = models.ForeignKey('UsuarioTipo', on_delete=models.CASCADE, related_name='tipo_permissions')

    class Meta:
        """
        Metadados para a model PermissaoWebsite.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        db_table = 'permissao_website'
        verbose_name = 'Permissão de Website'
        verbose_name_plural = 'Permissões de Website'

    def __str__(self):
        return f"{self.usuario_tipo.nome} - {self.permission.codename} - {self.site.name}"
