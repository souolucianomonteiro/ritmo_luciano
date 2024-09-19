from django.core.exceptions import ValidationError

def validar_cnpj(cnpj: str) -> bool:
    """
    Valida se o CNPJ fornecido é válido.

    Args:
        cnpj (str): O CNPJ a ser validado (deve conter 14 dígitos).

    Returns:
        bool: Retorna True se o CNPJ for válido, ou levanta uma exceção caso seja inválido.

    Raises:
        ValidationError: Se o CNPJ não for válido.
    """
    # Remove caracteres não numéricos (separadores como pontos, traços e barras)
    cnpj = ''.join(filter(str.isdigit, cnpj))

    # Verifica se o CNPJ tem 14 dígitos
    if len(cnpj) != 14:
        raise ValidationError("CNPJ deve ter 14 dígitos.")

    # Elimina CNPJs com todos os dígitos iguais (ex.: 11.111.111/1111-11)
    if cnpj == cnpj[0] * 14:
        raise ValidationError("CNPJ inválido.")

    # Calcula o primeiro dígito verificador
    def calcular_digito(cnpj, pesos):
        soma = sum(int(digito) * peso for digito, peso in zip(cnpj, pesos))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Pesos para o primeiro e segundo dígito verificador
    pesos_primeiro = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

    primeiro_digito = calcular_digito(cnpj[:12], pesos_primeiro)
    segundo_digito = calcular_digito(cnpj[:13], pesos_segundo)

    # Verifica se os dois dígitos verificadores estão corretos
    if cnpj[-2:] != f"{primeiro_digito}{segundo_digito}":
        raise ValidationError("CNPJ inválido.")
    
    return True
