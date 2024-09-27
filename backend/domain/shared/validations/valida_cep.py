from django.core.exceptions import ValidationError

def validar_cep(cep: str) -> bool:
    """
    Valida o formato do CEP (Código Postal Brasileiro).

    Args:
        cep (str): O CEP a ser validado.

    Returns:
        bool: Retorna True se o CEP for válido.

    Raises:
        ValidationError: Se o CEP for inválido.
    """
    # Remover traços e espaços
    cep = ''.join(filter(str.isdigit, cep))

    # Verificar se o CEP tem 8 dígitos
    if len(cep) != 8:
        raise ValidationError("CEP inválido. Deve conter 8 dígitos.")
    
    return True
