# pylint: disable=no-member
"""
Repositório concreto para a entidade PessoaFisica.

Implementa as operações definidas na interface PessoaFisicaContract,
interagindo
com o banco de dados via as models do Django. Interage também com o repositório
de Endereco para manipulação de endereços.
"""

from typing import List, Optional
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.repositories.pessoa_fisica import PessoaFisicaContract
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.repositories.marketing.endereco import EnderecoRepository


class PessoaFisicaRepository(PessoaFisicaContract):
    """
    Repositório concreto para manipulação dos dados de PessoaFisica no banco de dados.
    Interage com o repositório de Endereco para gerenciar endereços.
    """

    def __init__(self):
        self.endereco_repository = EnderecoRepository()  # Instância do repositório de Endereco

    def get_by_id(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        """
        Recupera uma pessoa física pelo ID do banco de dados.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.

        Returns:
            PessoaFisicaDomain: A entidade de domínio correspondente, ou None se não encontrada.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            return self._model_to_domain(pessoa_model)
        except PessoaFisicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao buscar pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    def save(self, pessoa: PessoaFisicaDomain) -> PessoaFisicaDomain:
        """
        Salva ou atualiza uma pessoa física no banco de dados.

        Args:
            pessoa (PessoaFisicaDomain): A entidade de domínio a ser salva.

        Returns:
            PessoaFisicaDomain: A entidade de domínio salva ou atualizada.
        """
        try:
            pessoa_model, _ = PessoaFisicaModel.objects.update_or_create(
                pessoa_fisica_id=pessoa.pessoa_fisica_id,
                defaults={
                    'first_name': pessoa.primeiro_nome,
                    'last_name': pessoa.sobrenome,
                    'email': pessoa.email,
                    'cpf': pessoa.cpf,
                    'genero': pessoa.genero,
                    'telefone': pessoa.telefone,
                    'data_nascimento': pessoa.data_nascimento,
                    'foto': pessoa.foto,
                    'bios': pessoa.bios,
                    'situacao': pessoa.situacao,
                }
            )

            # Gerenciar o relacionamento de endereços
            if pessoa.enderecos:
                self._atualizar_enderecos(pessoa_model, pessoa.enderecos)

            return self._model_to_domain(pessoa_model)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao salvar a pessoa física: {str(exc)}") from exc

    def delete(self, pessoa_fisica_id: int) -> None:
        """
        Exclui uma pessoa física do banco de dados pelo ID.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física a ser excluída.

        Raises:
            EntityNotFoundException: Se a pessoa física não for encontrada.
        """
        try:
            PessoaFisicaModel.objects.filter(pessoa_fisica_id=pessoa_fisica_id).delete()
        except Exception as exc:
            raise OperationFailedException(f"Erro ao excluir pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    def list_all(self) -> List[PessoaFisicaDomain]:
        """
        Retorna uma lista de todas as pessoas físicas do banco de dados.

        Returns:
            List[PessoaFisicaDomain]: Lista de todas as entidades de domínio PessoaFisica.
        """
        try:
            pessoas = PessoaFisicaModel.objects.all()
            return [self._model_to_domain(pessoa) for pessoa in pessoas]
        except Exception as exc:
            raise OperationFailedException(f"Erro ao listar todas as pessoas físicas: {str(exc)}") from exc

    def alterar_status(self, pessoa_fisica_id: int, status: str) -> None:
        """
        Altera o status de uma pessoa física no banco de dados.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.
            status (str): O novo status a ser definido.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            pessoa_model.situacao = status
            pessoa_model.save()
        except PessoaFisicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao alterar o status da pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    def adicionar_endereco(self, pessoa_fisica_id: int, endereco: EnderecoRepository) -> None:
        """
        Adiciona um endereço à pessoa física usando o repositório de Endereco.

        Args:
            pessoa_fisica_id (int): O identificador da pessoa física.
            endereco (EnderecoDomain): O endereço a ser adicionado.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            endereco_salvo = self.endereco_repository.save(endereco)  # Usar o repositório para salvar o endereço
            pessoa_model.enderecos.add(endereco_salvo)  # Associa o endereço à pessoa física
            pessoa_model.save()
        except PessoaFisicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao adicionar endereço à pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    def remover_endereco(self, pessoa_fisica_id: int, endereco_id: int) -> None:
        """
        Remove um endereço da pessoa física usando soft delete
        pelo repositório de Endereco.

        Args:
            pessoa_fisica_id (int): O identificador da pessoa física.
            endereco_id (int): O identificador do endereço a ser removido.
        """
        try:
            # Verifica se a pessoa física existe
            if not PessoaFisicaModel.objects.filter(
                pessoa_fisica_id=pessoa_fisica_id
            ).exists():
                raise EntityNotFoundException(
                    f"Pessoa Física com ID {pessoa_fisica_id} não encontrada."
                )

            # Usar o repositório de Endereco para realizar o soft delete
            self.endereco_repository.soft_delete(endereco_id)

        except EntityNotFoundException as exc:
            raise EntityNotFoundException(
                f"Pessoa Física com ID {pessoa_fisica_id} não encontrada."
            ) from exc

        except Exception as exc:
            raise OperationFailedException(
                f"Erro ao remover endereço da pessoa física "
                f"com ID {pessoa_fisica_id}: {str(exc)}"
            ) from exc

    # Métodos auxiliares privados

    def _model_to_domain(self, pessoa_model: PessoaFisicaModel) -> PessoaFisicaDomain:
        """
        Converte um modelo de banco de dados em um objeto de domínio.

        Args:
            pessoa_model (PessoaFisicaModel): A instância do modelo de banco de dados.

        Returns:
            PessoaFisicaDomain: A instância de domínio convertida.
        """
        enderecos = [self.endereco_repository.get_by_id(e.id) for e in pessoa_model.enderecos.all()]

        return PessoaFisicaDomain(
            pessoa_fisica_id=pessoa_model.pessoa_fisica_id,
            primeiro_nome=pessoa_model.first_name,
            sobrenome=pessoa_model.last_name,
            email=pessoa_model.email,
            cpf=pessoa_model.cpf,
            genero=pessoa_model.genero,
            telefone=pessoa_model.telefone,
            data_nascimento=pessoa_model.data_nascimento,
            enderecos=enderecos,
            localizacao_criacao=None,  # Deve ser ajustado conforme a lógica de localização
            ultimo_login=pessoa_model.last_login,
            conta_pessoa=pessoa_model.conta_pessoa,
            iniciador_conta_empresa=pessoa_model.iniciador_conta_empresa,
            foto=pessoa_model.foto,
            bios=pessoa_model.bios,
            situacao=pessoa_model.situacao
        )

    def _atualizar_enderecos(self, pessoa_model: PessoaFisicaModel, enderecos: List[EnderecoRepository]) -> None:
        """
        Atualiza a lista de endereços de uma pessoa física usando o repositório de Endereco.

        Args:
            pessoa_model (PessoaFisicaModel): A instância do modelo de pessoa física.
            enderecos (List[EnderecoDomain]): Lista de endereços a serem atualizados.
        """
        pessoa_model.enderecos.clear()  # Limpar os endereços atuais

        for endereco in enderecos:
            endereco_salvo = self.endereco_repository.save(endereco)  # Salvar o endereço usando o repositório
            pessoa_model.enderecos.add(endereco_salvo)

        pessoa_model.save()
