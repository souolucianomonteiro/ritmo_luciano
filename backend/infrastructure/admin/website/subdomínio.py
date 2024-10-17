"""
Módulo de configuração do Django Admin para a model Subdominio.

Este módulo define as configurações de exibição e administração
da model Subdominio no Django Admin. As configurações incluem a 
organização dos campos em seções, filtros para busca e listagem 
de subdomínios, além de campos de leitura somente para datas de criação.

Classes:
    SubdominioAdmin: Classe que define a configuração do Django Admin para a model Subdominio.
"""
from django.contrib import admin
from infrastructure.models.website.subdominio import Subdominio 

@admin.register(Subdominio)
class SubdominioAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo Subdominio no Django Admin.
    """

    list_display = ('nome', 'site', 'created_at')
    search_fields = ('nome', 'site__name')
    list_filter = ('site',)
    readonly_fields = ('created_at',)

    fieldsets = (
        ('Informações do Subdomínio', {
            'fields': ('nome', 'site')
        }),
        ('Datas', {
            'fields': ('created_at',)
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
