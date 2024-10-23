# shared/utilities/utils.py
from datetime import date
from typing import Optional


def calcular_idade(data_nascimento: Optional[date]) -> dict:
    """
    Calcula a idade exata em anos e meses com base na data de nascimento.

    Args:
        data_nascimento (Optional[date]): A data de nascimento da pessoa.

    Returns:
        dict: Dicionário contendo a idade em anos e meses.
    """
    if not data_nascimento:
        return {"anos": None, "meses": None}

    hoje = date.today()
    anos = hoje.year - data_nascimento.year
    meses = hoje.month - data_nascimento.month

    # Ajusta a idade se o mês atual for anterior ao mês de nascimento
    if meses < 0:
        anos -= 1
        meses += 12

    return {"anos": anos, "meses": meses}
