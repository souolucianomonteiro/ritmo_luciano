"""
Módulo de configuração do Django Admin para a model UsuarioTipo.

Este módulo define as configurações de exibição e administração
da model UsuarioTipo no Django Admin, incluindo a organização dos 
campos em seções, filtros de busca e listagem, além de campos 
de leitura somente para datas de criação e atualização.

Classes:
    UsuarioTipoAdmin: Classe que define a configuração do Django Admin para a model UsuarioTipo.
"""
from django.contrib import admin
from infrastructure.models.marketing.usuario_tipo import UsuarioTipo

@admin.register(UsuarioTipo)
class UsuarioTipoAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo UsuarioTipo no Django Admin.
    """

    list_display = ('nome', 'is_active', 'created_at', 'updated_at')
    search_fields = ('nome',)
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações do Tipo de Usuário', {
            'fields': ('nome', 'descricao', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
