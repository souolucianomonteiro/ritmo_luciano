# pylint: disable=no-member

"""
Módulo responsável pela implementação do repositório concreto de Localizacao.

Este módulo implementa o repositório concreto que interage com a model de banco
de dados LocalizacaoModel. Ele implementa as operações definidas no contrato
LocalizacaoContract, realizando as interações com o banco de dados para salvar
e buscar instâncias de Localizacao.

Classes:
    LocalizacaoRepository: Repositório concreto que implementa o contrato
    LocalizacaoContract para gerenciar Localizacoes no banco de dados.
"""

from typing import List, Optional
from domain.shared.resources.entities.localizacao import LocalizacaoDomain
from domain.shared.resources.repositories.localizacao import LocalizacaoContract
from infrastructure.models.shared.resources.localizacao import LocalizacaoModel
from django.core.exceptions import ObjectDoesNotExist


class LocalizacaoRepository(LocalizacaoContract):
    """
    Repositório concreto para a entidade de domínio Localizacao.

    Este repositório implementa o contrato LocalizacaoContract, gerenciando
    as operações de persistência e recuperação de Localizacoes no banco
    de dados.
    """

    def salvar(self, localizacao: LocalizacaoDomain) -> None:
        """
        Salva uma instância de Localizacao no banco de dados.

        Este método realiza a conversão da entidade de domínio Localizacao
        para a model LocalizacaoModel e salva no banco de dados.

        Args:
            localizacao (Localizacao): A instância de Localizacao a ser salva.
        """
        # Converte a entidade de domínio Localizacao para a model
        # LocalizacaoModel
        localizacao_model = LocalizacaoModel(
            ip_address=localizacao.ip_address,
            latitude=localizacao.latitude,
            longitude=localizacao.longitude,
            precisao=localizacao.precisao,
            cidade=localizacao.cidade,
            estado=localizacao.estado,
            pais=localizacao.pais,
            data_hora_captura=localizacao.data_hora_captura
        )
        localizacao_model.save()  # Salva no banco de dados

    def buscar_por_id(self, localizacao_id: int) -> Optional[LocalizacaoDomain]:
        """
        Busca uma instância de Localizacao no banco de dados pelo ID.

        Este método realiza a busca da LocalizacaoModel no banco de dados e,
        se encontrada, converte-a para a entidade de domínio Localizacao.

        Args:
            localizacao_id (int): O identificador único da Localizacao.

        Returns:
            Optional[Localizacao]: A instância de Localizacao, ou None se
            não encontrada.
        """
        try:
            # Busca a model LocalizacaoModel no banco de dados
            localizacao_model = LocalizacaoModel.objects.get(id=localizacao_id)
            
            # Converte a model LocalizacaoModel para a entidade de domínio
            # Localizacao
            return LocalizacaoDomain(
                ip_address=localizacao_model.ip_address,
                latitude=localizacao_model.latitude,
                longitude=localizacao_model.longitude,
                precisao=localizacao_model.precisao,
                cidade=localizacao_model.cidade,
                estado=localizacao_model.estado,
                pais=localizacao_model.pais,
                data_hora_captura=localizacao_model.data_hora_captura
            )
        except ObjectDoesNotExist:
            # Se a localização não for encontrada, retorna None
            return None

    def listar_todas(self) -> List[LocalizacaoDomain]:
        """
        Lista todas as instâncias de Localizacao no banco de dados.

        Este método busca todas as instâncias de LocalizacaoModel no banco
        de dados
        e as converte para a entidade de domínio Localizacao.

        Returns:
            List[Localizacao]: Uma lista com todas as instâncias de
            Localizacao.
        """
        # Busca todas as instâncias de LocalizacaoModel no banco de dados
        localizacoes_model = LocalizacaoModel.objects.all()

        # Converte as instâncias de LocalizacaoModel para a entidade de
        # domínio Localizacao
        return [
            LocalizacaoDomain(
                ip_address=localizacao_model.ip_address,
                latitude=localizacao_model.latitude,
                longitude=localizacao_model.longitude,
                precisao=localizacao_model.precisao,
                cidade=localizacao_model.cidade,
                estado=localizacao_model.estado,
                pais=localizacao_model.pais,
                data_hora_captura=localizacao_model.data_hora_captura
            )
            for localizacao_model in localizacoes_model
        ]
