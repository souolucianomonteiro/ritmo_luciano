# pylint: disable=no-member
"""
Módulo que implementa o repositório concreto para UsuarioTipo.

Este repositório interage com o banco de dados através da model UsuarioTipoModel,
implementando as operações definidas no contrato UsuarioTipoContract.

Classes:
    UsuarioTipoRepository: Implementa o contrato UsuarioTipoContract e gerencia 
    as operações de persistência e recuperação de UsuarioTipoModel.
"""

from typing import List, Optional
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.entities.usuario_tipo import UsuarioTipoDomain
from domain.marketing.repositories.usuario_tipo import UsuarioTipoContract
from infrastructure.models.marketing.usuario_tipo import UsuarioTipoModel


class UsuarioTipoRepository(UsuarioTipoContract):
    """
    Repositório concreto para a entidade de domínio UsuarioTipo.

    Este repositório implementa o contrato UsuarioTipoContract, interagindo com o banco
    de dados através da model UsuarioTipoModel.
    """

    def salvar(self, usuario_tipo: UsuarioTipoDomain) -> str:
        """
        Salva uma instância de UsuarioTipo no banco de dados.

        Converte a entidade de domínio UsuarioTipoDomain para a model UsuarioTipoModel
        e a salva no banco.

        Args:
            usuario_tipo (UsuarioTipoDomain): A instância de UsuarioTipo a ser salva.

        Returns:
            str: Mensagem de sucesso indicando que o tipo de usuário foi salvo.
        """
        try:
            usuario_tipo_model = UsuarioTipoModel(
                nome=usuario_tipo.nome,
                descricao=usuario_tipo.descricao
            )
            usuario_tipo_model.save()
            return "Tipo de usuário salvo com sucesso."
        except Exception as exc:
            raise OperationFailedException(f"Erro ao salvar o tipo de usuário: {str(exc)}") from exc

    def buscar_por_id(self, usuario_tipo_id: int) -> Optional[UsuarioTipoDomain]:
        """
        Busca uma instância de UsuarioTipo por seu ID no banco de dados.

        Args:
            usuario_tipo_id (int): O identificador único do tipo de usuário.

        Returns:
            Optional[UsuarioTipoDomain]: A instância de UsuarioTipo, ou None se não encontrada.
        """
        try:
            usuario_tipo_model = UsuarioTipoModel.objects.get(id=usuario_tipo_id)
            return UsuarioTipoDomain(
                usuario_tipo_id=usuario_tipo_model.id,
                nome=usuario_tipo_model.nome,
                descricao=usuario_tipo_model.descricao
            )
        except UsuarioTipoModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Tipo de usuário com ID {usuario_tipo_id} não encontrado.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao buscar o tipo de usuário: {str(exc)}") from exc

    def listar_todos(self) -> List[UsuarioTipoDomain]:
        """
        Lista todas as instâncias de UsuarioTipo no banco de dados.

        Returns:
            List[UsuarioTipoDomain]: Uma lista com todos os tipos de usuário.
        """
        try:
            usuario_tipos = UsuarioTipoModel.objects.all()
            return [
                UsuarioTipoDomain(
                    usuario_tipo_id=usuario_tipo.id,
                    nome=usuario_tipo.nome,
                    descricao=usuario_tipo.descricao
                ) for usuario_tipo in usuario_tipos
            ]
        except Exception as exc:
            raise OperationFailedException(f"Erro ao listar os tipos de usuário: {str(exc)}") from exc
