from .categoria import CategoriaAdmin
from .tipo_plugin import TipoPluginAdmin
from .artefato_plugin import ArtefatoPluginAdmin
from .plugin import PluginAdmin
from .tag_plugin import TagPluginAdmin
from .dependencia_plugin import DependenciaPluginAdmin
from .historico_modificacoes import HistoricoModificacoesAdmin
from .permissao_plugin import PermissaoPluginAdmin
from .template_plugin import TemplatePluginAdmin

__all__ = [
    'CategoriaAdmin', 'TipoPluginAdmin', 'ArtefatoPluginAdmin', 'PluginAdmin',
    'TagPluginAdmin', 'DependenciaPluginAdmin', 'HistoricoModificacoesAdmin',
    'PermissaoPluginAdmin', 'TemplatePluginAdmin'
]
