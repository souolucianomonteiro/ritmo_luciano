"""
    Módulo responsável pela definição da classe de domínio AtividadeEconomicaDomain.

    Este módulo define a entidade AtividadeEconomicaDomain, que representa uma
    atividade econômica dentro do contexto de domínio da aplicação. A classe de 
    domínio é utilizada para encapsular a lógica de negócios relacionada à 
    atividade econômica e possui atributos para o código e a descrição da atividade.
"""


class AtividadeEconomicaDomain:
    """
    Classe de domínio que representa uma Atividade Econômica.

    Atributos:
    atividade_econ_id (int | None): Identificador único da atividade econômica.
    atividade_econ_codigo (str): Código único da atividade econômica.
    atividade_econ_descricao (str): Descrição única da atividade econômica.
    """

    def __init__(self, atividade_econ_id: int | None, atividade_econ_codigo: str, atividade_econ_descricao: str):
        """
        Construtor para a classe AtividadeEconomicaDomain.

        Args:
                atividade_econ_id (int | None): Identificador único da atividade econômica.
                atividade_econ_codigo (str): Código da atividade econômica.
                atividade_econ_descricao (str): Descrição da atividade econômica.
        """
        self.atividade_econ_id = atividade_econ_id
        self._atividade_econ_codigo = None
        self._atividade_econ_descricao = None
        self.set_atividade_econ_codigo(atividade_econ_codigo)
        self.set_atividade_econ_descricao(atividade_econ_descricao)

        # Getters e Setters

    @property
    def atividade_econ_codigo(self) -> str:
        """Retorna o código da atividade econômica."""
        return self._atividade_econ_codigo

    @property
    def atividade_econ_descricao(self) -> str:
        """Retorna a descrição da atividade econômica."""
        return self._atividade_econ_descricao

    def set_atividade_econ_codigo(self, codigo: str) -> None:
        """Define o código da atividade econômica, com validação."""
        if not codigo:
            raise ValueError("O código da atividade econômica não pode ser vazio.")
        if len(codigo) != 7:  # Supondo que o código de atividade econômica tenha 7 caracteres
            raise ValueError("O código da atividade econômica deve ter 7 caracteres.")
        self._atividade_econ_codigo = codigo

    def set_atividade_econ_descricao(self, descricao: str) -> None:
        """Define a descrição da atividade econômica, com validação."""
        if not descricao:
            raise ValueError("A descrição da atividade econômica não pode ser vazia.")
        self._atividade_econ_descricao = descricao

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância da classe AtividadeEconomicaDomain.

        Returns:
            str: Representação textual da atividade econômica.
        """
        return (f"AtividadeEconomicaDomain(id={self.atividade_econ_id}, "
               f"codigo={self.atividade_econ_codigo}, descricao={self.atividade_econ_descricao})")
