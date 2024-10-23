"""Implementa a model do conceito produto """

import uuid
from django.db import models
from infrastructure.models.marketing.produto_tipo import TipoProdutoModel


class ProdutoModel(models.Model):
    """
    Model para o Produto.

    Atributos:
        id (UUID): Identificador único.
        nome (str): Nome do produto.
        descricao (str): Descrição do produto.
        tipo_produto (ForeignKey): Referência ao Tipo de Produto.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=255)
    descricao = models.TextField(null=True, blank=True)
    tipo_produto = models.ForeignKey(TipoProdutoModel, on_delete=models.PROTECT, related_name='produtos')

    def __str__(self):
        return str(self.nome)
