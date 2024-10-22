# pylint: disable=no-member

from typing import Optional, List
from django.db import transaction
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.repositories.pessoa_juridica import (
                                            PessoaJuridicaContract)
from domain.marketing.entities.pessoa_juridica import PessoaJuridicaDomain
from infrastructure.models.marketing.pessoa_juridica import PessoaJuridicaModel
from infrastructure.repositories.marketing.pessoa_fisica import (
                                            PessoaFisicaRepository)
from infrastructure.repositories.marketing.endereco import EnderecoRepository
from infrastructure.repositories.shared.resources.rede_social import (
                                                    RedeSocialRepository)
from infrastructure.repositories.marketing.atividade_economica import (
                                            AtividadeEconomicaRepository)


class PessoaJuridicaRepository(PessoaJuridicaContract):
    """
    Repositório concreto para a entidade PessoaJuridica, interagindo apenas com repositórios
    de relacionamentos, sem acesso direto às models.
    """

    def __init__(
        self,
        pessoa_fisica_repository: PessoaFisicaRepository,
        atividade_economica_repository: AtividadeEconomicaRepository,
        endereco_repository: EnderecoRepository,
        rede_social_repository: RedeSocialRepository
    ):
        self.pessoa_fisica_repository = pessoa_fisica_repository
        self.atividade_economica_repository = atividade_economica_repository
        self.endereco_repository = endereco_repository
        self.rede_social_repository = rede_social_repository

    @transaction.atomic
    def get_by_id(self, pessoa_juridica_id: int) -> Optional[PessoaJuridicaDomain]:
        """
        Recupera uma pessoa jurídica pelo ID, utilizando os repositórios de relacionamento.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.

        Returns:
            Optional[PessoaJuridicaDomain]: A entidade de domínio correspondente, ou None se não encontrada.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            return self._model_to_domain(pessoa_juridica_model)
        except PessoaJuridicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Jurídica com ID {pessoa_juridica_id} não encontrada.") from exc

    @transaction.atomic
    def save(self, pessoa_juridica: PessoaJuridicaDomain) -> PessoaJuridicaDomain:
        """
        Salva ou atualiza uma pessoa jurídica no repositório.

        Args:
            pessoa_juridica (PessoaJuridicaDomain): A entidade de domínio a ser salva.

        Returns:
            PessoaJuridicaDomain: A entidade de domínio salva ou atualizada.
        """
        try:
            pessoa_juridica_model, created = PessoaJuridicaModel.objects.update_or_create(
                id=pessoa_juridica.id,
                defaults={
                    'razao_social': pessoa_juridica.razao_social,
                    'nome_fantasia': pessoa_juridica.nome_fantasia,
                    'cnpj': pessoa_juridica.cnpj,
                    'inscricao_estadual': pessoa_juridica.inscricao_estadual,
                    'website': pessoa_juridica.website,
                    'iniciador_id': pessoa_juridica.iniciador_id,
                }
            )

            # Atualizar os relacionamentos usando os repositórios
            self._atualizar_relacionamentos(pessoa_juridica_model, pessoa_juridica)

            return self._model_to_domain(pessoa_juridica_model)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao salvar a pessoa jurídica: {str(exc)}") from exc

    @transaction.atomic
    def delete(self, pessoa_juridica_id: int) -> None:
        """
        Exclui uma pessoa jurídica do repositório pelo ID.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica a ser excluída.
        """
        try:
            PessoaJuridicaModel.objects.filter(id=pessoa_juridica_id).delete()
        except Exception as exc:
            raise OperationFailedException(f"Erro ao excluir a pessoa jurídica com ID {pessoa_juridica_id}: {str(exc)}") from exc

    @transaction.atomic
    def list_all(self) -> List[PessoaJuridicaDomain]:
        """
        Retorna uma lista de todas as pessoas jurídicas cadastradas.

        Returns:
            List[PessoaJuridicaDomain]: Lista de todas as entidades de domínio PessoaJuridica.
        """
        try:
            pessoas_juridicas = PessoaJuridicaModel.objects.all()
            return [self._model_to_domain(pessoa) for pessoa in pessoas_juridicas]
        except Exception as exc:
            raise OperationFailedException(f"Erro ao listar todas as pessoas jurídicas: {str(exc)}") from exc

    @transaction.atomic
    def adicionar_administrador(self, pessoa_juridica_id: int, administrador_id: int) -> None:
        """
        Adiciona um administrador a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            administrador_id (int): O ID do administrador a ser adicionado.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            administrador = self.pessoa_fisica_repository.get_by_id(administrador_id)
            pessoa_juridica_model.administradores.add(administrador.id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao adicionar o administrador à pessoa jurídica: {str(exc)}") from exc

    @transaction.atomic
    def remover_administrador(self, pessoa_juridica_id: int, administrador_id: int) -> None:
        """
        Remove um administrador de uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            administrador_id (int): O ID do administrador a ser removido.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            administrador = self.pessoa_fisica_repository.get_by_id(administrador_id)
            pessoa_juridica_model.administradores.remove(administrador.id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao remover o administrador da pessoa jurídica: {str(exc)}") from exc

    @transaction.atomic
    def adicionar_atividade_economica(self, pessoa_juridica_id: int, atividade_id: int) -> None:
        """
        Adiciona uma atividade econômica a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            atividade_id (int): O ID da atividade econômica a ser adicionada.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            atividade = self.atividade_economica_repository.get_by_id(atividade_id)
            pessoa_juridica_model.atividades_economicas.add(atividade.id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao adicionar a atividade econômica: {str(exc)}") from exc

    @transaction.atomic
    def remover_atividade_economica(self, pessoa_juridica_id: int, atividade_id: int) -> None:
        """
        Remove uma atividade econômica de uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            atividade_id (int): O ID da atividade econômica a ser removida.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            atividade = self.atividade_economica_repository.get_by_id(atividade_id)
            pessoa_juridica_model.atividades_economicas.remove(atividade.id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao remover a atividade econômica: {str(exc)}") from exc

    @transaction.atomic
    def adicionar_rede_social(self, pessoa_juridica_id: int, rede_social_id: int) -> None:
        """
        Adiciona uma rede social a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            rede_social_id (int): O ID da rede social a ser adicionada.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            rede_social = self.rede_social_repository.get_by_id(rede_social_id)
            pessoa_juridica_model.redes_sociais.add(rede_social.id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao adicionar a rede social: {str(exc)}") from exc

    @transaction.atomic
    def remover_rede_social(self, pessoa_juridica_id: int, rede_social_id: int) -> None:
        """
        Remove uma rede social de uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.
            rede_social_id (int): O ID da rede social a ser removida.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            rede_social = self.rede_social_repository.get_by_id(rede_social_id)
            pessoa_juridica_model.redes_sociais.remove(rede_social.id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao remover a rede social: {str(exc)}") from exc

    def _model_to_domain(self, pessoa_juridica_model: PessoaJuridicaModel) -> PessoaJuridicaDomain:
        """
        Converte um modelo de banco de dados em uma entidade de domínio.

        Args:
            pessoa_juridica_model (PessoaJuridicaModel): A instância do modelo do banco de dados.

        Returns:
            PessoaJuridicaDomain: A instância da entidade de domínio convertida.
        """
        administradores_ids = list(pessoa_juridica_model.administradores.values_list('id', flat=True))
        atividades_economicas_ids = list(pessoa_juridica_model.atividades_economicas.values_list('id', flat=True))
        enderecos_ids = list(pessoa_juridica_model.enderecos.values_list('id', flat=True))
        redes_sociais_ids = list(pessoa_juridica_model.redes_sociais.values_list('id', flat=True))

        return PessoaJuridicaDomain(
            id=pessoa_juridica_model.id,
            razao_social=pessoa_juridica_model.razao_social,
            nome_fantasia=pessoa_juridica_model.nome_fantasia,
            cnpj=pessoa_juridica_model.cnpj,
            inscricao_estadual=pessoa_juridica_model.inscricao_estadual,
            administradores=administradores_ids,
            iniciador_id=pessoa_juridica_model.iniciador_id,
            enderecos=enderecos_ids,
            atividades_economicas=atividades_economicas_ids,
            website=pessoa_juridica_model.website,
            redes_sociais=redes_sociais_ids
        )

    def _atualizar_relacionamentos(self, pessoa_juridica_model: PessoaJuridicaModel, pessoa_juridica: PessoaJuridicaDomain) -> None:
        """
        Atualiza os relacionamentos da pessoa jurídica (administradores, atividades econômicas, endereços e redes sociais).

        Args:
            pessoa_juridica_model (PessoaJuridicaModel): A instância do modelo do banco de dados.
            pessoa_juridica (PessoaJuridicaDomain): A entidade de domínio da pessoa jurídica.
        """
        # Atualizar administradores
        pessoa_juridica_model.administradores.set(
            self.pessoa_fisica_repository.get_by_ids(pessoa_juridica.administradores)
        )

        # Atualizar atividades econômicas
        pessoa_juridica_model.atividades_economicas.set(
            self.atividade_economica_repository.get_by_ids(pessoa_juridica.atividades_economicas)
        )

        # Atualizar endereços
        pessoa_juridica_model.enderecos.set(
            self.endereco_repository.get_by_ids(pessoa_juridica.enderecos)
        )

        # Atualizar redes sociais
        pessoa_juridica_model.redes_sociais.set(
            self.rede_social_repository.get_by_ids(pessoa_juridica.redes_sociais)
        )

        pessoa_juridica_model.save()
