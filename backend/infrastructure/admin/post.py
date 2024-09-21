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
    As informações são organizadas em seções para facilitar a visualização.
    """
    list_display = ('title', 'slug', 'published_date', 'autor', 'blog', 'status', 'numero_compartilhamentos')
    search_fields = ('title', 'slug', 'autor__primeiro_nome', 'autor__sobrenome', 'blog__title')
    list_filter = ('status', 'published_date', 'blog', 'autor')
    ordering = ('-published_date',)

    fieldsets = (
        ('Informações Gerais', {
            'fields': ('title', 'slug', 'content', 'status')
        }),
        ('Autor e Blog', {
            'fields': ('autor', 'blog')
        }),
        ('Datas', {
            'fields': ('published_date',)
        }),
        ('Relacionamentos', {
            'fields': ('comentarios', 'reacoes')
        }),
        ('Compartilhamento', {
            'fields': ('compartilhado', 'numero_compartilhamentos')
        }),
    )

    # Apenas campos ManyToManyField no filter_horizontal
    filter_horizontal = ('comentarios', 'reacoes')

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form

