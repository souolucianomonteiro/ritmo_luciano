# pylint: disable=no-member
"""
Módulo responsável pela implementação do repositório concreto de PessoaFisica.

Este módulo implementa o repositório concreto que interage com as models do banco
de dados PessoaFisicaModel, LocalizacaoModel e outras entidades relacionadas.
Ele implementa as operações definidas no contrato PessoaFisicaContract, realizando 
as interações com o banco de dados para salvar, buscar, atualizar, excluir, 
alterar status, gerenciar endereços e redes sociais associadas a uma pessoa física.

Classes:
    PessoaFisicaRepository: Repositório concreto que implementa o contrato
    PessoaFisicaContract para gerenciar PessoaFisica no banco de dados.

Métodos:
    - get_by_id: Busca uma pessoa física pelo ID.
    - save: Salva ou atualiza uma pessoa física e seus relacionamentos.
    - delete: Exclui uma pessoa física do banco de dados.
    - list_all: Lista todas as pessoas físicas cadastradas.
    - alterar_status: Altera o status da pessoa física.
    - adicionar_endereco: Adiciona um endereço à pessoa física.
    - remover_endereco: Remove um endereço da pessoa física.
    - _model_to_domain: Converte uma instância de PessoaFisicaModel para a entidade de domínio.
    - _atualizar_enderecos: Atualiza a lista de endereços de uma pessoa física.
    - _salvar_redes_sociais: Gerencia as redes sociais associadas a uma pessoa física.
"""
from typing import Optional, List
from django.db import transaction
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)
from domain.shared.exceptions.operation_failed_exception import (
                                            OperationFailedException)
from domain.marketing.entities.pessoa_juridica import PessoaJuridicaDomain
from domain.marketing.repositories.pessoa_juridica import (
                                        PessoaJuridicaContract)
from domain.marketing.domain_service.ativar_pessoa_juridica import (
                                                        AtivarPessoaJuridica)
from infrastructure.models.marketing.pessoa_juridica import PessoaJuridicaModel
from infrastructure.repositories.marketing.pessoa_fisica import (
                                            PessoaFisicaRepository)
from infrastructure.repositories.marketing.endereco import EnderecoRepository
from infrastructure.repositories.marketing.atividade_economica import (
                                                AtividadeEconomicaRepository)
from infrastructure.repositories.shared.resources.rede_social import (
                                                        RedeSocialRepository)


