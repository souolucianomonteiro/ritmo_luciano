# pylint: disable=no-member

from domain.website.entities.pessoa_fisica_tipo import PessoaFisicaTipoDomain
from domain.website.repositories.pessoa_fisica_tipo import (
                                PessoaFisicaTipoRepository)
from infrastructure.models.marketing.pessoa_fisica_tipo import PessoaFisicaTipo
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.marketing.usuario_tipo import UsuarioTipo


class DjangoPessoaFisicaTipoRepository(PessoaFisicaTipoRepository):
    """
    Repositório concreto para a entidade PessoaFisicaTipo.
    Interage com as models PessoaFisicaModel, UsuarioTipo e PessoaFisicaTipoModel
    para realizar as operações de persistência.
    """

    def save(self, pessoa_fisica_tipo: PessoaFisicaTipoDomain) -> PessoaFisicaTipoDomain:
        """
        Salva a associação entre uma pessoa física e seus tipos de usuário no banco de dados.
        """
        pessoa_fisica_model = PessoaFisicaModel.objects.get(id=pessoa_fisica_tipo.pessoa_fisica.id)
        usuario_tipo_model = UsuarioTipo.objects.get(id=pessoa_fisica_tipo.usuario_tipo.id)

        pessoa_fisica_tipo_model = PessoaFisicaTipo(
            pessoa_fisica=pessoa_fisica_model,
            usuario_tipo=usuario_tipo_model
        )
        pessoa_fisica_tipo_model.save()

        pessoa_fisica_tipo.id = pessoa_fisica_tipo_model.id
        return pessoa_fisica_tipo

    def get_by_id(self, pessoa_fisica_tipo_id: int) -> PessoaFisicaTipoDomain:
        """
        Retorna a associação entre pessoa física e tipo de usuário com base no ID.
        """
        try:
            pessoa_fisica_tipo_model = PessoaFisicaTipo.objects.get(id=pessoa_fisica_tipo_id)
            return PessoaFisicaTipoDomain(
                id=pessoa_fisica_tipo_model.id,
                pessoa_fisica=PessoaFisicaModel(
                    id=pessoa_fisica_tipo_model.pessoa_fisica.id,
                    primeiro_nome=pessoa_fisica_tipo_model.pessoa_fisica.first_name,
                    sobrenome=pessoa_fisica_tipo_model.pessoa_fisica.last_name,
                    email=pessoa_fisica_tipo_model.pessoa_fisica.email,
                    cpf=pessoa_fisica_tipo_model.pessoa_fisica.cpf,
                    genero=pessoa_fisica_tipo_model.pessoa_fisica.genero
                ),
                usuario_tipo=UsuarioTipo(
                    id=pessoa_fisica_tipo_model.usuario_tipo.id,
                    nome=pessoa_fisica_tipo_model.usuario_tipo.nome,
                    descricao=pessoa_fisica_tipo_model.usuario_tipo.descricao
                )
            )
        except PessoaFisicaTipo.DoesNotExist:
            return None

    def list_all(self) -> list[PessoaFisicaTipoDomain]:
        """
        Lista todas as associações entre pessoa física e tipos de usuário.
        """
        pessoa_fisica_tipos = PessoaFisicaTipo.objects.all()
        return [
            PessoaFisicaTipoDomain(
                id=pessoa_fisica_tipo.id,
                pessoa_fisica=PessoaFisicaModel(
                    id=pessoa_fisica_tipo.pessoa_fisica.id,
                    primeiro_nome=pessoa_fisica_tipo.pessoa_fisica.first_name,
                    sobrenome=pessoa_fisica_tipo.pessoa_fisica.last_name,
                    email=pessoa_fisica_tipo.pessoa_fisica.email,
                    cpf=pessoa_fisica_tipo.pessoa_fisica.cpf,
                    genero=pessoa_fisica_tipo.pessoa_fisica.genero
                ),
                usuario_tipo=UsuarioTipo(
                    id=pessoa_fisica_tipo.usuario_tipo.id,
                    nome=pessoa_fisica_tipo.usuario_tipo.nome,
                    descricao=pessoa_fisica_tipo.usuario_tipo.descricao
                )
            )
            for pessoa_fisica_tipo in pessoa_fisica_tipos
        ]
    
    def delete(self, pessoa_fisica_tipo: PessoaFisicaTipoDomain) -> None:
        """
        Exclui uma associação entre pessoa física e tipo de usuário.
        """
        PessoaFisicaTipo.objects.filter(id=pessoa_fisica_tipo.id).delete()
