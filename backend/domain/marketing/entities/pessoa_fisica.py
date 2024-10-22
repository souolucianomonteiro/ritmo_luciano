"""
Módulo de domínio responsável pela entidade PessoaFisicaDomain.

Este módulo define a entidade PessoaFisicaDomain, que representa uma pessoa
física
no sistema. A classe encapsula a lógica de negócio, incluindo validações de
CPF,
e-mail, telefone, data de nascimento, e relacionamentos com endereço e
localização.
"""

from datetime import date, datetime
from typing import Optional, List
from domain.shared.validations.valida_cpf import validar_cpf
from domain.shared.validations.valida_email import validar_email
from domain.shared.validations.valida_nascimento import validar_data_nascimento
from domain.shared.validations.valida_telefone import validar_telefone
from domain.marketing.entities.endereco import EnderecoDomain
from domain.shared.resources.entities.localizacao import LocalizacaoDomain
from domain.shared.resources.entities.rede_social import RedeSocialDomain
from domain.shared.exceptions.exception_account_person import (
    InvalidCPFException, InvalidEmailException, InvalidDateException,
    InvalidPhoneException)


class PessoaFisicaDomain:
    """
    Classe de domínio que representa uma pessoa física no sistema.

    Atributos:
        pessoa_fisica_id (Optional[int]): Identificador único da pessoa física.
        _primeiro_nome (str): Primeiro nome da pessoa física.
        _sobrenome (str): Sobrenome da pessoa física.
        _email (str): E-mail da pessoa física, usado como login.
        _data_nascimento (Optional[date]): Data de nascimento.
        _cpf (str): CPF da pessoa física (identificador único).
        _genero (str): Gênero da pessoa física.
        _telefone (str): Número de telefone da pessoa física (WhatsApp).
        _enderecos (List[EnderecoDomain]): Lista de endereços da pessoa física.
        _localizacao_criacao (LocalizacaoDomain): Localização da criação da conta.
        _ultimo_login (datetime): Data e hora do último login.
        conta_pessoa (bool): Indica se essa pessoa física é também uma conta.
        iniciador_conta_empresa (bool): Indica se a pessoa iniciou uma conta de empresa.
    """

    def __init__(
        self,
        pessoa_fisica_id: Optional[int] = None,
        primeiro_nome: str = '',
        sobrenome: str = '',
        email: str = '',
        data_nascimento: Optional[date] = None,
        cpf: str = '',
        genero: str = '',
        telefone: str = '',
        enderecos: Optional[List[EnderecoDomain]] = None,
        localizacao_criacao: Optional[LocalizacaoDomain] = None,
        ultimo_login: Optional[datetime] = None,
        conta_pessoa: Optional[bool] = None,
        iniciador_conta_empresa: Optional[bool] = None,
        foto: Optional[str] = None,
        bios: Optional[str] = None,
        situacao: Optional[str] = None,
        situacao_projeto: str = 'sem_projeto',
        redes_sociais: Optional[List[RedeSocialDomain]] = None 
        
    ):
        """
        Inicializa a instância de PessoaFisicaDomain com atributos obrigatórios e opcionais.

        Args:
            pessoa_fisica_id (Optional[int]): Identificador único da pessoa
            física.
            primeiro_nome (str): Primeiro nome da pessoa.
            sobrenome (str): Sobrenome da pessoa.
            email (str): Endereço de e-mail.
            data_nascimento (Optional[date]): Data de nascimento.
            cpf (str): CPF da pessoa física.
            genero (str): Gênero da pessoa.
            telefone (str): Número de telefone.
            enderecos (Optional[List[EnderecoDomain]]): Lista de endereços.
            localizacao_criacao (Optional[LocalizacaoDomain]): Localização da
            criação da conta.
            ultimo_login (Optional[datetime]): Data do último login.
            conta_pessoa (Optional[bool]): Indica se é uma conta de pessoa
            física.
            iniciador_conta_empresa (Optional[bool]): Indica se iniciou uma
            conta de empresa.
        """
        self.pessoa_fisica_id = pessoa_fisica_id
        self.set_primeiro_nome(primeiro_nome)
        self.set_sobrenome(sobrenome)
        self.set_email(email)
        self.set_data_nascimento(data_nascimento)
        self.set_cpf(cpf)
        self.set_telefone(telefone)
        self.genero = genero
        self.enderecos = enderecos or []
        self.localizacao_criacao = localizacao_criacao
        self.ultimo_login = ultimo_login
        self.conta_pessoa = conta_pessoa
        self.iniciador_conta_empresa = iniciador_conta_empresa
        self.foto = foto
        self.bios = bios
        self.situacao = situacao
        self.situacao_projeto = situacao_projeto
        self.redes_sociais = redes_sociais or []
        
        
    # Getters e Setters com validação e exceções

    @property
    def primeiro_nome(self) -> str:
        return self._primeiro_nome

    def set_primeiro_nome(self, nome: str) -> None:
        if not nome:
            raise ValueError("O primeiro nome não pode ser vazio.")
        self._primeiro_nome = nome

    @property
    def sobrenome(self) -> str:
        return self._sobrenome

    def set_sobrenome(self, sobrenome: str) -> None:
        if not sobrenome:
            raise ValueError("O sobrenome não pode ser vazio.")
        self._sobrenome = sobrenome

    @property
    def email(self) -> str:
        return self._email

    def set_email(self, email: str) -> None:
        if not validar_email(email):
            raise InvalidEmailException("O e-mail informado não é válido.")
        self._email = email

    @property
    def data_nascimento(self) -> Optional[date]:
        return self._data_nascimento

    def set_data_nascimento(self, data_nascimento: Optional[date]) -> None:
        if data_nascimento and not validar_data_nascimento(data_nascimento):
            raise InvalidDateException("A data de nascimento é inválida.")
        self._data_nascimento = data_nascimento

    @property
    def cpf(self) -> str:
        return self._cpf

    def set_cpf(self, cpf: str) -> None:
        if not validar_cpf(cpf):
            raise InvalidCPFException("O CPF informado é inválido.")
        self._cpf = cpf

    @property
    def telefone(self) -> str:
        return self._telefone

    def set_telefone(self, telefone: str) -> None:
        if not validar_telefone(telefone):
            raise InvalidPhoneException("O número de telefone informado é inválido.")
        self._telefone = telefone

    @property
    def ultimo_login(self) -> Optional[datetime]:
        return self._ultimo_login

    def set_ultimo_login(self, data_login: Optional[datetime]) -> None:
        self._ultimo_login = data_login

    @property
    def situacao_projeto(self) -> str:
        """Retorna a situação da pessoa física em relação a projetos."""
        return self._situacao_projeto

    @situacao_projeto.setter
    def situacao_projeto(self, situacao: str) -> None:
        """Atualiza a situação da pessoa física em relação a projetos."""
        if situacao not in ['ativo', 'sem_projeto']:
            raise ValueError("Situação inválida para projetos")
        self._situacao_projeto = situacao

    def atualizar_situacao_projeto(self, esta_em_projetos: bool) -> None:
        """
        Atualiza a situação da pessoa física com base na participação em projetos.
        
        Args:
            esta_em_projetos (bool): Se a pessoa está ou não participando de algum projeto.
        """
        self.situacao_projeto = 'ativo' if esta_em_projetos else 'sem_projeto'

    def associar_usuario_rede_social(self, rede_social: RedeSocialDomain, usuario: str) -> None:
        """
        Associa um nome de usuário à rede social selecionada.
        Args:
            rede_social (RedeSocialDomain): A rede social selecionada.
            usuario (str): O nome de usuário associado a essa rede social.
        """
        self.redes_sociais[rede_social] = usuario  # Associa a rede social ao nome de usuário

    def remover_usuario_rede_social(self, rede_social: RedeSocialDomain) -> None:
        """
        Remove o nome de usuário associado a uma rede social.
        Args:
            rede_social (RedeSocialDomain): A rede social a ser removida.
        """
        if rede_social in self.redes_sociais:
            del self.redes_sociais[rede_social]

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de PessoaFisicaDomain.

        Returns:
            str: Representação textual da pessoa física.
        """
        return (f"Pessoa: {self._primeiro_nome} {self._sobrenome}, CPF: {self._cpf}, "
                f"E-mail: {self._email}, Gênero: {self.genero}, Último Login: {self.ultimo_login}")
