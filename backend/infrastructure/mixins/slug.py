"""
Mixin que adiciona um campo de slug e métodos utilitários relacionados
para um modelo Django.

Este mixin inclui um campo `slug` que é utilizado para gerar URLs amigáveis
com base em outro campo do modelo, como `nome` ou `título`. Ele também
fornece métodos para automaticamente preencher o campo `slug` a partir de
um valor dado e garantir que o slug seja único.

Atributos:
    slug (models.SlugField): Campo de slug que será gerado automaticamente
    com base em um campo específico do modelo.

Métodos:
    save(*args, **kwargs): Sobrescreve o método save do modelo para garantir
    que o campo slug seja gerado e validado antes de salvar o modelo.
    _generate_slug(): Gera o valor do slug baseado em um campo específico
    do modelo e garante sua unicidade.

Exemplo de uso:
    class Artigo(SlugMixin, models.Model):
        titulo = models.CharField(max_length=255)
        conteudo = models.TextField()

        def __str__(self):
            return self.titulo

    # Neste exemplo, o slug será gerado automaticamente a partir do título
    do artigo e será único.
"""
from django.db import models
from django.utils.text import slugify
from .mixin_base import MixinBase


class SlugMixin(MixinBase):
    """
    Mixin que adiciona um campo slug para URLs amigáveis em modelos Django.
    """

    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        """
        Sobrescreve o método save para gerar automaticamente o slug
        se ele não for fornecido, baseado no campo 'nome'.
        """
        # Se o slug ainda não foi definido, cria um com base no campo 'nome'
        if not self.slug:
            self.slug = slugify(self.nome)
        super().save(*args, **kwargs)

    class Meta:
        """
        Metadados para a classe modelo.

        Define que a classe é abstrata, ou seja, não será criada uma tabela
        diretamente para este modelo no banco de dados. Outras classes podem
        herdar este modelo e estender sua funcionalidade.
        """
        abstract = True
