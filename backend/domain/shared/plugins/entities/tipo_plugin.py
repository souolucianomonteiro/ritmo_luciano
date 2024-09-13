"""
Módulo que define a entidade `TipoPlugin` no domínio do sistema.

O `TipoPlugin` representa diferentes tipos de plugins que podem ser utilizados
no sistema.
"""


class TipoPlugin:
    """
    Classe que representa um Tipo de Plugin.

    O TipoPlugin classifica os plugins do sistema, diferenciando suas
    funcionalidades e características.

    Atributos:
        nome (str): O nome do tipo de plugin.
    """

    def __init__(self, nome: str):
        """
        Inicializa uma nova instância da classe TipoPlugin.

        Args:
            nome (str): O nome do tipo de plugin.
        """
        self.nome = nome

    # Métodos adicionais relacionados à lógica de domínio desta entidade
    # devem ser adicionados aqui.
