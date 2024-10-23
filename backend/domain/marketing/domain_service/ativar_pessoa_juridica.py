

from infrastructure.repositories.marketing.pessoa_juridica import (
                                            PessoaJuridicaRepository)
from domain.shared.exceptions.business_rule_violation_exception import (
                                            BusinessRuleViolationException)
from domain.shared.exceptions.entity_not_found_exception import (
                                            EntityNotFoundException)

class AtivarPessoaJuridica:
    """
    Serviço responsável pela ativação de uma conta de Pessoa Jurídica.
    
    A conta será ativada somente se houver exatamente 2 administradores.
    """

    def __init__(self, pessoa_juridica_id: int, pessoa_juridica_repository: PessoaJuridicaRepository):
        self.pessoa_juridica_id = pessoa_juridica_id
        self.pessoa_juridica_repository = pessoa_juridica_repository

    def executar(self) -> dict:
        """
        Ativa uma conta de Pessoa Jurídica se tiver exatamente 2 administradores.

        Raises:
            EntityNotFoundException: Se a pessoa jurídica não for encontrada.
            BusinessRuleViolationException: Se as regras de negócio não forem cumpridas.
        
        Returns:
            dict: Um dicionário com o status da operação e uma mensagem.
        """
        # Busca a Pessoa Jurídica no banco de dados via repositório
        pessoa_juridica = self.pessoa_juridica_repository.get_by_id(self.pessoa_juridica_id)

        if not pessoa_juridica:
            raise EntityNotFoundException('Pessoa Jurídica não encontrada.')

        # Verifica se a conta já está ativa
        if pessoa_juridica.ativa:
            return {
                'status': 'ja_ativa',
                'mensagem': 'A conta já está ativada.'
            }

        # Verifica se existem exatamente 2 administradores
        if pessoa_juridica.administradores.count() == 2:
            pessoa_juridica.ativa = True

            # Passa a entidade atualizada para o repositório salvar
            self.pessoa_juridica_repository.save(pessoa_juridica)

            return {
                'status': 'ativada',
                'mensagem': 'A conta foi ativada com sucesso.'
            }

        raise BusinessRuleViolationException('Para ativar, a conta deve ter exatamente 2 administradores.')
