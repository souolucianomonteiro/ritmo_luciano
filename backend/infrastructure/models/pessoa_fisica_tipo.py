"""Módulo que implementa a model da relação pessoa física X usuario tipo"""

from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.usuario_tipo import UsuarioTipo


class PessoaFisicaTipoModel(
    AuditMixin, InactivateMixin, SoftDeleteMixin, models.Model
):
    """
    Model que representa a associação entre Pessoa Física e Usuário Tipo.
    Esta model estabelece a relação entre uma pessoa física e os tipos de usuário
    que ela pode ter (ex: autor, editor, administrador).
    
    Atributos:
        pessoa_fisica (ForeignKey): Referência à pessoa física.
        usuario_tipo (ForeignKey): Referência ao tipo de usuário.
        data_criacao (DateTimeField): Data e hora de criação do vínculo.
    """
    
    id = models.AutoField(primary_key=True)  # Campo de chave primária
    pessoa_fisica = models.ForeignKey(PessoaFisicaModel, on_delete=models.CASCADE)  # Chave estrangeira para Pessoa Física
    usuario_tipo = models.ForeignKey(UsuarioTipo, on_delete=models.CASCADE)  # Chave estrangeira para Tipo de Usuário
    data_criacao = models.DateTimeField(auto_now_add=True)  # Registra automaticamente a data de criação do vínculo
    
    class Meta:
        """
        Metadados para a model PessoaFisicaTipo.
        Define o comportamento da model no Django.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_pessoa_fisica_tipo'
        verbose_name = 'Tipo de Usuário da Pessoa Física'
        verbose_name_plural = 'Tipos de Usuário das Pessoas Físicas'
        unique_together = ('pessoa_fisica', 'usuario_tipo')  # Evita duplicações da mesma pessoa com o mesmo tipo de usuário
    
    def __str__(self):
        return f"{self.pessoa_fisica.nome} - {self.usuario_tipo.nome}"
