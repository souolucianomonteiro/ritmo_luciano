from django.contrib import admin
from infrastructure.models.blog.compartilhamento_post import CompartilhamentoPost

@admin.register(CompartilhamentoPost)
class CompartilhamentoPostAdmin(admin.ModelAdmin):
    """
    Configuração do Django Admin para CompartilhamentoPost.
    Organiza a exibição dos campos em seções no formulário de administração.
    """
    list_display = ('post', 'pessoa_fisica', 'data_compartilhamento', 'total_compartilhamentos')
    list_filter = ('post', 'data_compartilhamento')
    search_fields = ('post__title', 'pessoa_fisica__primeiro_nome', 'pessoa_fisica__sobrenome')
    readonly_fields = ('data_compartilhamento', 'total_compartilhamentos')

    fieldsets = (
        ('Informações do Post', {
            'fields': ('post', 'data_compartilhamento')
        }),
        ('Pessoa Física', {
            'fields': ('pessoa_fisica',)
        }),
        ('Total de Compartilhamentos', {
            'fields': ('total_compartilhamentos',)
        }),
    )
