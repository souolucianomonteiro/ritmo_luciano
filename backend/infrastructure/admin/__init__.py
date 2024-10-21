"""
Módulo responsável pela configuração do Django Admin.

Este módulo define as classes e os dados que serão exibidos e manipulados
na interface de administração do Django.

Classes:
    EnderecoAdmin: Classe que configura a interface de administração
    de EnderecoModel.
"""
from .shared.plugins.categoria_plugin import CategoriaPluginAdmin
from .shared.plugins.tipo_plugin import TipoPluginAdmin
from .shared.plugins.artefato_plugin import ArtefatoPluginAdmin
from .shared.plugins.plugin import PluginAdmin
from .shared.plugins.tag_plugin import TagPluginAdmin
from .shared.plugins.dependencia_plugin import DependenciaPluginAdmin
from .shared.plugins.historico_modificacoes import HistoricoModificacoesAdmin
from .shared.plugins.permissao_plugin import PermissaoPluginAdmin
from .shared.plugins.template_plugin import TemplatePluginAdmin
from .shared.resources.localizacao import LocalizacaoAdmin
from .website.site import CustomSiteAdmin
from .website.subdomínio import SubdominioAdmin
from .blog.post import PostAdmin
from .blog.categoria_post import CategoriaPostAdmin
from .blog.tag_post import TagPostAdmin
from .marketing.usuario_tipo import UsuarioTipoAdmin
from .website.permissao_website import PermissaoWebsiteAdmin
from .marketing.profissao import ProfissaoAdmin
from .marketing.pessoa_fisica import PessoaFisicaAdmin
from .marketing.pessoa_juridica import PessoaJuridicaAdmin
from .marketing.endereco import EnderecoAdmin
from .blog.visualizacao_post import VisualizacaoPostAdmin
from .blog.comentario_reacao import ComentarioReacaoAdmin
from .blog.votacao_post import VotacaoPost
from .blog.compartilhamento_post import CompartilhamentoPostAdmin
from .blog.comentario_post import ComentarioPostAdmin
from .blog.reacao_tipo import ReacaoTipoAdmin
from .blog.imagem_post import ImagemPostAdmin


__all__ = [
    'CategoriaPluginAdmin', 'TipoPluginAdmin', 'ArtefatoPluginAdmin',
    'PluginAdmin', 'TagPluginAdmin', 'DependenciaPluginAdmin',
    'HistoricoModificacoesAdmin', 'PermissaoPluginAdmin', 'TemplatePluginAdmin', 'CustomSiteAdmin', 'SubdominioAdmin', 'BlogAdmin', 'PostAdmin',
    'CategoriaPostAdmin', 'TagPostAdmin', 'UsuarioTipoAdmin',
    'PermissaoWebsiteAdmin', 'ProfissaoAdmin', 'PessoaFisicaAdmin',
    'PessoaJuridicaAdmin', 'EnderecoAdmin', 'VisualizacaoPostAdmin',
    'ComentarioReacaoAdmin', 'VotacaoPost', 'CompartilhamentoPostAdmin',
    'ComentarioPostAdmin', 'ReacaoTipoAdmin', 'ImagemPostAdmin',
    'LocalizacaoAdmin'
   
    ]
