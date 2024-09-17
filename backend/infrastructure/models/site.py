"""
Módulo responsável pela definição da model Site.

Este módulo define a model Site, que representa um site no sistema. 
A model inclui campos para armazenar informações sobre o nome, domínio, 
proprietário, status de atividade e datas de criação e modificação. 
Além disso, a model utiliza mixins para fornecer funcionalidades adicionais 
como auditoria, inativação, exclusão lógica e gerenciamento de status.

Classes:
    Site: Model que representa um site com todas as suas funcionalidades e atributos.
"""
# Importações de bibliotecas de terceiros
from django.db import models
from django.contrib.sites.models import Site as DjangoSite
from django.contrib.auth.models import User

# Importações de módulos internos do projeto
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class CustomSite(
                AuditMixin, InactivateMixin, SoftDeleteMixin, StatusMixin,
                DjangoSite
                ):
    """
    Model que estende a classe nativa do Django `Site`.

    Esta model adiciona funcionalidades de auditoria, inativação, exclusão
    lógica,
    e gerenciamento de status à model `Site` nativa do Django. Além disso,
    inclui
    um campo `owner` para associar um usuário proprietário ao site.

    Atributos adicionais:
        owner (ForeignKey): O proprietário do site, relacionado à model User.
    """

    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='sites'
        )

    class Meta:
        """
        Metadados para a model CustomSite.

        Define o nome da tabela no banco de dados para evitar conflitos com
        a tabela nativa.
        """
        db_table = 'custom_site'
        verbose_name = 'Site Personalizado'
        verbose_name_plural = 'Sites Personalizados'

    def __str__(self):
        return str(self.name)

