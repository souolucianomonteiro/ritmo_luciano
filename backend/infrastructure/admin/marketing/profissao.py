"""
Configurações de exibição e administração de Profissao no Django Admin.

Esta configuração permite a visualização e gerenciamento das profissões no sistema,
incluindo auditoria, ordenação, e inativação.
"""

from django.contrib import admin
from infrastructure.models.marketing.profissao import ProfissaoModel

@admin.register(ProfissaoModel)
class ProfissaoAdmin(admin.ModelAdmin):
    """
    Admin para gerenciamento de Profissao no Django Admin.
    """
    
    list_display = ('codigo', 'descricao', 'is_active', 'created_at', 'updated_at')
    search_fields = ('codigo', 'descricao')
    list_filter = ('is_active',)
    ordering = ('order',)
    readonly_fields = ('created_at', 'updated_at')
