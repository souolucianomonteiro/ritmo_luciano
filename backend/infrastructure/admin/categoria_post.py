"""
Módulo de configuração do Django Admin para a model Category.

Este módulo define as configurações de exibição e administração
da model Category no Django Admin, incluindo a organização dos 
campos em seções, filtros de busca e listagem, além de campos 
de leitura somente para datas de criação e atualização.

Classes:
    CategoryAdmin: Classe que define a configuração do Django Admin para a model Category.
"""
from django.contrib import admin
from infrastructure.models.categoria_post import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo Category no Django Admin.
    """

    list_display = ('name', 'blog', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'blog__title')
    list_filter = ('blog', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações da Categoria', {
            'fields': ('name', 'slug', 'blog', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
