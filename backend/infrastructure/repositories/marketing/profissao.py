# pylint: disable=no-member
"""
Módulo que implementa o repositório concreto para Profissao.

Este repositório interage com o banco de dados através da model ProfissaoModel,
implementando as operações definidas no contrato ProfissaoContract.
Exceções lançadas:
    - EntityNotFoundException: Se a profissão não for encontrada no banco de dados.
    - OperationFailedException: Se ocorrer um erro inesperado ao realizar alguma operação.
"""

from typing import List, Optional
from django.db import transaction
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.entities.profissao import ProfissaoDomain
from domain.marketing.repositories.profissao import ProfissaoContract
from infrastructure.models.marketing.profissao import ProfissaoModel


class ProfissaoRepository(ProfissaoContract):
    """
    Repositório concreto para a entidade de domínio Profissao.

    Este repositório implementa o contrato ProfissaoContract, interagindo com o banco
    de dados através da model ProfissaoModel e gerenciando as operações de CRUD.
    """

    @transaction.atomic
    def salvar(self, profissao: ProfissaoDomain, user) -> str:
        """
        Salva ou atualiza uma instância de Profissao no banco de dados.

        Converte a entidade de domínio ProfissaoDomain para a model ProfissaoModel
        e a salva ou atualiza no banco.

        Args:
            profissao (ProfissaoDomain): A instância de Profissao a ser salva.

        Returns:
            str: Mensagem indicando se a profissão foi criada ou atualizada.

        Raises:
            OperationFailedException: Se ocorrer algum erro ao salvar.
        """
        try:
            # Salva ou atualiza a profissão e retorna um indicador de criação
            profissao_model, created = ProfissaoModel.objects.update_or_create(
                id=profissao.profissao_id,
                defaults={
                    'codigo': profissao.codigo,
                    'descricao': profissao.descricao,
                }
            )

            # Garantir que os campos de auditoria sejam preenchidos passando o user
            profissao_model.save(user=user)

            # Retorna a mensagem apropriada
            if created:
                return "Profissão criada com sucesso."
            return "Profissão atualizada com sucesso."

        except Exception as exc:
            raise OperationFailedException(f"Erro ao salvar a profissão: {str(exc)}") from exc

    @transaction.atomic
    def buscar_por_id(self, profissao_id: int) -> Optional[ProfissaoDomain]:
        """
        Busca uma instância de Profissao por seu ID no banco de dados.

        Args:
            profissao_id (int): O identificador único da profissão.

        Returns:
            Optional[ProfissaoDomain]: A instância de Profissao, ou None se não encontrada.

        Raises:
            EntityNotFoundException: Se a profissão não for encontrada.
            OperationFailedException: Se ocorrer algum erro ao buscar a profissão.
        """
        try:
            profissao_model = ProfissaoModel.objects.get(id=profissao_id)
            return ProfissaoDomain(
                profissao_id=profissao_model.id,
                codigo=profissao_model.codigo,
                descricao=profissao_model.descricao
            )
        except ProfissaoModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Profissão com ID {profissao_id} não encontrada.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao buscar a profissão: {str(exc)}") from exc

    def listar_todas(self) -> List[ProfissaoDomain]:
        """
        Lista todas as instâncias de Profissao no banco de dados.

        Returns:
            List[ProfissaoDomain]: Uma lista com todas as profissões.

        Raises:
            OperationFailedException: Se ocorrer algum erro ao listar as profissões.
        """
        try:
            profissao_model_list = ProfissaoModel.objects.all()
            return [
                ProfissaoDomain(
                    profissao_id=profissao.id,
                    codigo=profissao.codigo,
                    descricao=profissao.descricao
                ) for profissao in profissao_model_list
            ]
        except Exception as exc:
            raise OperationFailedException(f"Erro ao listar as profissões: {str(exc)}") from exc
