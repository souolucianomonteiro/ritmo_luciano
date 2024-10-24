
"""
Configurações de exibição e administração do modelo AtividadeEconomicaModel
no Django Admin.

Este admin organiza os campos do modelo AtividadeEconomicaModel para facilitar a
visualização, pesquisa e edição das atividades econômicas no painel
administrativo do Django. Além disso, implementa a funcionalidade de exclusão
lógica (soft delete), garantindo que os registros não sejam removidos
fisicamente, mas apenas marcados como excluídos.

Listagem:
    list_display: Define os campos visíveis na listagem principal do admin,
    incluindo o status de exclusão lógica (is_deleted) e auditoria
    (deleted_at, deleted_by).
    
    search_fields: Campos que podem ser usados para busca textual.
    
    list_filter: Filtros aplicados para facilitar a pesquisa, incluindo o
    filtro por registros excluídos (is_deleted).

Formulário:
    fieldsets: Agrupa os campos de código e descrição da atividade econômica,
    além de campos de auditoria como is_deleted, deleted_at e deleted_by.
    
    readonly_fields: Define os campos de exclusão lógica e auditoria como
    somente leitura.

Ações:
    restore_selected: Adiciona uma ação para restaurar registros que foram
    excluídos logicamente, permitindo que sejam reintegrados ao sistema.
    
Métodos Sobrescritos:
    delete_model: Sobrescreve o comportamento padrão de exclusão para usar
    soft delete, passando o usuário responsável pela exclusão.
    
    delete_queryset: Sobrescreve a exclusão de múltiplos registros no admin
    para usar soft delete, aplicando a mesma lógica de exclusão lógica.
"""
from django.contrib import admin
from infrastructure.models.marketing.atividade_economica import AtividadeEconomicaModel

@admin.register(AtividadeEconomicaModel)
class AtividadeEconomicaAdmin(admin.ModelAdmin):
    """
    Admin para Atividade Econômica com suporte para soft delete.
    Exibe campos de auditoria e exclusão lógica, permitindo restauração e
    exclusão lógica de registros.
    """

    # Exibe os campos de soft delete na listagem
    list_display = (
        'atividade_econ_codigo', 
        'atividade_econ_descricao',
        'is_deleted',           # Exibe se o registro está excluído
        'deleted_at',           # Exibe a data da exclusão
        'deleted_by'            # Exibe quem excluiu
    )

    # Campos que permitem busca no admin
    search_fields = ('atividade_econ_codigo', 'atividade_econ_descricao')

    # Filtros para facilitar a pesquisa, incluindo is_deleted
    list_filter = ('atividade_econ_codigo', 'is_deleted')

    # Organização dos campos no formulário de edição
    fieldsets = (
        ('Informações da Atividade Econômica', {
            'fields': ('atividade_econ_codigo', 'atividade_econ_descricao')
        }),
        ('Informações de Exclusão', {
            'fields': ('is_deleted', 'deleted_at', 'deleted_by'),
            'classes': ('collapse',)  # Colapsa a seção para não ocupar muito espaço
        }),
    )

    # Campos de auditoria e exclusão lógica como somente leitura
    readonly_fields = ('is_deleted', 'deleted_at', 'deleted_by')

    # Sobrescreve o método de exclusão para usar soft delete
    def delete_model(self, request, obj) -> None:
        """
        Sobrescreve o comportamento de exclusão para usar soft delete.
        """
        obj.delete(user=request.user)

    # Sobrescreve a exclusão em massa para soft delete
    def delete_queryset(self, request, queryset) -> None:
        """
        Sobrescreve a exclusão de múltiplos registros para soft delete.
        """
        for obj in queryset:
            obj.delete(user=request.user)

    # Ação para restaurar registros excluídos logicamente
    actions = ['restore_selected']

    def restore_selected(self, request, queryset) -> None:
        """
        Ação personalizada para restaurar registros excluídos logicamente.
        """
        for obj in queryset:
            obj.restore()
        self.message_user(request, "Registros restaurados com sucesso.")

    # Define a descrição legível da ação para o Django Admin
    restore_selected.short_description = "Restaurar registros selecionados"
