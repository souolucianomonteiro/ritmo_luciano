# pylint: disable=no-member
# type: ignore[attr-defined]
"""
Módulo responsável pela implementação do repositório concreto para a entidade
EnderecoDomain.

Este módulo implementa as operações de persistência e recuperação de dados
relacionados à entidade EnderecoDomain no banco de dados, utilizando o Django ORM.
As operações incluem criação, leitura, atualização e exclusão (CRUD), além de
consultas específicas para pessoas físicas e jurídicas.

Classes:
    EnderecoRepository: Implementação concreta do contrato EnderecoContract.
"""
from django.core.exceptions import ObjectDoesNotExist
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.entities.endereco import EnderecoDomain
from domain.marketing.repositories.endereco import EnderecoContract
from infrastructure.models.marketing.endereco import EnderecoModel


class EnderecoRepository(EnderecoContract):
    """
    Repositório concreto para EnderecoDomain.

    Esta classe implementa as operações de persistência e consulta para a entidade
    EnderecoDomain, utilizando o Django ORM para interagir com o banco de dados.
    """

    def get_by_id(self, endereco_id: int) -> EnderecoDomain:
        """
        Recupera um endereço pelo seu ID.

        Args:
            endereco_id (int): O identificador único do endereço.

        Returns:
            EnderecoDomain: A entidade de endereço correspondente ao ID fornecido.

        Raises:
            EntityNotFoundException: Se o endereço com o ID fornecido não for
            encontrado no banco de dados.
            OperationFailedException: Se ocorrer um erro inesperado ao realizar
            a operação.
        """
        try:
            # Busca o endereço no banco de dados
            endereco = EnderecoModel.objects.get(id=endereco_id)
            # Converte EnderecoModel para EnderecoDomain (se necessário)
            return self._from_model_to_domain(endereco)
        except ObjectDoesNotExist:
            raise EntityNotFoundException(
                f"Endereço com ID {endereco_id} não encontrado."
            ) from e
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao buscar o endereço: {str(e)}"
            ) from e

    def list_all(self) -> list[EnderecoDomain]:
        """
        Retorna uma lista com todos os endereços cadastrados no banco de dados.

        Returns:
            List[EnderecoDomain]: Lista de todas as entidades de EnderecoDomain.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao listar os
            endereços.
        """
        try:
            # Lista todos os endereços do banco de dados
            enderecos = EnderecoModel.objects.all()
            return [self._from_model_to_domain(endereco) for endereco in enderecos]
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao listar os endereços: {str(e)}"
            ) from e

    def save(self, endereco: EnderecoDomain) -> None:
        """
        Salva ou atualiza um endereço no banco de dados.

        Args:
            endereco (EnderecoDomain): A entidade de endereço a ser salva ou
            atualizada no repositório.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao salvar o endereço.
        """
        try:
            # Converte EnderecoDomain para EnderecoModel e salva no banco de dados
            endereco_model = self._from_domain_to_model(endereco)
            endereco_model.save()
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao salvar o endereço: {str(e)}"
            ) from e

    def delete(self, endereco_id: int) -> None:
        """
        Remove um endereço do banco de dados pelo ID.

        Args:
            endereco_id (int): O identificador único do endereço a ser removido.

        Raises:
            EntityNotFoundException: Se o endereço com o ID fornecido não for
            encontrado no banco de dados.
            OperationFailedException: Se ocorrer um erro inesperado ao remover o
            endereço.
        """
        try:
            # Busca o endereço no banco de dados e o remove
            endereco = EnderecoModel.objects.get(id=endereco_id)
            endereco.delete()
        except ObjectDoesNotExist:
            raise EntityNotFoundException(
                f"Endereço com ID {endereco_id} não encontrado."
            ) from e
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao remover o endereço: {str(e)}"
            ) from e

    def list_by_pessoa_fisica(self, pessoa_fisica_id: int) -> list[EnderecoDomain]:
        """
        Retorna uma lista de endereços associados a uma pessoa física.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.

        Returns:
            List[EnderecoDomain]: Lista de endereços associados à pessoa física.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao listar os
            endereços.
        """
        try:
            # Busca endereços associados a uma pessoa física no banco de dados
            enderecos = EnderecoModel.objects.filter(pessoa_fisica_id=pessoa_fisica_id)
            return [self._from_model_to_domain(endereco) for endereco in enderecos]
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao listar endereços para pessoa física: {str(e)}"
            ) from e

    def list_by_pessoa_juridica(self, pessoa_juridica_id: int) -> list[EnderecoDomain]:
        """
        Retorna uma lista de endereços associados a uma pessoa jurídica.

        Args:
            pessoa_juridica_id (int): O identificador único da pessoa jurídica.

        Returns:
            List[EnderecoDomain]: Lista de endereços associados à pessoa jurídica.

        Raises:
            OperationFailedException: Se ocorrer um erro inesperado ao listar os
            endereços.
        """
        try:
            # Busca endereços associados a uma pessoa jurídica no banco de dados
            enderecos = EnderecoModel.objects.filter(pessoa_juridica_id=pessoa_juridica_id)
            return [self._from_model_to_domain(endereco) for endereco in enderecos]
        except Exception as e:
            raise OperationFailedException(
                f"Erro ao listar endereços para pessoa jurídica: {str(e)}"
            ) from e

    # Métodos de conversão (simples placeholders, ajuste conforme sua estrutura)

    def _from_model_to_domain(self, endereco_model: EnderecoModel) -> EnderecoDomain:
        """
        Converte um objeto EnderecoModel em um objeto EnderecoDomain.

        Args:
            endereco_model (EnderecoModel): A instância do modelo de banco de dados.

        Returns:
            EnderecoDomain: A instância de domínio convertida.
        """
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
            data_fim=endereco_model.data_fim,
        )

    def _from_domain_to_model(self, endereco: EnderecoDomain) -> EnderecoModel:
        """
        Converte um objeto EnderecoDomain em um objeto EnderecoModel.

        Args:
            endereco (EnderecoDomain): A instância de domínio.

        Returns:
            EnderecoModel: A instância do modelo de banco de dados convertida.
        """
        return EnderecoModel(
            id=endereco.endereco_id,
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
            data_fim=endereco.data_fim,
        )
