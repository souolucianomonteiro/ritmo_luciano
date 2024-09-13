# shared/plugins/value_objects/categoria.py

class Categoria:
    """
    Representa a categoria de um plugin.

    Este objeto de valor é imutável e serve para identificar
    a categoria a que um plugin pertence, como 'site', 'blog',
    ou 'reutilizável'. A imutabilidade garante que a categoria
    não possa ser alterada uma vez definida.
    """

    def __init__(self, valor: str):
        """
        Inicializa uma nova instância de Categoria.

        :param valor: Um valor string que representa a
        categoria do plugin.
        """
        if not valor:
            raise ValueError("Categoria não pode ser vazia")
        self._valor = valor

    @property
    def valor(self) -> str:
        """
           Retorna o valor da categoria.
           Acessa o valor do atributo _nome diretamente,
           como um atributo público, mas mantendo o encapsulamento.
        """
        return self._valor

    def __eq__(self, other) -> bool:
        """
        Verifica se duas categorias são iguais com base
        no valor.

        :param other: Outro objeto Categoria para comparação.
        :return: True se as categorias forem iguais,
        False caso contrário.
        """
        return (
            isinstance(other, Categoria) and
            self._valor == other.valor
        )
        
    def __str__(self) -> str:
        """
        Retorna a representação em string da categoria.
        Retorna uma representação textual da instância da classe, 
        que pode ser usada, por exemplo, para exibir o objeto
        em um log, em uma interface de usuário, ou ao
        serializar o objeto para alguma saída textual.
        :return: String representando a categoria.
        """
        return self._valor
