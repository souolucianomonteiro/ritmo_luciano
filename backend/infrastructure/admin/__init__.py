from .categoria import CategoriaAdmin
from .tipo_plugin import TipoPluginAdmin
from .artefato_plugin import ArtefatoPluginAdmin
from .plugin import PluginAdmin
from .tag_plugin import TagPluginAdmin
from .dependencia_plugin import DependenciaPluginAdmin
from .historico_modificacoes import HistoricoModificacoesAdmin
from .permissao_plugin import PermissaoPluginAdmin
from .template_plugin import TemplatePluginAdmin
from .site import CustomSiteAdmin
from .subdomínio import SubdominioAdmin
from .blog import BlogAdmin
from .post import PostAdmin
from .categoria_blog import CategoryAdmin
from .tag_post import TagAdmin
from .usuario_tipo import UsuarioTipoAdmin
from .permissao_website import PermissaoWebsiteAdmin

__all__ = [
    'CategoriaAdmin', 'TipoPluginAdmin', 'ArtefatoPluginAdmin', 'PluginAdmin',
    'TagPluginAdmin', 'DependenciaPluginAdmin', 'HistoricoModificacoesAdmin',
    'PermissaoPluginAdmin', 'TemplatePluginAdmin', 'CustomSiteAdmin',
    'SubdominioAdmin', 'BlogAdmin', 'PostAdmin', 'CategoryAdmin', 'TagAdmin',
    'UsuarioTipoAdmin', 'PermissaoWebsiteAdmin'
    ]
