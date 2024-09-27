from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

def validar_url(url: str) -> bool:
    """
    Valida se a URL fornecida é válida.

    Args:
        url (str): A URL a ser validada.

    Returns:
        bool: Retorna True se a URL for válida.

    Raises:
        ValidationError: Se a URL não for válida.
    """
    validator = URLValidator()
    try:
        validator(url)
    except ValidationError:
        raise ValidationError("URL inválida.")
    
    return True
