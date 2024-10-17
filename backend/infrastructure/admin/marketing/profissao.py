from django.contrib import admin
from infrastructure.models.marketing.profissao import ProfissaoModel

@admin.register(ProfissaoModel)
class ProfissaoAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo ProfissaoModel no Django Admin.
    Organiza os campos da profissão em seções no formulário.
    """
    
    list_display = ('codigo', 'descricao')
    search_fields = ('codigo', 'descricao')
    list_filter = ('codigo',)
    ordering = ('codigo',)

    fieldsets = (
        ('Informações Básicas', {
            'fields': ('codigo', 'descricao'),
            'description': 'Preencha as informações básicas da profissão, incluindo código e descrição.',
        }),
    )
