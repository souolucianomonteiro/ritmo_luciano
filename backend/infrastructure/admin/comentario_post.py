from django.contrib import admin
from infrastructure.models.comentario_post import ComentarioPost

@admin.register(ComentarioPost)
class ComentarioPostAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para ComentarioPost.
    Organiza a exibição dos campos em seções no formulário de administração.
    """
    list_display = ('post', 'autor', 'data_comentario', 'status')
    list_filter = ('status', 'data_comentario', 'post')
    search_fields = ('post__title', 'autor__primeiro_nome', 'autor__sobrenome', 'comentario')
    readonly_fields = ('data_comentario',)

    fieldsets = (
        ('Informações do Post', {
            'fields': ('post', 'comentario')
        }),
        ('Autor', {
            'fields': ('autor',)
        }),
        ('Status e Data do Comentário', {
            'fields': ('status', 'data_comentario')
        }),
    )
