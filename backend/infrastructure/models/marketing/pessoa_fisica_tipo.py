"""Módulo que implementa a model da relação pessoa física X usuario tipo"""

from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.inactivate import InactivateMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.marketing.usuario_tipo import UsuarioTipoModel


class PessoaFisicaTipoModel( 
                       AuditMixin, InactivateMixin,
                       SoftDeleteMixin, models.Model
                    ):
    """
    Model que representa a associação entre Pessoa Fisica e Usuario Tipo.

    Esta model estabelece a relação de uma pessoa física com os tipos de usuário que ela pode ter
    (por exemplo: autor, editor, administrador). 

    Atributos:
        pessoa_fisica (ForeignKey): Referência à pessoa física.
        usuario_tipo (ForeignKey): Referência ao tipo de usuário.
    """
    
    pessoa_fisica_tipo_id = models.AutoField(primary_key=True) 
    pessoa_fisica_tipo_id = models.ForeignKey(PessoaFisicaModel, on_delete=models.CASCADE)
    usuario_tipo_tipo = models.ForeignKey(UsuarioTipoModel, on_delete=models.CASCADE)

    class Meta:
        """
        Metadados para a model PessoaFisicaTipo.

        Define o comportamento do modelo no Django, incluindo o nome da tabela
        no banco de dados e restrições de unicidade.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_pessoa_fisica_tipo'
        verbose_name = 'Tipo de Usuário da Pessoa Física'
        verbose_name_plural = 'Tipos de Usuário das Pessoas Físicas'
        unique_together = ('pessoa_fisica', 'usuario_tipo')  
        # Garante que a mesma pessoa não tenha o mesmo tipo mais de uma vez.

    def __str__(self):
        return f"PessoaFisicaTipo(pessoa_fisica_tipo_id={self.pessoa_fisica_tipo_id}, pessoa_fisica_id={self.pessoa_fisica}, usuario_tipo_id={self.usuario_tipo})"
