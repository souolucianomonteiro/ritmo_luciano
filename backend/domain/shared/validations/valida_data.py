# apps/shared/validations/date_validation.py

from datetime import date
from django.core.exceptions import ValidationError

def validar_data_nascimento(data_nascimento: date):
    """
    Valida se a data de nascimento é uma data passada válida e se a pessoa tem uma idade plausível.
    """
    hoje = date.today()

    if data_nascimento >= hoje:
        raise ValidationError("A data de nascimento deve ser uma data passada.")
    
    idade = hoje.year - data_nascimento.year
    if idade > 120:
        raise ValidationError("A idade máxima permitida é de 120 anos.")
