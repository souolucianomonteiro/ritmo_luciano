"""
    Model responsável pela persistência de artefatos de plugins no banco de 
    dados.

    Esta model armazena informações sobre o artefato de um plugin, incluindo 
    o nome, versão, descrição, tipo de arquivo, caminho do arquivo e status de 
    ativação. Os mixins de auditoria, soft delete e inativação são utilizados 
    para fornecer funcionalidades adicionais, como rastreamento de criação e 
    modificação, exclusão lógica e gerenciamento do status de ativação.

    Atributos:
        nome (CharField): Nome do artefato do plugin.
        versao (CharField): Versão do artefato do plugin.
        descricao (TextField): Descrição opcional do artefato.
        tipo_arquivo (CharField): Tipo de arquivo associado ao artefato.
        caminho_arquivo (CharField): Caminho onde o arquivo do artefato está 
        armazenado.
        ativo (BooleanField): Indica se o artefato está ativo ou inativo.
    """
from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.inactivate import InactivateMixin


class ArtefatoPluginModel(AuditMixin, SoftDeleteMixin, InactivateMixin,
                          models.Model):
    """
    Model para a persistência de ArtefatoPlugin no banco de dados.
    Inclui informações sobre o nome, versão, tipo de arquivo, 
    caminho do arquivo, e estado de ativação.
    """

    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    versao = models.CharField(max_length=50)
    tipo_arquivo = models.CharField(max_length=50)
    caminho_arquivo = models.CharField(max_length=500)
    ativo = models.BooleanField(default=True)

    class Meta:
        """
        Metadados para a model Artefato Plugin Model.

        Define o rótulo da aplicação, o nome singular e plural para exibição
        no Django Admin.
        """
        app_label = 'infrastructure'
        app_label = 'infrastructure'
        verbose_name = 'Artefato do Plugin'
        verbose_name_plural = 'Artefatos do Plugin'
        
