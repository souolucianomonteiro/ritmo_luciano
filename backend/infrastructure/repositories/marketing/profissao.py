# pylint: disable=no-member
"""
Módulo que implementa o repositório concreto para Profissao.

Este repositório interage com o banco de dados através da model ProfissaoModel,
implementando as operações definidas no contrato ProfissaoContract.
"""

from typing import List, Optional
from infrastructure.models.marketing.profissao import ProfissaoModel
from domain.marketing.entities.profissao import ProfissaoDomain
from domain.marketing.repositories.profissao import ProfissaoContract
from django.core.exceptions import ObjectDoesNotExist

class ProfissaoRepository(ProfissaoContract):
    """
    Repositório concreto para a entidade de domínio Profissao.

    Este repositório implementa o contrato ProfissaoContract, interagindo com o banco
    de dados através da model ProfissaoModel.
    """

    def salvar(self, profissao: ProfissaoDomain) -> None:
        """
        Salva uma instância de Profissao no banco de dados.

        Converte a entidade de domínio ProfissaoDomain para a model ProfissaoModel
        e a salva no banco.

        Args:
            profissao (ProfissaoDomain): A instância de Profissao a ser salva.
        """
        profissao_model = ProfissaoModel(
            codigo=profissao.codigo,
            descricao=profissao.descricao
        )
        profissao_model.save()

    def buscar_por_id(self, profissao_id: int) -> Optional[ProfissaoDomain]:
        """
        Busca uma instância de Profissao por seu ID no banco de dados.

        Args:
            profissao_id (int): O identificador único da profissão.

        Returns:
            Optional[ProfissaoDomain]: A instância de Profissao, ou None se não encontrada.
        """
        try:
            profissao_model = ProfissaoModel.objects.get(id=profissao_id)
            return ProfissaoDomain(
                profissao_id=profissao_model.id,
                codigo=profissao_model.codigo,
                descricao=profissao_model.descricao
            )
        except ObjectDoesNotExist:
            return None

    def listar_todas(self) -> List[ProfissaoDomain]:
        """
        Lista todas as instâncias de Profissao no banco de dados.

        Returns:
            List[ProfissaoDomain]: Uma lista com todas as profissões.
        """
        profissao_model_list = ProfissaoModel.objects.all()
        return [
            ProfissaoDomain(
                profissao_id=profissao.id,
                codigo=profissao.codigo,
                descricao=profissao.descricao
            ) for profissao in profissao_model_list
        ]
