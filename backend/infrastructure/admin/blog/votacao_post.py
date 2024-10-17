from django.contrib import admin
from infrastructure.models.blog.votacao_post import VotacaoPost

@admin.register(VotacaoPost)
class VotacaoPostAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para VotacaoPost.
    Organiza a exibição dos campos em seções no formulário de administração.
    """
    list_display = ('post', 'pessoa_fisica', 'voto', 'data_votacao')
    list_filter = ('post', 'voto', 'data_votacao')
    search_fields = ('post__title', 'pessoa_fisica__primeiro_nome', 'pessoa_fisica__sobrenome')
    readonly_fields = ('data_votacao',)

    fieldsets = (
        ('Informações do Post', {
            'fields': ('post', 'data_votacao')
        }),
        ('Voto', {
            'fields': ('voto',)
        }),
        ('Pessoa Física', {
            'fields': ('pessoa_fisica',)
        }),
    )
