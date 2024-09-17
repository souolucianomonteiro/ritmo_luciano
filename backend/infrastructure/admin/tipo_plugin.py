"""
Admin da model TipoPlugin.

Este módulo registra a model TipoPlugin no Django Admin, permitindo 
que os dados dessa model sejam gerenciados através da interface de 
administração padrão do Django.
"""

from django.contrib import admin
from infrastructure.models.tipo_plugin import TipoPluginModel

@admin.register(TipoPluginModel)
class TipoPluginAdmin(admin.ModelAdmin):
    """
    Classe administrativa para a model TipoPlugin.

    Esta classe configura como a model TipoPlugin será exibida e
    interagida no Django Admin.
    """

    list_display = ('nome', 'is_active', 'created_at', 'updated_at')
    search_fields = ('nome',)
    list_filter = ('is_active', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    ordering = ('nome',)

    # Organizando os campos em seções
    fieldsets = (
        ('Informações do Tipo de Plugin', {
            'fields': ('nome', 'is_active')
        }),
        ('Informações de Auditoria', {
            'fields': ('created_at', 'updated_at')
        }),
    )
