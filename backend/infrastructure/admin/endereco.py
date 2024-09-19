from django.contrib import admin
from infrastructure.models.endereco import EnderecoModel

@admin.register(EnderecoModel)
class EnderecoAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo EnderecoModel no Django Admin.
    Organiza os campos em seções para facilitar a visualização.
    """
    
    list_display = ('rua', 'numero', 'bairro', 'cidade', 'estado', 'pais', 'tipo', 'is_active')
    search_fields = ('rua', 'bairro', 'cidade', 'estado', 'cep', 'pais')
    list_filter = ('cidade', 'estado', 'pais', 'tipo', 'is_active')
    
    fieldsets = (
        ('Endereço', {
            'fields': ('rua', 'numero', 'complemento', 'bairro', 'cidade', 'estado', 'cep', 'pais')
        }),
        ('Tipo de Endereço', {
            'fields': ('tipo',)
        }),
        ('Associações', {
            'fields': ('pessoa_fisica', 'pessoa_juridica')
        }),
        ('Status', {
            'fields': ('is_active', 'data_inicio', 'data_fim')
        }),
    )
    
    ordering = ('rua', 'numero')
    readonly_fields = ('data_inicio',)
