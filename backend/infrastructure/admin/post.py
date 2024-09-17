"""
Módulo de configuração do Django Admin para a model Post.

Este módulo define as configurações de exibição e administração
da model Post no Django Admin. As configurações incluem organização 
dos campos em seções, filtros para busca e listagem de postagens, 
além de campos de leitura somente para datas de criação e atualização.

Classes:
    PostAdmin: Classe que define a configuração do Django Admin para a model Post.
"""
from django.contrib import admin
from infrastructure.models.post import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo Post no Django Admin.
    """

    list_display = ('title', 'author', 'blog', 'published_date', 'is_active')
    search_fields = ('title', 'author__username', 'blog__title')
    list_filter = ('blog', 'is_active', 'published_date')
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações da Postagem', {
            'fields': ('title', 'slug', 'content', 'author', 'blog', 'is_active')
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at', 'published_date')
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
