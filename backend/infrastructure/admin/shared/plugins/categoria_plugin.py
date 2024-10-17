from django.contrib import admin
from infrastructure.models.shared.plugins.categoria_plugin import CategoriaPlugin

@admin.register(CategoriaPlugin)
class CategoriaPluginAdmin(admin.ModelAdmin):
    """
    Configurações de exibição e administração do modelo CategoriaPlugin no Django Admin.
    """

    list_display = ('nome', 'is_active', 'created_at', 'updated_at')
    search_fields = ['nome',]
    list_filter = ('is_active',)
    readonly_fields = ('created_at', 'updated_at')

    fieldsets = (
        ('Informações da Categoria', {
            'fields': ['nome', 'is_active'],
            
        }),
        ('Datas e Auditoria', {
            'fields': ('created_at', 'updated_at'),
        }),
    )

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj, change, **kwargs)
        return form
