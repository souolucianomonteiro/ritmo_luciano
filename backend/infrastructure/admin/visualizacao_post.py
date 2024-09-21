from django.contrib import admin
from infrastructure.models.visualizacao_post import VisualizacaoPost

@admin.register(VisualizacaoPost)
class VisualizacaoPostAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para VisualizacaoPost.
    Organiza a exibição dos campos em seções no formulário de administração.
    """
    list_display = ('post', 'localizacao', 'pessoa_fisica', 'data_visualizacao')
    list_filter = ('post', 'data_visualizacao')
    search_fields = ('post__title', 'pessoa_fisica__primeiro_nome', 'pessoa_fisica__sobrenome')
    readonly_fields = ('data_visualizacao',)

    fieldsets = (
        ('Informações do Post', {
            'fields': ('post', 'data_visualizacao')
        }),
        ('Localização', {
            'fields': ('localizacao',)
        }),
        ('Pessoa Física', {
            'fields': ('pessoa_fisica',)
        }),
    )
