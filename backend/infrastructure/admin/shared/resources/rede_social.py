"""
Configurações de exibição e administração de RedeSocial no Django Admin.

Este módulo define a configuração de exibição e administração das redes sociais 
no sistema, permitindo que o administrador gerencie os dados de nome e ícone das 
redes sociais disponíveis. As funcionalidades incluem busca, filtros e listagem 
personalizada das redes sociais.

Classes:
    RedeSocialAdmin: Configurações de exibição e administração da model RedeSocial.
"""

from django.contrib import admin
from infrastructure.models.shared.resources.rede_social import RedeSocialModel

@admin.register(RedeSocialModel)
class RedeSocialAdmin(admin.ModelAdmin):
    """
    Admin para gerenciamento de RedeSocial no Django Admin.
    """
    
    list_display = ('nome', 'icone')
    search_fields = ('nome',)
