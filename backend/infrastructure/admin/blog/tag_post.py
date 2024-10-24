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
from infrastructure.models.blog.tag_post import TagPost

@admin.register(TagPost)
class TagPostAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração da model TagPost no Django Admin.
    """

    list_display = ('name', 'descricao')
    search_fields = ('name', 'descricao')
    ordering = ('name',)

    fieldsets = (
        ('Informações da Tag', {
            'fields': ('name', 'descricao'),
            'description': 'Preencha as informações da tag de postagem.',
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
