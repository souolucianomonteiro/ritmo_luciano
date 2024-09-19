from django.contrib import admin
from infrastructure.models.pessoa_juridica import PessoaJuridicaModel

@admin.register(PessoaJuridicaModel)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo PessoaJuridicaModel no Django Admin.
    """

    list_display = ('razao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual', 'usuario_titular', 'iniciador_id')
    search_fields = ('razao_social', 'nome_fantasia', 'cnpj', 'usuario_titular__first_name', 'iniciador_id__first_name')
    list_filter = ('usuario_titular', 'iniciador_id')
    ordering = ('razao_social',)

    fieldsets = (
        ('Informações da Empresa', {
            'fields': ('razao_social', 'nome_fantasia', 'cnpj', 'inscricao_estadual')
        }),
        ('Informações do Usuário', {
            'fields': ('usuario_titular', 'iniciador_id')
        }),
        ('Status', {
            'fields': ('is_active', 'is_deleted', 'created_at', 'updated_at')
        }),
    )

    readonly_fields = ('created_at', 'updated_at')

    def get_form(self, request, obj=None, **kwargs):
        """
        Customiza o formulário do admin, se necessário.
        """
        form = super().get_form(request, obj, **kwargs)
        # Lógica adicional pode ser adicionada aqui
        return form
