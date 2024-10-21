"""
Módulo de exceções customizadas para validações relacionadas à Conta Pessoa.

Este módulo encapsula todas as exceções personalizadas que são lançadas quando
há falhas nas validações de CPF, e-mail, telefone ou data de nascimento.
"""


class InvalidCPFException(Exception):
    """
    Exceção lançada quando um CPF inválido é informado.
    """
    def __init__(self, message="O CPF informado é inválido."):
        self.message = message
        super().__init__(self.message)


class InvalidEmailException(Exception):
    """
    Exceção lançada quando um e-mail inválido é informado.
    """
    def __init__(self, message="O e-mail informado é inválido."):
        self.message = message
        super().__init__(self.message)


class InvalidDateException(Exception):
    """
    Exceção lançada quando uma data de nascimento inválida é informada.
    """
    def __init__(self, message="A data de nascimento é inválida."):
        self.message = message
        super().__init__(self.message)


class InvalidPhoneException(Exception):
    """
    Exceção lançada quando um número de telefone inválido é informado.
    """
    def __init__(self, message="O número de telefone informado é inválido."):
        self.message = message
        super().__init__(self.message)
