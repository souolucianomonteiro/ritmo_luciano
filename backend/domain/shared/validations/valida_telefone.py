from django.core.exceptions import ValidationError

def validar_telefone(telefone: str) -> bool:
    """
    Valida se o telefone fornecido é válido (padrão nacional ou internacional).

    Args:
        telefone (str): O número de telefone a ser validado.

    Returns:
        bool: Retorna True se o telefone for válido.

    Raises:
        ValidationError: Se o telefone não for válido.
    """
    # Remover espaços, traços e parênteses
    telefone = ''.join(filter(str.isdigit, telefone))

    # Verificar comprimento do número de telefone (fixo ou celular no Brasil)
    if len(telefone) < 10 or len(telefone) > 11:
        raise ValidationError("Número de telefone inválido.")
    
    return True
