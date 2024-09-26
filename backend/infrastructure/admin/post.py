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
    Configuração do admin para Post.
    """
    list_display = ('title', 'slug', 'published_date', 'status')
    list_filter = ('status', 'published_date')
    search_fields = ('title', 'slug', 'content')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('published_date',)

    fieldsets = (
        (None, {
            'fields': ('title', 'slug', 'content', 'blog', 'status', 'tags')
        }),
        ('Informações Adicionais', {
            'fields': ('published_date', 'numero_compartilhamentos', 'compartilhado'),
            'classes': ('collapse',),
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
