"""
Módulo de configuração do Django Admin para a model Blog.

Este módulo define as configurações de exibição e administração
da model Blog no Django Admin, incluindo a organização dos campos
em seções, filtros de busca e listagem, além de campos de leitura
somente para datas de criação e atualização.

Classes:
    BlogAdmin: Classe que define a configuração do Django Admin para a model
    Blog.
"""
from django.contrib import admin
from infrastructure.models.blog import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo Blog no Django Admin.
    """

    list_display = ('title', 'proprietario', 'site', 'is_active', 'created_at', 'updated_at')
    search_fields = ('title', 'proprietario__username', 'site__name')
    list_filter = ('site', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações do Blog', {
            'fields': ('title', 'description', 'proprietario', 'site', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
