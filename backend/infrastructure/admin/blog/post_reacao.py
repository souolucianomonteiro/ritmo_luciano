from django.contrib import admin
from infrastructure.models.blog.post_reacao import PostReacao

@admin.register(PostReacao)
class PostReacaoAdmin(admin.ModelAdmin):
    """
    Configuração do admin para PostReacao.
    """
    list_display = ('post', 'reacao_tipo', 'ip_origem', 'localizacao', 'data_reacao')
    list_filter = ('reacao_tipo', 'data_reacao', 'localizacao')
    search_fields = ('post__title', 'reacao_tipo', 'ip_origem', 'localizacao')
    readonly_fields = ('data_reacao',)

    fieldsets = (
        (None, {
            'fields': ('post', 'reacao_tipo', 'ip_origem', 'localizacao')
        }),
        ('Informações Adicionais', {
            'fields': ('data_reacao',),
            'classes': ('collapse',),
        }),
    )
