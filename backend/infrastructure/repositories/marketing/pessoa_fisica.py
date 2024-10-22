# pylint: disable=no-member
"""
Módulo responsável pela implementação do repositório concreto de PessoaFisica.

Este módulo implementa o repositório concreto que interage com as models do banco
de dados PessoaFisicaModel e LocalizacaoModel. Ele implementa as operações definidas
no contrato PessoaFisicaContract, realizando as interações com o banco de dados
para salvar, buscar, alterar status e gerenciar endereços e localização.

Classes:
    PessoaFisicaRepository: Repositório concreto que implementa o contrato
    PessoaFisicaContract para gerenciar PessoaFisica no banco de dados.
"""

from typing import List, Optional
from django.db import transaction  # Importa o módulo para transações atômicas
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.repositories.pessoa_fisica import PessoaFisicaContract
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.repositories.marketing.endereco import EnderecoRepository
from infrastructure.repositories.shared.resources.localizacao import (
                                                    LocalizacaoRepository)


class PessoaFisicaRepository(PessoaFisicaContract):
    """
    Repositório concreto para a entidade de domínio PessoaFisica.

    Este repositório implementa o contrato PessoaFisicaContract, gerenciando
    as operações de persistência e recuperação de PessoaFisica no banco
    de dados, além de gerenciar os relacionamentos com endereços e localização.
    """

    def __init__(self):
        self.endereco_repository = EnderecoRepository()  # Repositório de Endereço
        self.localizacao_repository = LocalizacaoRepository()  # Repositório de Localização

    def get_by_id(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        """
        Recupera uma pessoa física pelo ID do banco de dados.

        Args:
            pessoa_fisica_id (int): O identificador único da pessoa física.

        Returns:
            Optional[PessoaFisicaDomain]: A entidade de domínio correspondente, ou None se não encontrada.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            return self._model_to_domain(pessoa_model)
        except PessoaFisicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao buscar pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    @transaction.atomic  # Inicia uma transação atômica
    def save(self, pessoa: PessoaFisicaDomain) -> PessoaFisicaDomain:
        """
        Salva ou atualiza uma pessoa física no banco de dados.

        Este método realiza a conversão da entidade de domínio PessoaFisicaDomain
        para a model PessoaFisicaModel e persiste os dados no banco. Além disso,
        salva os endereços e localização associados à pessoa física.

        Usa transações atômicas para garantir que todas as operações sejam bem-sucedidas,
        ou sejam revertidas em caso de falha.

        Args:
            pessoa (PessoaFisicaDomain): A entidade de domínio a ser salva.

        Returns:
            PessoaFisicaDomain: A entidade de domínio salva ou atualizada.
        """
        try:
            # Salva ou atualiza os dados da pessoa física no banco de dados
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

            # Gerencia o relacionamento de endereços
            if pessoa.enderecos:
                self._atualizar_enderecos(pessoa_model, pessoa.enderecos)

            # Salva a localização de criação da conta, se fornecida
            if pessoa.localizacao_criacao:
                self.localizacao_repository.salvar(pessoa.localizacao_criacao)

            return self._model_to_domain(pessoa_model)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao salvar a pessoa física: {str(exc)}") from exc

    @transaction.atomic  # Garante que a exclusão seja atômica
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

    @transaction.atomic  # Garante que a alteração de status seja atômica
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

    @transaction.atomic  # Garante que a adição de endereço seja atômica
    def adicionar_endereco(self, pessoa_fisica_id: int, endereco) -> None:
        """
        Adiciona um endereço à pessoa física.

        Args:
            pessoa_fisica_id (int): O identificador da pessoa física.
            endereco (EnderecoDomain): O endereço a ser adicionado.
        """
        try:
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            endereco_salvo = self.endereco_repository.save(endereco)
            pessoa_model.enderecos.add(endereco_salvo)
            pessoa_model.save()
        except PessoaFisicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from exc
        except Exception as exc:
            raise OperationFailedException(f"Erro ao adicionar endereço à pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    @transaction.atomic  # Garante que a remoção de endereço seja atômica
    def remover_endereco(self, pessoa_fisica_id: int, endereco_id: int) -> None:
        """
        Remove um endereço da pessoa física usando soft delete.

        Args:
            pessoa_fisica_id (int): O identificador da pessoa física.
            endereco_id (int): O identificador do endereço a ser removido.
        """
        try:
            if not PessoaFisicaModel.objects.filter(pessoa_fisica_id=pessoa_fisica_id).exists():
                raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.")

            self.endereco_repository.soft_delete(endereco_id)
        except Exception as exc:
            raise OperationFailedException(f"Erro ao remover endereço da pessoa física com ID {pessoa_fisica_id}: {str(exc)}") from exc

    # Métodos auxiliares privados

    def _model_to_domain(self, pessoa_model: PessoaFisicaModel) -> PessoaFisicaDomain:
        """
        Converte um modelo de banco de dados em um objeto de domínio.

        Args:
            pessoa_model (PessoaFisicaModel): A instância do modelo de banco de dados.

        Returns:
            PessoaFisicaDomain: A instância de domínio convertida.
        """
        # Busca os endereços associados
        enderecos = [self.endereco_repository.get_by_id(e.id) for e in pessoa_model.enderecos.all()]

        # Busca a localização associada, se aplicável
        localizacao = self.localizacao_repository.buscar_por_id(pessoa_model.localizacao_id) if pessoa_model.localizacao_id else None

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
            localizacao_criacao=localizacao,
            ultimo_login=pessoa_model.last_login,
            conta_pessoa=pessoa_model.conta_pessoa,
            iniciador_conta_empresa=pessoa_model.iniciador_conta_empresa,
            foto=pessoa_model.foto,
            bios=pessoa_model.bios,
            situacao=pessoa_model.situacao
        )

    def _atualizar_enderecos(self, pessoa_model: PessoaFisicaModel, enderecos: List) -> None:
        """
        Atualiza a lista de endereços de uma pessoa física.

        Este método limpa os endereços existentes e associa a nova lista
        de endereços fornecida.

        Args:
            pessoa_model (PessoaFisicaModel): A instância do modelo de pessoa física.
            enderecos (List[EnderecoDomain]): Lista de endereços a serem atualizados.
        """
        pessoa_model.enderecos.clear()  # Limpa os endereços atuais

        for endereco in enderecos:
            endereco_salvo = self.endereco_repository.save(endereco)  # Salva o novo endereço
            pessoa_model.enderecos.add(endereco_salvo)

        pessoa_model.save()

    def atualizar_situacao_projeto(self, pessoa_fisica_id: int) -> None:
        """
        Atualiza a situação de projeto da pessoa física com base na quantidade de projetos.

        Args:
            pessoa_fisica_id (int): O ID da pessoa física cuja situação de projeto será atualizada.
        """
        try:
            # Conta quantos projetos a pessoa está participando
            quantidade_projetos = ProjetoUsuario.objects.filter(pessoa_fisica_id=pessoa_fisica_id).count()

            # Busca a pessoa no banco de dados e atualiza sua situação de projeto
            pessoa_model = PessoaFisicaModel.objects.get(pessoa_fisica_id=pessoa_fisica_id)
            pessoa_model.situacao_projeto = 'ativo' if quantidade_projetos > 0 else 'sem_projeto'
            pessoa_model.save()

        except PessoaFisicaModel.DoesNotExist:
            raise EntityNotFoundException(f"Pessoa Física com ID {pessoa_fisica_id} não encontrada.") from exc
