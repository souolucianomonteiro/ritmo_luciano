
from domain.blog.repositories.post_reacao import PostReacaoRepository
from domain.blog.repositories.reacao_tipo import ReacaoTipoRepository
from infrastructure.models.post import Post
from django.utils import timezone

class RegistrarReacaoPostUseCase:
    """
    Caso de uso para registrar uma reação a um post. Pode ser realizada por 
    um usuário logado ou um visitante não logado.

    Atributos:
        post_reacao_repository (PostReacaoRepository): Repositório para interagir 
        com o armazenamento de reações de post.
        reacao_tipo_repository (ReacaoTipoRepository): Repositório para buscar tipos de reações.
    """

    def __init__(self, post_reacao_repository: PostReacaoRepository, reacao_tipo_repository: ReacaoTipoRepository):
        self.post_reacao_repository = post_reacao_repository
        self.reacao_tipo_repository = reacao_tipo_repository

    def execute(self, post_id: int, reacao_tipo_id: int, request) -> str:
        """
        Executa o caso de uso de registrar uma reação em um post.

        Parâmetros:
            post_id (int): O ID do post que está recebendo a reação.
            reacao_tipo_id (int): O ID do tipo de reação (curtida, amor, etc.).
            request (HttpRequest): A requisição HTTP, usada para capturar o IP do usuário.

        Retorna:
            str: Mensagem indicando o sucesso do registro da reação.
        """
        # Captura o IP do usuário (para não logados)
        ip_origem = request.META.get('REMOTE_ADDR', '0.0.0.0')

        # Se o usuário estiver logado, pega a referência de pessoa física (opcional)
        usuario_logado = None
        if request.user.is_authenticated:
            usuario_logado = request.user.pessoa_fisica  # Ajustar de acordo com sua estrutura de usuário

        # Buscar o post
        post = Post.objects.get(id=post_id)

        # Buscar o tipo de reação
        reacao_tipo = self.reacao_tipo_repository.get_by_id(reacao_tipo_id)

        # Registrar a reação no post
        self.post_reacao_repository.save(
            post=post,
            reacao_tipo=reacao_tipo,
            ip_origem=ip_origem,
            pessoa_fisica=usuario_logado,  # Será None para não logados
            data_reacao=timezone.now()
        )

        return "Reação registrada com sucesso"
