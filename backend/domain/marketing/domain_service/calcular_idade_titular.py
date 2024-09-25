""" Módulo que implementa o serviço de domínio
calcular idade da pessoa física.
"""

from datetime import date
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain


class CalcularIdadePessoaFisicaService:
    """Calcular a idade da pessoa fisica em anos e meses"""
    @staticmethod
    def calcular_idade(pessoa_fisica: PessoaFisicaDomain) -> (
                                            PessoaFisicaDomain):
        """
        Método que calcula a idade da pessoa física em anos e meses com base
        na data de nascimento.
        """
        if pessoa_fisica.data_nascimento:
            hoje = date.today()
            idade_anos = hoje.year - pessoa_fisica.data_nascimento.year
            idade_meses = hoje.month - pessoa_fisica.data_nascimento.month
            if idade_meses < 0:
                idade_anos -= 1
                idade_meses += 12
            pessoa_fisica.idade_anos = idade_anos
            pessoa_fisica.idade_meses = idade_meses
        return pessoa_fisica
