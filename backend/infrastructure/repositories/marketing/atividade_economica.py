"""
Módulo responsável pela implementação do repositório concreto para a entidade
AtividadeEconomicaModel.

Este módulo implementa as operações de persistência e recuperação de dados
relacionados à entidade AtividadeEconomicaModel no banco de dados utilizando
o Django ORM. As operações incluem criação, leitura, atualização e exclusão
(CRUD), com tratamento adequado de exceções para erros esperados e
inesperados.

Exceções lançadas:
    - EntityNotFoundException: Lançada quando uma entidade não é encontrada no
    banco de dados.
    - OperationFailedException: Lançada quando ocorre um erro inesperado ao
    realizar uma operação no banco de dados.
"""
from django.core.exceptions import ObjectDoesNotExist
from domain.marketing.repositories.atividade_economica import (
                                    AtividadeEconomicaContract)
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                        OperationFailedException)
from infrastructure.models.marketing.atividade_economica import (
                                        AtividadeEconomicaModel)


class AtividadeEconomicaRepository(AtividadeEconomicaContract):
    """
    Repositório concreto para AtividadeEconomicaDomain.

    Esta classe implementa as operações de persistência e recuperação
    da entidade AtividadeEconomicaDomain no banco de dados utilizando o Django ORM.
    """

    def get_by_id(self, atividade_econ_id: int) -> AtividadeEconomicaModel:
        """
        Recupera uma entidade AtividadeEconomicaModel pelo seu ID.

        Args:
            atividade_econ_id (int): O identificador único da atividade 
            econômica.

        Returns:
            AtividadeEconomicaModel: A entidade de atividade econômica 
            encontrada.

        Raises:
            EntityNotFoundException: Se a atividade econômica com o ID 
            fornecido não for encontrada no repositório.
            OperationFailedException: Se ocorrer um erro inesperado
            na operação.
        """
        try:
            # Busca a atividade econômica no banco de dados
            atividade = AtividadeEconomicaModel.objects.get(id=atividade_econ_id)
            return atividade

        except ObjectDoesNotExist: 
            raise EntityNotFoundException(
                f"Atividade econômica com ID {atividade_econ_id} "
                f"não encontrada."
            ) from e

        except Exception as e:
            raise OperationFailedException(
                f"Erro ao buscar a atividade econômica: {str(e)}"
            ) from e

    def list_all(self) -> list[AtividadeEconomicaModel]:
        """
        Retorna todas as atividades econômicas cadastradas no banco de dados.

        Returns:
            List[AtividadeEconomicaModel]: Lista de todas as atividades econômicas.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado na operação.
        """
        try:
            # Lista todas as atividades econômicas do banco de dados
            atividades = AtividadeEconomicaModel.objects.all()
            return list(atividades)

        except Exception as e:
            raise OperationFailedException(
                f"Erro ao listar as atividades econômicas: {str(e)}"
            ) from e

    def save(self, atividade_economica: AtividadeEconomicaModel) -> None:
        """
        Salva ou atualiza uma entidade AtividadeEconomicaModel no banco de dados.

        Args:
            atividade_economica (AtividadeEconomicaModel): A entidade a ser salva ou atualizada.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao salvar a entidade.
        """
        try:
            # Salva a atividade econômica no banco de dados
            atividade_economica.save()

        except Exception as e:
            raise OperationFailedException(
                f"Erro ao salvar a atividade econômica: {str(e)}"
            ) from e

    def delete(self, atividade_econ_id: int) -> None:
        """
        Remove uma entidade AtividadeEconomicaModel do banco de dados pelo ID.

        Args:
            atividade_econ_id (int): O identificador único da atividade econômica.

        Raises:
            EntityNotFoundException: Se a atividade econômica com o ID fornecido
            não for encontrada no banco de dados.
            OperationFailedException: Se ocorrer um erro inesperado ao remover a entidade.
        """
        try:
            # Busca a atividade econômica no banco de dados
            atividade = AtividadeEconomicaModel.objects.get(id=atividade_econ_id)
            
            # Remove a entidade
            atividade.delete()

        except ObjectDoesNotExist:
            raise EntityNotFoundException(
                f"Atividade econômica com ID {atividade_econ_id} não encontrada."
            )from e

        except Exception as e:
            raise OperationFailedException(
                f"Erro ao remover a atividade econômica: {str(e)}"
            ) from e
