"""
Módulo responsável pela definição da classe de domínio AtividadeEconomicaDomain.

Este módulo define a entidade AtividadeEconomicaDomain, que representa uma atividade econômica dentro
do contexto de domínio da aplicação. A classe de domínio é utilizada para encapsular a lógica de negócios 
relacionada à atividade econômica e possui atributos para o código e a descrição da atividade.

Classes:
    AtividadeEconomicaDomain: Classe de domínio que representa uma atividade econômica.
"""
from dataclasses import dataclass

@dataclass
class AtividadeEconomicaDomain:
    """
    Classe de domínio que representa uma Atividade Econômica.

    Atributos:
        id (int | None): Identificador único da atividade econômica.
        atividade_econ_codigo (str): Código único da atividade econômica.
        atividade_econ_descricao (str): Descrição única da atividade econômica.
    """
    id: int | None
    atividade_econ_codigo: str
    atividade_econ_descricao: str
