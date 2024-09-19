"""
Módulo da classe que faz a validação da Inscrição Estadual
"""
from django.core.exceptions import ValidationError


def validar_inscricao_estadual(inscricao_estadual: str) -> bool:
    """
    Valida se a Inscrição Estadual fornecida é válida com base no tamanho.

    A Inscrição Estadual deve ter entre 8 e 14 dígitos.

    Args:
        inscricao_estadual (str): A inscrição estadual a ser validada.

    Returns:
        bool: Retorna True se a inscrição estadual for válida, ou levanta uma exceção caso seja inválida.

    Raises:
        ValidationError: Se a inscrição estadual não for válida.
    """
    # Remove caracteres não numéricos
    inscricao_estadual = ''.join(filter(str.isdigit, inscricao_estadual))

    # Verifica se o tamanho está no intervalo de 8 a 14 dígitos
    if not 8 <= len(inscricao_estadual) <= 14:
        raise ValidationError("A Inscrição Estadual deve ter entre 8 e 14 dígitos.")
    
    # Retorna True se a inscrição estadual é válida em termos de tamanho
    return True
