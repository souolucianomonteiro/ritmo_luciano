# pylint: disable=no-member
"""
Módulo que implementa o repositório concreto para a entidade EnderecoDomain.

Este módulo define a classe DjangoEnderecoRepository, que utiliza o ORM do Django
para realizar operações de CRUD relacionadas à entidade Endereco, como salvar, buscar
por ID, listar todos e excluir endereços no banco de dados.

Classes:
    - DjangoEnderecoRepository: Implementa as operações de persistência e recuperação de dados
      para a entidade EnderecoDomain.
"""
from typing import List, Optional
from infrastructure.models.endereco import EnderecoModel
from domain.website.entities.endereco import EnderecoDomain
from domain.website.repositories.endereco import EnderecoRepository


class DjangoEnderecoRepository(EnderecoRepository):
    """
    Repositório concreto para manipular a model EnderecoModel no Django ORM.
    """

    def save(self, endereco: EnderecoDomain) -> EnderecoDomain:
        """
        Salva ou atualiza um endereço no banco de dados.
        """

        # Se houver um endereço_id, tentamos encontrar um objeto existente. Caso contrário, cria-se um novo.
        if endereco.endereco_id:
            endereco_model = EnderecoModel.objects.get(id=endereco.endereco_id)
            endereco_model.rua = endereco.rua
            endereco_model.numero = endereco.numero
            endereco_model.complemento = endereco.complemento
            endereco_model.bairro = endereco.bairro
            endereco_model.cidade = endereco.cidade
            endereco_model.estado = endereco.estado
            endereco_model.cep = endereco.cep
            endereco_model.pais = endereco.pais
            endereco_model.tipo = endereco.tipo
            endereco_model.pessoa_fisica_id = endereco.pessoa_fisica_id
            endereco_model.pessoa_juridica_id = endereco.pessoa_juridica_id
            endereco_model.is_active = endereco.is_active
            endereco_model.data_fim = endereco.data_fim
        else:
            endereco_model = EnderecoModel(
                rua=endereco.rua,
                numero=endereco.numero,
                complemento=endereco.complemento,
                bairro=endereco.bairro,
                cidade=endereco.cidade,
                estado=endereco.estado,
                cep=endereco.cep,
                pais=endereco.pais,
                tipo=endereco.tipo,
                pessoa_fisica_id=endereco.pessoa_fisica_id,
                pessoa_juridica_id=endereco.pessoa_juridica_id,
                is_active=endereco.is_active,
                data_inicio=endereco.data_inicio,
                data_fim=endereco.data_fim
            )

        endereco_model.save()

        return EnderecoDomain(
            endereco_id=endereco_model.id,
            rua=endereco_model.rua,
            numero=endereco_model.numero,
            complemento=endereco_model.complemento,
            bairro=endereco_model.bairro,
            cidade=endereco_model.cidade,
            estado=endereco_model.estado,
            cep=endereco_model.cep,
            pais=endereco_model.pais,
            tipo=endereco_model.tipo,
            pessoa_fisica_id=endereco_model.pessoa_fisica_id,
            pessoa_juridica_id=endereco_model.pessoa_juridica_id,
            is_active=endereco_model.is_active,
            data_inicio=endereco_model.data_inicio,
            data_fim=endereco_model.data_fim
        )

    def find_by_id(self, endereco_id: int) -> Optional[EnderecoDomain]:
        """
        Busca um endereço pelo ID.
        """
        try:
            endereco_model = EnderecoModel.objects.get(id=endereco_id)
            return EnderecoDomain(
                endereco_id=endereco_model.id,
                rua=endereco_model.rua,
                numero=endereco_model.numero,
                complemento=endereco_model.complemento,
                bairro=endereco_model.bairro,
                cidade=endereco_model.cidade,
                estado=endereco_model.estado,
                cep=endereco_model.cep,
                pais=endereco_model.pais,
                tipo=endereco_model.tipo,
                pessoa_fisica_id=endereco_model.pessoa_fisica_id,
                pessoa_juridica_id=endereco_model.pessoa_juridica_id,
                is_active=endereco_model.is_active,
                data_inicio=endereco_model.data_inicio,
                data_fim=endereco_model.data_fim
            )
        except EnderecoModel.DoesNotExist:
            return None

    def find_all(self) -> List[EnderecoDomain]:
        """
        Retorna todos os endereços cadastrados no sistema.
        """
        endereco_models = EnderecoModel.objects.all()
        return [
            EnderecoDomain(
                endereco_id=endereco_model.id,
                rua=endereco_model.rua,
                numero=endereco_model.numero,
                complemento=endereco_model.complemento,
                bairro=endereco_model.bairro,
                cidade=endereco_model.cidade,
                estado=endereco_model.estado,
                cep=endereco_model.cep,
                pais=endereco_model.pais,
                tipo=endereco_model.tipo,
                pessoa_fisica_id=endereco_model.pessoa_fisica_id,
                pessoa_juridica_id=endereco_model.pessoa_juridica_id,
                is_active=endereco_model.is_active,
                data_inicio=endereco_model.data_inicio,
                data_fim=endereco_model.data_fim
            )
            for endereco_model in endereco_models
        ]

    def delete(self, endereco_id: int) -> None:
        """
        Remove um endereço pelo ID.
        """
        EnderecoModel.objects.filter(id=endereco_id).delete()
