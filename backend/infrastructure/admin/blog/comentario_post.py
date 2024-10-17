from django.contrib import admin
from infrastructure.models.blog.comentario_post import ComentarioPost

@admin.register(ComentarioPost)
class ComentarioPostAdmin(admin.ModelAdmin):
    """
    Configuração do admin para ComentarioPost, sem o campo autor.
    """
    list_display = ('comentario_resumido', 'post', 'data_comentario', 'status')
    list_filter = ('status', 'data_comentario')
    search_fields = ('comentario', 'post__title')
    readonly_fields = ('data_comentario',)

    fieldsets = (
        (None, {
            'fields': ('post', 'comentario', 'status')
        }),
        ('Informações Adicionais', {
            'fields': ('data_comentario',),
            'classes': ('collapse',),
        }),
    )

    def comentario_resumido(self, obj):
        """
        Retorna uma versão resumida do comentário para exibição na listagem do admin.
        """
        return obj.comentario[:50] + '...' if len(obj.comentario) > 50 else obj.comentario
    comentario_resumido.short_description = 'Comentário'

    def get_status_choices(self, obj=None):
        """
        Retorna as opções de status específicas para esta model no admin.
        """
        return ComentarioPost.STATUS_CHOICES
