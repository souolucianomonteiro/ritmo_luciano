"""
Módulo que implementa o repositório concreto para RedeSocial.

Este repositório interage com o banco de dados através da model RedeSocialModel,
implementando as operações definidas no contrato RedeSocialContract.
"""

from typing import List, Optional
from domain.shared.resources.entities.rede_social import RedeSocialDomain
from domain.shared.resources.repositories.rede_social import RedeSocialContract
from infrastructure.models.shared.resources.rede_social import RedeSocialModel
from django.core.exceptions import ObjectDoesNotExist


class RedeSocialRepository(RedeSocialContract):
    """
    Repositório concreto para a entidade de domínio RedeSocial.

    Este repositório implementa o contrato RedeSocialContract, interagindo com o banco
    de dados através da model RedeSocialModel.
    """

    def salvar(self, rede_social: RedeSocialDomain) -> None:
        """
        Salva uma instância de RedeSocial no banco de dados.

        Converte a entidade de domínio RedeSocialDomain para a model RedeSocialModel
        e a salva no banco de dados.

        Args:
            rede_social (RedeSocialDomain): A instância de RedeSocial a ser salva.
        """
        rede_social_model = RedeSocialModel(
            nome=rede_social.nome,
            icone=rede_social.icone
        )
        rede_social_model.save()

    def buscar_por_id(self, rede_social_id: int) -> Optional[RedeSocialDomain]:
        """
        Busca uma instância de RedeSocial por seu ID no banco de dados.

        Args:
            rede_social_id (int): O identificador único da rede social.

        Returns:
            Optional[RedeSocialDomain]: A instância de RedeSocial, ou None se não encontrada.
        """
        try:
            rede_social_model = RedeSocialModel.objects.get(id=rede_social_id)
            return RedeSocialDomain(
                rede_social_id=rede_social_model.id,
                nome=rede_social_model.nome,
                icone=rede_social_model.icone
            )
        except ObjectDoesNotExist:
            return None

    def listar_todas(self) -> List[RedeSocialDomain]:
        """
        Lista todas as instâncias de RedeSocial no banco de dados.

        Returns:
            List[RedeSocialDomain]: Uma lista com todas as redes sociais.
        """
        redes_sociais = RedeSocialModel.objects.all()
        return [
            RedeSocialDomain(
                rede_social_id=rede_social.id,
                nome=rede_social.nome,
                icone=rede_social.icone
            ) for rede_social in redes_sociais
        ]
