"""
Configurações de exibição e administração de UsuarioTipo no Django Admin.

Esta configuração permite a visualização e gerenciamento dos tipos de usuário no
sistema, incluindo auditoria, ordenação, e inativação.
"""

from django.contrib import admin
from infrastructure.models.marketing.usuario_tipo import UsuarioTipoModel

@admin.register(UsuarioTipoModel)
class UsuarioTipoAdmin(admin.ModelAdmin):
    """
    Admin para gerenciamento de UsuarioTipo no Django Admin.
    """
    
    list_display = ('nome', 'descricao', 'is_active', 'created_at', 'updated_at')
    search_fields = ('nome', 'descricao')
    list_filter = ('is_active',)
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
