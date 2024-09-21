from django.contrib import admin
from infrastructure.models.reacao_comentario import ReacaoComentario

@admin.register(ReacaoComentario)
class ReacaoComentarioAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para ReacaoComentario.
    Organiza a exibição dos campos em seções no formulário de administração.
    """
    list_display = ('comentario_post', 'pessoa_fisica', 'reacao', 'data_reacao')
    list_filter = ('comentario_post', 'reacao', 'data_reacao')
    search_fields = ('comentario_post__comentario', 'pessoa_fisica__primeiro_nome', 'pessoa_fisica__sobrenome')
    readonly_fields = ('data_reacao',)

    fieldsets = (
        ('Comentário', {
            'fields': ('comentario_post', 'data_reacao')
        }),
        ('Reação', {
            'fields': ('reacao',)
        }),
        ('Pessoa Física', {
            'fields': ('pessoa_fisica',)
        }),
    )
