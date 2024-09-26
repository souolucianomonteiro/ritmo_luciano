"""
Módulo responsável pela configuração do Django Admin.

Este módulo define as classes e os dados que serão exibidos e manipulados
na interface de administração do Django.

Classes:
    EnderecoAdmin: Classe que configura a interface de administração
    de EnderecoModel.
"""
from .categoria_plugin import CategoriaPluginAdmin
from .tipo_plugin import TipoPluginAdmin
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
from .categoria_post import CategoriaPostAdmin
from .tag_post import TagPostAdmin
from .usuario_tipo import UsuarioTipoAdmin
from .permissao_website import PermissaoWebsiteAdmin
from .profissao import ProfissaoAdmin
from .pessoa_fisica import PessoaFisicaAdmin
from .pessoa_juridica import PessoaJuridicaAdmin
from .endereco import EnderecoAdmin
from .visualizacao_post import VisualizacaoPostAdmin
from .comentario_reacao import ComentarioReacaoAdmin
from .votacao_post import VotacaoPost
from .compartilhamento_post import CompartilhamentoPostAdmin
from .comentario_post import ComentarioPostAdmin
from .reacao_tipo import ReacaoTipoAdmin
from .imagem_post import ImagemPostAdmin


__all__ = [
    'CategoriaPluginAdmin', 'TipoPluginAdmin', 'ArtefatoPluginAdmin',
    'PluginAdmin', 'TagPluginAdmin', 'DependenciaPluginAdmin',
    'HistoricoModificacoesAdmin', 'PermissaoPluginAdmin', 
    'TemplatePluginAdmin', 'CustomSiteAdmin', 'SubdominioAdmin', 'BlogAdmin',
    'PostAdmin', 'CategoriaPostAdmin', 'TagPostAdmin', 'UsuarioTipoAdmin',
    'PermissaoWebsiteAdmin', 'ProfissaoAdmin', 'PessoaFisicaAdmin',
    'PessoaJuridicaAdmin', 'EnderecoAdmin', 'VisualizacaoPostAdmin',
    'ComentarioReacaoAdmin', 'VotacaoPost', 'CompartilhamentoPostAdmin',
    'ComentarioPostAdmin', 'ReacaoTipoAdmin', 'ImagemPostAdmin',
    
    ]
