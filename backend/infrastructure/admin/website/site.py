"""
Módulo de configuração do Django Admin para a model CustomSite.

Este módulo define as configurações de exibição e administração
da model CustomSite no Django Admin, incluindo a organização dos 
campos em seções, filtros de busca e listagem, além de campos 
de leitura somente para datas de criação e atualização.

Classes:
    CustomSiteAdmin: Classe que define a configuração do Django Admin para a model CustomSite.
"""
from django.contrib import admin
from infrastructure.models.website.site import CustomSite

@admin.register(CustomSite)
class CustomSiteAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo CustomSite no Django Admin.
    """

    list_display = ('name', 'domain', 'owner', 'is_active', 'created_at', 'updated_at')
    search_fields = ('name', 'domain', 'owner__username')
    list_filter = ('is_active', 'owner')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações do Site', {
            'fields': ('name', 'domain', 'owner', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
