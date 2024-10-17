"""
Módulo de configuração do Django Admin para a model PermissaoWebsite.

Este módulo define as configurações de exibição e administração
da model PermissaoWebsite no Django Admin, incluindo a organização 
dos campos em seções, filtros de busca e listagem, além de campos 
de leitura somente para datas de criação e atualização.

Classes:
    PermissaoWebsiteAdmin: Classe que define a configuração do Django Admin
    para a model PermissaoWebsite.
"""
from django.contrib import admin
from infrastructure.models.website.permissao_website import PermissaoWebsite

@admin.register(PermissaoWebsite)
class PermissaoWebsiteAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PermissaoWebsite no Django Admin.
    """

    list_display = ('usuario_tipo', 'permission', 'site', 'is_active', 'created_at', 'updated_at')
    search_fields = ('usuario_tipo__nome', 'permission__codename', 'site__name')
    list_filter = ('site', 'usuario_tipo', 'is_active')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações da Permissão', {
            'fields': ('usuario_tipo', 'permission', 'site', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
