"""
Configurações de exibição e administração do modelo Localizacao no Django Admin.

Este admin permite a visualização, busca e administração direta dos registros
de Localizacao, como endereço IP, coordenadas geográficas e outros dados 
relacionados à geolocalização capturada no sistema. 

As funcionalidades incluem:
- Exibição de campos como IP, latitude, longitude, cidade, estado, país e 
  data de captura.
- Filtros e campos de busca para facilitar a navegação e consulta dos dados 
  de geolocalização.
- Ordenação padrão para exibir os registros mais recentes primeiro.

Classes:
    LocalizacaoAdmin: Configurações de exibição e administração de
    LocalizacaoModel.
"""

from django.contrib import admin
from infrastructure.models.shared.resources.localizacao import LocalizacaoModel


@admin.register(LocalizacaoModel)
class LocalizacaoAdmin(admin.ModelAdmin):
    """
    Admin para exibição e administração direta de Localizacoes no Django Admin.
    """
    
    # Campos exibidos na listagem
    list_display = ('ip_address', 'latitude', 'longitude', 'cidade', 'estado', 'pais', 'data_hora_captura')
    
    # Campos de busca
    search_fields = ('ip_address', 'cidade', 'estado', 'pais')
    
    # Filtros para facilitar a navegação
    list_filter = ('cidade', 'estado', 'pais')
    
    # Ordenação padrão
    ordering = ('-data_hora_captura',)
    
    # Campos de leitura somente
    readonly_fields = ('data_hora_captura',)
