from django.contrib import admin
from infrastructure.models.blog.reacao_tipo import ReacaoTipo

@admin.register(ReacaoTipo)
class ReacaoTipoAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para ReacaoDetalhe.
    Organiza a exibição dos campos em seções no formulário de administração.
    """
    list_display = ('nome', 'descricao', 'icone')
    search_fields = ('nome', 'descricao', 'icone')
    
    fieldsets = (
        ('Informações da Reação', {
            'fields': ('nome', 'descricao')
        }),
        ('Detalhes do Ícone', {
            'fields': ('icone',)
        }),
    )
