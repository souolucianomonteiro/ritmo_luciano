# pylint: disable=no-member
"""
Módulo responsável pela implementação concreta do repositório de UsuarioTipo.

Este módulo implementa o repositório concreto DjangoUsuarioTipoRepository,
utilizando o Django ORM para realizar as operações de persistência e
recuperação de dados relacionadas à entidade UsuarioTipo.

Classes:
    DjangoUsuarioTipoRepository: Classe concreta que implementa os métodos
    definidos no repositório abstrato para lidar com a persistência de
    UsuarioTipo.
"""
from typing import Optional, List
from domain.website.entities.usuario_tipo import UsuarioTipoDomain
from domain.website.repositories.usuario_tipo import UsuarioTipoRepository
from infrastructure.models.usuario_tipo import UsuarioTipo


class DjangoUsuarioTipoRepository(UsuarioTipoRepository):
    """
    Repositório concreto para a entidade UsuarioTipo.

    Implementa os métodos definidos no repositório abstrato, utilizando o Django ORM.
    """

    def save(self, usuario_tipo: UsuarioTipoDomain) -> UsuarioTipoDomain:
        """
        Salva ou atualiza uma instância de UsuarioTipo no repositório.

        Args:
            usuario_tipo (UsuarioTipoDomain): Instância de domínio a ser salva.

        Returns:
            UsuarioTipoDomain: A instância salva ou atualizada.
        """
        usuario_tipo_model = UsuarioTipo(
            id=usuario_tipo.id,
            nome=usuario_tipo.nome,
            descricao=usuario_tipo.descricao
        )
        usuario_tipo_model.save()
        usuario_tipo.id = usuario_tipo_model.id
        return usuario_tipo

    def get_by_id(self, usuario_tipo_id: int) -> Optional[UsuarioTipoDomain]:
        """
        Recupera uma instância de UsuarioTipo por seu ID.

        Args:
            usuario_tipo_id (int): ID do tipo de usuário a ser recuperado.

        Returns:
            Optional[UsuarioTipoDomain]: A instância encontrada ou None.
        """
        try:
            usuario_tipo_model = UsuarioTipo.objects.get(id=usuario_tipo_id)
            return UsuarioTipoDomain(
                id=usuario_tipo_model.id,
                nome=usuario_tipo_model.nome,
                descricao=usuario_tipo_model.descricao
            )
        except UsuarioTipo.DoesNotExist:
            return None

    def delete(self, usuario_tipo: UsuarioTipoDomain) -> None:
        """
        Exclui uma instância de UsuarioTipo do repositório.

        Args:
            usuario_tipo (UsuarioTipoDomain): A instância a ser excluída.
        """
        UsuarioTipo.objects.filter(id=usuario_tipo.id).delete()

    def list_all(self) -> List[UsuarioTipoDomain]:
        """
        Lista todas as instâncias de UsuarioTipo no repositório.

        Returns:
            List[UsuarioTipoDomain]: Lista de instâncias de tipos de usuários.
        """
        usuario_tipos = UsuarioTipo.objects.all()
        return [
            UsuarioTipoDomain(
                id=usuario_tipo.id,
                nome=usuario_tipo.nome,
                descricao=usuario_tipo.descricao
            )
            for usuario_tipo in usuario_tipos
        ]
