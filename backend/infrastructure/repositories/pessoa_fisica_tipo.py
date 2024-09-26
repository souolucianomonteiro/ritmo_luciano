# pylint: disable=no-member

"""
Repositório concreto para a entidade PessoaFisicaTipoDomain.

Este repositório implementa os métodos definidos no repositório abstrato,
utilizando o Django ORM para manipular a persistência de dados da model
PessoaFisicaTipoModel.
"""
from typing import Optional, List
from domain.marketing.entities.pessoa_fisica_tipo import PessoaFisicaTipoDomain
from domain.marketing.repositories.pessoa_fisica_tipo import (
                                        PessoaFisicaTipoRepository)
from infrastructure.models.pessoa_fisica_tipo import PessoaFisicaTipoModel
from infrastructure.repositories.pessoa_fisica import (
                            PessoaFisicaRepositoryConcrete)
from infrastructure.repositories.usuario_tipo import (
                    DjangoUsuarioTipoRepositoryConcrete)


class DjangoPessoaFisicaTipoRepository(PessoaFisicaTipoRepository):
    """
    Repositório concreto para a entidade PessoaFisicaTipoDomain.
    """

    def __init__(self, pessoa_fisica_repo: PessoaFisicaRepositoryConcrete, usuario_tipo_repo: DjangoUsuarioTipoRepositoryConcrete):
        self.pessoa_fisica_repo = pessoa_fisica_repo
        self.usuario_tipo_repo = usuario_tipo_repo

    def get_by_id(self, pessoa_fisica_tipo_id: int) -> Optional[PessoaFisicaTipoDomain]:
        """
        Busca uma associação PessoaFisicaTipo pelo seu ID.
        """
        try:
            model = PessoaFisicaTipoModel.objects.get(id=pessoa_fisica_tipo_id)
            return self._model_to_domain(model)
        except PessoaFisicaTipoModel.DoesNotExist:
            return None

    def list_all(self) -> List[PessoaFisicaTipoDomain]:
        """
        Retorna todas as associações entre Pessoa Física e Tipos de Usuário.
        """
        models = PessoaFisicaTipoModel.objects.all()
        return [
            self._model_to_domain(model)
            for model in models
        ]

    def save(self, pessoa_fisica_tipo: PessoaFisicaTipoDomain) -> PessoaFisicaTipoDomain:
        """
        Salva ou atualiza uma associação no banco de dados.
        """
        pessoa_fisica = self.pessoa_fisica_repo.get_by_id(pessoa_fisica_tipo.pessoa_fisica_id)
        usuario_tipo = self.usuario_tipo_repo.get_by_id(pessoa_fisica_tipo.usuario_tipo_id)

        if not pessoa_fisica or not usuario_tipo:
            raise ValueError("Pessoa Física ou Tipo de Usuário inválido.")

        model = self._domain_to_model(pessoa_fisica_tipo)
        model.pessoa_fisica_id = pessoa_fisica.pessoa_fisica_id
        model.usuario_tipo_id = usuario_tipo.usuario_tipo_id
        model.save()

        return self._model_to_domain(model)

    def _model_to_domain(self, model: PessoaFisicaTipoModel) -> PessoaFisicaTipoDomain:
        """
        Converte o model de infraestrutura para a entidade de domínio.
        """
        return PessoaFisicaTipoDomain(
            pessoa_fisica_tipo_id=model.id,
            pessoa_fisica_id=model.pessoa_fisica_id,
            usuario_tipo_id=model.usuario_tipo_id,
            data_criacao=model.data_criacao
        )

    def _domain_to_model(self, domain: PessoaFisicaTipoDomain) -> PessoaFisicaTipoModel:
        """
        Converte a entidade de domínio para o model de infraestrutura.
        """
        return PessoaFisicaTipoModel(
            id=domain.pessoa_fisica_tipo_id,
            pessoa_fisica_id=domain.pessoa_fisica_id,
            usuario_tipo_id=domain.usuario_tipo_id,
            data_criacao=domain.data_criacao
        )
