"""
Módulo de configuração do Django Admin para a model CategoriaPost.

Este módulo define as configurações de exibição e administração
da model CategoriaPost no Django Admin, incluindo a organização
dos campos em seções, filtros de busca e listagem, além de campos de leitura
somente para datas de criação e atualização.

Classes:
    CategoriaPostAdmin: Classe que define a configuração do Django Admin para a model CategoriaPost.
"""

from django.contrib import admin
from infrastructure.models.categoria_post import CategoriaPost

@admin.register(CategoriaPost)
class CategoriaPostAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo CategoriaPost no Django Admin.
    """

    list_display = ('nome', 'descricao', 'created_at', 'updated_at')
    search_fields = ('nome',)
    list_filter = ('created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações da Categoria', {
            'fields': ('nome', 'descricao')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
