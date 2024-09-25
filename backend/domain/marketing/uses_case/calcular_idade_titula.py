"""Módulo implementa o caso de uso calcular idade do titular"""
from domain.marketing.domain_service.calcular_idade_titular import (
                                CalcularIdadePessoaFisicaService)
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain
from domain.marketing.repositories.pessoa_fisica import PessoaFisicaRepository


class CalcularIdadePessoaFisicaUseCase:
    """
    Caso de uso para calcular a idade de uma pessoa física.
    Este caso de uso interage com o repositório para obter os dados da pessoa
    e usa o serviço de domínio para calcular a idade.
    """
    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepository, calcular_idade_service: CalcularIdadePessoaFisicaService):
        self.pessoa_fisica_repository = pessoa_fisica_repository
        self.calcular_idade_service = calcular_idade_service

    def execute(self, pessoa_fisica_id: int) -> PessoaFisicaDomain:
        # Passo 1: Obter os dados da pessoa física através do repositório
        pessoa_fisica = self.pessoa_fisica_repository.get_by_id(pessoa_fisica_id)
        
        if pessoa_fisica is None:
            raise ValueError("Pessoa Física não encontrada.")
        
        # Passo 2: Calcular a idade usando o serviço de domínio
        pessoa_fisica = self.calcular_idade_service.calcular_idade(pessoa_fisica)
        
        # Retornar a pessoa física com a idade calculada
        return pessoa_fisica
