""""Módulo que implementa a model produto_tipo"""

from django.db import models
from infrastructure.mixins.audit import AuditMixin
from infrastructure.mixins.softdelete import SoftDeleteMixin
from infrastructure.mixins.status import StatusMixin


class TipoProdutoModel(AuditMixin, SoftDeleteMixin, StatusMixin, models.Model):
    """
    Model que representa o Tipo de Produto no banco de dados.

    Atributos:
        nome (str): Nome do tipo de produto.
        descricao (str): Descrição do tipo de produto.
        situacao (str): Situação atual do tipo de produto, gerenciada pelo
        StatusMixin.
    """

    STATUS_CHOICES = [
        ('criado', 'Criado'),
        ('em_desenvolvimento', 'Em Desenvolvimento'),
        ('ativo', 'Ativo'),
        ('em_manutencao', 'Em Manutenção'),
        ('inativo', 'Inativo')
    ]

    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)

    # Campo situacao com choices para gerenciar os status do tipo de produto
    situacao = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='criado'
    )

    def get_status_choices(self):
        """
        Retorna as opções de status disponíveis para o tipo de produto.
        """
        return self.STATUS_CHOICES

    class Meta:
        """
        Metadados da model TipoProdutoModel.

        Define o nome da tabela no banco de dados e nomes amigáveis para
        exibição.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_tipo_produto'
        verbose_name = 'Tipo de Produto'
        verbose_name_plural = 'Tipos de Produtos'

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de TipoProdutoModel.

        Returns:
            str: Representação textual do tipo de produto.
        """
        return f"TipoProduto: {self.nome}, Situação:{self.get_situacao_display()}"


