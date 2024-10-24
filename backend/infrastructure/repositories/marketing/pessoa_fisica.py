# pylint: disable=no-member
"""
Módulo responsável pela implementação do repositório concreto de PessoaFisica.

Este módulo implementa o repositório concreto que interage com as models do banco
de dados PessoaFisicaModel e seus relacionamentos. Ele implementa as operações
definidas no contrato PessoaFisicaContract, realizando as interações com o banco
de dados para salvar, buscar, alterar status, gerenciar endereços, localização
e redes sociais.

Classes:
    PessoaFisicaRepository: Repositório concreto que implementa o contrato
    PessoaFisicaContract para gerenciar PessoaFisica no banco de dados.
"""
from typing import Dict, List
from django.db import transaction
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.marketing.pessoa_fisica_rede_social import (
    PessoaFisicaRedeSocialModel
)
from infrastructure.repositories.marketing.endereco import EnderecoRepository
from infrastructure.repositories.shared.resources.localizacao import (
                                                    LocalizacaoRepository)
from infrastructure.repositories.shared.resources.rede_social import (
                                                    RedeSocialRepository)


class PessoaFisicaRepository:
    """
    Repositório concreto para a entidade de domínio PessoaFisica.

    Este repositório gerencia as operações de persistência e recuperação
    de PessoaFisica no banco de dados, além de gerenciar os relacionamentos
    com endereços, localização e redes sociais.
    """

    def __init__(self):
        self.endereco_repository = EnderecoRepository()
        self.localizacao_repository = LocalizacaoRepository()
        self.rede_social_repository = RedeSocialRepository()

    @transaction.atomic
    def get_by_id(self, pessoa_fisica_id: int) -> PessoaFisicaModel:
        """
        Recupera uma pessoa física pelo ID no banco de dados.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.

        Returns:
            PessoaFisicaModel: A entidade de pessoa física do banco de dados.

        Raises:
            EntityNotFoundException: Se a pessoa física não for encontrada.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            return pessoa_model
        except PessoaFisicaModel.DoesNotExist as e:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from e
        except Exception as e:
            raise OperationFailedException(f"Erro ao buscar pessoa física: {str(e)}") from e

    @transaction.atomic
    def save(self, pessoa_model: PessoaFisicaModel, redes_sociais: Dict[int, str], user) -> str:
        """
        Salva ou atualiza uma pessoa física no banco de dados e suas redes sociais associadas.

        Args:
            pessoa_model (PessoaFisicaModel): A entidade pessoa física.
            redes_sociais (Dict[int, str]): Redes sociais com o nome de usuário.

        Returns:
            str: Mensagem indicando se a pessoa foi criada ou atualizada.
        """
        try:
            created = not pessoa_model.pk  # Verifica se a pessoa está sendo criada ou atualizada

            # Salva ou atualiza a pessoa física no banco de dados
            pessoa_model.save(user=user)

            # Gerencia o relacionamento de redes sociais
            self._salvar_redes_sociais(pessoa_model, redes_sociais)

            # Retorna a mensagem apropriada
            if created:
                return "Pessoa Física criada com sucesso."
            else:
                return "Pessoa Física atualizada com sucesso."
        except Exception as e:
            raise OperationFailedException(f"Erro ao salvar a pessoa física: {str(e)}") from e

    @transaction.atomic
    def delete(self, pessoa_fisica_id: int, user) -> str:
        """
        Exclui uma pessoa física do banco de dados pelo ID.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.

        Returns:
            str: Mensagem de sucesso da exclusão.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)

            # Remove todas as associações de redes sociais da pessoa
            PessoaFisicaRedeSocialModel.objects.filter(pessoa_fisica=pessoa_model).delete()

            # Exclui a pessoa física
            pessoa_model.delete(user=user)

            return "Pessoa Física excluída com sucesso."
        except PessoaFisicaModel.DoesNotExist as e:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from e
        except Exception as e:
            raise OperationFailedException(f"Erro ao excluir a pessoa física: {str(e)}") from e

    def list_all(self) -> List[PessoaFisicaModel]:
        """
        Retorna uma lista de todas as pessoas físicas do banco de dados.

        Returns:
            List[PessoaFisicaModel]: Lista de todas as entidades PessoaFisica.
        """
        try:
            return PessoaFisicaModel.objects.all()
        except Exception as e:
            raise OperationFailedException(f"Erro ao listar pessoas físicas: {str(e)}") from e

    @transaction.atomic
    def alterar_status(self, pessoa_fisica_id: int, status: str) -> str:
        """
        Altera o status de uma pessoa física no banco de dados.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.
            status (str): O novo status a ser definido.

        Returns:
            str: Mensagem indicando que o status foi alterado.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            pessoa_model.situacao = status
            pessoa_model.save()

            return "Status da pessoa física alterado com sucesso."
        except PessoaFisicaModel.DoesNotExist as e:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from e
        except Exception as e:
            raise OperationFailedException(f"Erro ao alterar o status: {str(e)}") from e

    @transaction.atomic
    def _salvar_redes_sociais(self, pessoa_model: PessoaFisicaModel, redes_sociais: Dict[int, str]) -> None:
        """
        Salva ou atualiza as redes sociais associadas à pessoa física.

        Args:
            pessoa_model (PessoaFisicaModel): O modelo da pessoa física.
            redes_sociais (Dict[int, str]): Dicionário de ID da rede social e nome de usuário.
        """
        try:
            # Redes sociais já associadas a esta pessoa
            redes_existentes = PessoaFisicaRedeSocialModel.objects.filter(
                pessoa_fisica=pessoa_model
            )

            # Redes sociais que precisam ser atualizadas
            redes_a_atualizar = {}

            # Itera sobre as redes sociais fornecidas
            for rede_social_id, usuario in redes_sociais.items():
                rede_social_model = self.rede_social_repository.get_by_id(rede_social_id)

                # Verifica se já existe uma associação com essa rede social
                rede_existente = redes_existentes.filter(rede_social=rede_social_model).first()

                if rede_existente:
                    # Atualiza o usuário se houver alteração
                    if rede_existente.endereco != usuario:
                        rede_existente.endereco = usuario
                        redes_a_atualizar[rede_existente.id] = rede_existente
                else:
                    # Cria uma nova associação se não existir
                    PessoaFisicaRedeSocialModel.objects.create(
                        pessoa_fisica=pessoa_model,
                        rede_social=rede_social_model,
                        endereco=usuario
                    )

            # Atualiza as redes sociais modificadas
            if redes_a_atualizar:
                PessoaFisicaRedeSocialModel.objects.bulk_update(
                    list(redes_a_atualizar.values()), ['endereco']
                )

            # Remove redes sociais que não estão na lista fornecida
            ids_informados = list(redes_sociais.keys())
            redes_existentes.exclude(rede_social_id__in=ids_informados).delete()

        except Exception as e:
            raise OperationFailedException(
                f"Erro ao salvar redes sociais: {str(e)}") from e
