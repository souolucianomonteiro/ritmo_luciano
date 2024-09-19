# apps/shared/validations/cpf_validation.py

"""
Módulo de validação de CPF.

Este módulo contém a função `validar_cpf`, que realiza a validação de um CPF
(Cadastro de Pessoa Física) com base em sua estrutura e dígitos verificadores.

Funções:
    validar_cpf(cpf: str) -> bool:
        Valida se o CPF fornecido é válido, verificando tanto o formato quanto
        os dígitos verificadores.
"""

from django.core.exceptions import ValidationError


def validar_cpf(cpf: str) -> bool:
    """
    Valida se o CPF fornecido é válido.
    
    Args:
        cpf (str): O CPF a ser validado (deve conter 11 dígitos).
    
    Returns:
        bool: Retorna True se o CPF for válido, False caso contrário.
    """
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11 or cpf == cpf[0] * 11:
        raise ValidationError("CPF inválido.")

    def calcular_digito(cpf, peso):
        soma = sum(int(digito) * peso for digito, peso in zip(cpf, range(peso, 1, -1)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    primeiro_digito_verificador = calcular_digito(cpf[:9], 10)
    segundo_digito_verificador = calcular_digito(cpf[:10], 11)

    if cpf[-2:] != f"{primeiro_digito_verificador}{segundo_digito_verificador}":
        raise ValidationError("CPF inválido.")
    
    return True
