# pylint: disable=no-member

from typing import Optional
from domain.website.entities.localizacao import Localizacao
from domain.website.repositories.localizacao import (
                        LocalizacaoRepositoryInterface)
from infrastructure.models.localizacao import Localizacao as LocalizacaoModel


class LocalizacaoRepository(LocalizacaoRepositoryInterface):
    """Classe implmenta o repositório concreto de localização"""

    def save(self, localizacao: Localizacao) -> Localizacao:
        """
        Persiste a localização no banco de dados.
        """
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
        localizacao_model.save()
        return localizacao

    def find_by_ip(self, ip_address: str) -> Optional[Localizacao]:
        """
        Retorna a localização associada a um endereço IP.
        """
        try:
            localizacao_model = LocalizacaoModel.objects.get(ip_address=ip_address)
            return self._to_domain(localizacao_model)
        except LocalizacaoModel.DoesNotExist:
            return None

    def _to_domain(self, localizacao_model: LocalizacaoModel) -> Localizacao:
        """
        Converte o modelo de banco de dados para a entidade de domínio.
        """
        return Localizacao(
            ip_address=localizacao_model.ip_address,
            latitude=localizacao_model.latitude,
            longitude=localizacao_model.longitude,
            precisao=localizacao_model.precisao,
            cidade=localizacao_model.cidade,
            estado=localizacao_model.estado,
            pais=localizacao_model.pais,
            data_hora_captura=localizacao_model.data_hora_captura
        )