class PessoaJuridicaRepository(PessoaJuridicaContract):
    """
    Repositório concreto para a entidade Pessoa Jurídica, gerenciando
    a persistência e recuperação de dados no banco de dados e interagindo
    com outros repositórios para lidar com os relacionamentos.
    """

    def __init__(
        self,
        pessoa_fisica_repo: PessoaFisicaRepository,
        atividade_economica_repo: AtividadeEconomicaRepository,
        endereco_repo: EnderecoRepository,
        rede_social_repo: RedeSocialRepository
    ):
        self.pessoa_fisica_repo = pessoa_fisica_repo
        self.atividade_economica_repo = atividade_economica_repo
        self.endereco_repo = endereco_repo
        self.rede_social_repo = rede_social_repo

    @transaction.atomic
    def save(self, pessoa_juridica: PessoaJuridicaDomain, user) -> dict:
        """
        Salva ou atualiza uma pessoa jurídica no banco de dados.
        Retorna um dicionário contendo o objeto salvo e um booleano
        que indica se a entidade foi criada ou atualizada.

        Args:
            pessoa_juridica (PessoaJuridicaDomain): Entidade de domínio a ser salva.

        Returns:
            dict: Um dicionário com a entidade salva e um indicador de criação.
        """
        try:
            # Criar ou atualizar a entidade de Pessoa Jurídica
            pessoa_juridica_model, created = PessoaJuridicaModel.objects.update_or_create(
                id=pessoa_juridica.pessoa_juridica_id,  # Corrigido para pessoa_juridica_id
                defaults={
                    'razao_social': pessoa_juridica.razao_social,
                    'nome_fantasia': pessoa_juridica.nome_fantasia,
                    'cnpj': pessoa_juridica.cnpj,
                    'inscricao_estadual': pessoa_juridica.inscricao_estadual,
                    'website': pessoa_juridica.website,
                    'iniciador_id': pessoa_juridica.iniciador_id,
                }
            )

            # Garantir que os campos de auditoria sejam preenchidos passando o user
            pessoa_juridica_model.save(user=user)

            # Atualizar os relacionamentos de administradores, atividades econômicas, endereços e redes sociais
            self._atualizar_relacionamentos(pessoa_juridica_model, pessoa_juridica)

            # Retorna o objeto salvo e um indicador se foi criado ou atualizado
            return {
                'pessoa_juridica': pessoa_juridica_model,
                'created': created,
                
            }
        except Exception as e:
            raise OperationFailedException(f"Erro ao salvar a pessoa jurídica: {str(exc)}") from e

    @transaction.atomic
    def delete(self, pessoa_juridica_id: int, user) -> str:
        """
        Exclui uma pessoa jurídica pelo ID no banco de dados.
        Retorna uma mensagem de sucesso ou levanta uma exceção em caso de erro.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica a ser excluída.

        Returns:
            str: Mensagem de sucesso.
        """
        try:
            pessoa_juridica = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            pessoa_juridica.delete(user=user)     
            return "Pessoa Jurídica excluída com sucesso."
        except PessoaJuridicaModel.DoesNotExist:
            raise EntityNotFoundException(f"Pessoa Jurídica com ID {pessoa_juridica_id} não encontrada.") from e
        except Exception as e:
            raise OperationFailedException(f"Erro ao excluir a pessoa jurídica: {str(e)}") from e

    @transaction.atomic
    def get_by_id(self, pessoa_juridica_id: int) -> Optional[PessoaJuridicaDomain]:
        """
        Recupera uma pessoa jurídica pelo ID do banco de dados.

        Args:
            pessoa_juridica_id (int): O ID da pessoa jurídica.

        Returns:
            Optional[PessoaJuridicaDomain]: A entidade de domínio correspondente ou None.
        """
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)
            return self._model_to_domain(pessoa_juridica_model)
        except PessoaJuridicaModel.DoesNotExist as exc:
            raise EntityNotFoundException(f"Pessoa Jurídica com ID {pessoa_juridica_id} não encontrada.") from exc

    @transaction.atomic
    def list_all(self) -> List[PessoaJuridicaDomain]:
        """
        Retorna uma lista de todas as pessoas jurídicas cadastradas.

        Returns:
            List[PessoaJuridicaDomain]: Lista de todas as entidades de domínio PessoaJuridica.
        """
        try:
            pessoas_juridicas = PessoaJuridicaModel.objects.all()
            return [self._model_to_domain(pessoa) for pessoa in pessoas_juridicas]
        except Exception as exc:
            raise OperationFailedException(f"Erro ao listar todas as pessoas jurídicas: {str(exc)}") from exc

    def ativar_pessoa_juridica(self, pessoa_juridica_id: int) -> dict:
        """
        Ativa a pessoa jurídica se as condições forem atendidas.

        Args:
            pessoa_juridica_id (int): O identificador da pessoa jurídica a ser ativada.

        Returns:
            dict: Retorna o dicionário com o status e mensagem do serviço de ativação.
        """
        # Cria uma instância do serviço de ativação
        ativar_servico = AtivarPessoaJuridica(pessoa_juridica_id, self)

        # Executa o serviço de ativação e recebe o retorno
        resultado = ativar_servico.executar()

        # Retorna o resultado diretamente ou faz algum tratamento adicional se necessário
        return resultado

    def _atualizar_relacionamentos(self, pessoa_juridica_model: PessoaJuridicaModel, pessoa_juridica: PessoaJuridicaDomain) -> None:
        """
        Atualiza os relacionamentos de uma pessoa jurídica usando os repositórios
        correspondentes de Pessoa Física, Atividades Econômicas, Endereços e Redes Sociais.

        Args:
            pessoa_juridica_model (PessoaJuridicaModel): A instância do modelo de pessoa jurídica.
            pessoa_juridica (PessoaJuridicaDomain): A entidade de domínio de pessoa jurídica.
        """
        # Atualizar administradores usando o repositório de Pessoa Física
        administradores = self.pessoa_fisica_repo.get_by_ids(pessoa_juridica.administradores)
        pessoa_juridica_model.administradores.set(administradores)

        # Atualizar atividades econômicas usando o repositório de Atividades Econômicas
        atividades = self.atividade_economica_repo.get_by_ids(pessoa_juridica.atividades_economicas)
        pessoa_juridica_model.atividades_economicas.set(atividades)

        # Atualizar endereços usando o repositório de Endereços
        enderecos = self.endereco_repo.get_by_ids(pessoa_juridica.enderecos)
        pessoa_juridica_model.enderecos.set(enderecos)

        # Atualizar redes sociais usando o repositório de Redes Sociais
        redes_sociais = self.rede_social_repo.get_by_ids(pessoa_juridica.redes_sociais)
        pessoa_juridica_model.redes_sociais.set(redes_sociais)

        pessoa_juridica_model.save()

    def _model_to_domain(self, pessoa_juridica_model: PessoaJuridicaModel) -> PessoaJuridicaDomain:
        """
        Converte uma instância do modelo de banco de dados em uma entidade de domínio.

        Args:
            pessoa_juridica_model (PessoaJuridicaModel): A instância do modelo do banco de dados.

        Returns:
            PessoaJuridicaDomain: A entidade de domínio convertida.
        """
        return PessoaJuridicaDomain(
            pessoa_juridica_id=pessoa_juridica_model.id,  # Corrigido para pessoa_juridica_id
            razao_social=pessoa_juridica_model.razao_social,
            nome_fantasia=pessoa_juridica_model.nome_fantasia,
            cnpj=pessoa_juridica_model.cnpj,
            inscricao_estadual=pessoa_juridica_model.inscricao_estadual,
            administradores=list(pessoa_juridica_model.administradores.values_list('id', flat=True)),
            iniciador_id=pessoa_juridica_model.iniciador_id.id,
            enderecos=list(pessoa_juridica_model.enderecos.values_list('id', flat=True)),
            atividades_economicas=list(pessoa_juridica_model.atividades_economicas.values_list('id', flat=True)),
            website=pessoa_juridica_model.website,
            redes_sociais=list(pessoa_juridica_model.redes_sociais.values_list('id', flat=True))
        )
