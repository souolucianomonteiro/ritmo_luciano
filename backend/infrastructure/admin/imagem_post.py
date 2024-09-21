from django.contrib import admin
from infrastructure.models.imagem_post import ImagemPost

@admin.register(ImagemPost)
class ImagemPostAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para a model ImagemPost.
    Organiza a visualização em seções para melhor apresentação.
    """
    list_display = ['nome_imagem', 'post', 'data_upload']
    search_fields = ['nome_imagem', 'post__title']
    list_filter = ['data_upload', 'post__title']

    fieldsets = (
        ('Informações da Imagem', {
            'fields': ('nome_imagem', 'arquivo_imagem', 'data_upload'),
        }),
        ('Relacionamentos', {
            'fields': ('post',),
        }),
    )
    
    readonly_fields = ['data_upload']
