"""
Módulo de configuração do Django Admin para a model Tag.

Este módulo define as configurações de exibição e administração
da model Tag no Django Admin. As configurações incluem a organização 
dos campos em seções, filtros para busca e listagem de tags, além de 
campos de leitura somente para datas de criação e atualização.

Classes:
    TagAdmin: Classe que define a configuração do Django Admin para a model Tag.
"""
from django.contrib import admin
from infrastructure.models.tag_post import Tag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo Tag no Django Admin.
    """

    list_display = ('name', 'blog', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'blog__title')
    list_filter = ('blog', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações da Tag', {
            'fields': ('name', 'blog', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
