# apps/shared/validations/email_validation.py

from django.core.exceptions import ValidationError
from django.core.validators import validate_email as django_validate_email


def validar_email(email: str):
    """
    Valida se o email fornecido é válido.

    Args:
        email (str): O email a ser validado.

    Raises:
        ValidationError: Se o email for inválido.
    """
    try:
        django_validate_email(email)
    except ValidationError as exc:
        raise ValidationError("Email inválido.") from exc
