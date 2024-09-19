# apps/shared/validations/dominio_validation.py

import re
from django.core.exceptions import ValidationError


def validar_dominio(dominio: str):
    """
    Valida se o domínio fornecido segue o padrão de um domínio válido.
    
    Args:
        dominio (str): O domínio a ser validado.
    
    Raises:
        ValidationError: Se o domínio for inválido.
    """
    regex = r'^[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(regex, dominio):
        raise ValidationError("Domínio inválido.")
