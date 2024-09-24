from django.contrib import admin
from infrastructure.models.comentario_reacao import ComentarioReacaoModel

@admin.register(ComentarioReacaoModel)
class ComentarioReacaoAdmin(admin.ModelAdmin):
    """
    Configuração do admin para ReacaoComentario.
    """
    list_display = ('reacao_tipo', 'data_reacao', 'ip_origem', 'localizacao')
    list_filter = ('reacao_tipo', 'data_reacao', 'localizacao')
    search_fields = ('reacao_tipo', 'ip_origem', 'localizacao')
    readonly_fields = ('data_reacao',)

    fieldsets = (
        (None, {
            'fields': ('reacao_tipo', 'ip_origem', 'localizacao', 'data_reacao')
        }),
    )
