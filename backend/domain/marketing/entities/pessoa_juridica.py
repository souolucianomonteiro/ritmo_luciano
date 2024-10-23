"""
Módulo de domínio responsável pela entidade PessoaJuridicaDomain.

Este módulo define a classe PessoaJuridicaDomain, que representa uma empresa
no sistema. A classe encapsula a lógica de negócio, incluindo validações de 
CNPJ, razão social, administradores, e a situação da empresa. As validações
e regras de negócio são aplicadas para garantir que as operações respeitem 
as restrições de domínio.

Exceções Personalizadas:
- InvalidInputException: Lançada quando há uma entrada inválida em atributos 
  como CNPJ, razão social ou nome fantasia.
- BusinessRuleViolationException: Lançada para violações de regras de negócio, 
  como a adição de mais de dois administradores.
- ValidationException: Lançada para validações gerais, como situação inválida 
  da empresa.

Classes:
- PessoaJuridicaDomain: Representa uma entidade de domínio que encapsula a 
  lógica e os dados de uma pessoa jurídica.
"""
from typing import Optional, List
from domain.shared.validations.valida_cnpj import validar_cnpj
from domain.shared.exceptions.invalid_input_exception import (
                                            InvalidInputException)
from domain.shared.exceptions.business_rule_violation_exception import (
                                            BusinessRuleViolationException)
from domain.shared.exceptions.validation_exception import ValidationException


class PessoaJuridicaDomain:
    """
    Classe de domínio que representa uma Pessoa Jurídica (empresa).

    Atributos:
        _pessoa_juridica_id (Optional[int]): Identificador único da pessoa jurídica.
        _razao_social (str): Razão social da empresa.
        _nome_fantasia (str): Nome fantasia da empresa.
        _cnpj (str): CNPJ da empresa, que deve ser único e validado.
        _inscricao_estadual (Optional[str]): Inscrição estadual da empresa.
        _administradores (List[int]): IDs dos administradores (até 2), sendo um deles o iniciador.
        _iniciador_id (int): ID da pessoa física que criou a conta da empresa (iniciador).
        _enderecos (List[int]): Lista de IDs dos endereços associados à pessoa jurídica.
        _atividades_economicas (List[int]): Lista de IDs das atividades econômicas associadas.
        _website (Optional[str]): Website da empresa.
        _redes_sociais (List[int]): Lista de IDs das redes sociais associadas.
        _situacao (str): Situação atual da empresa (criada, ativada, inativada, suspensa).
    """

    def __init__(
        self,
        pessoa_juridica_id: Optional[int] = None,
        razao_social: str = '',
        nome_fantasia: str = '',
        cnpj: str = '',
        inscricao_estadual: Optional[str] = None,
        administradores: Optional[List[int]] = None,
        iniciador_id: Optional[int] = None,
        enderecos: Optional[List[int]] = None,
        atividades_economicas: Optional[List[int]] = None,
        website: Optional[str] = None,
        redes_sociais: Optional[List[int]] = None,
        situacao: str = 'criada'  # Situação inicial como "criada"
    ):
        """
        Inicializa uma instância de PessoaJuridicaDomain com as validações 
        necessárias.

        Args:
            pessoa_juridica_id (Optional[int]): Identificador único da pessoa 
            jurídica.
            razao_social (str): Razão social da empresa.
            nome_fantasia (str): Nome fantasia da empresa.
            cnpj (str): CNPJ da empresa.
            inscricao_estadual (Optional[str]): Inscrição estadual.
            administradores (List[int]): IDs dos administradores 
            (mínimo 1, máximo 2).
            iniciador_id (int): ID da pessoa física que criou a conta da 
            empresa.
            enderecos (List[int]): Lista de IDs dos endereços associados à 
            empresa.
            atividades_economicas (List[int]): Lista de IDs das atividades
            econômicas.
            website (Optional[str]): Website da empresa.
            redes_sociais (List[int]): Lista de IDs das redes sociais
            associadas.
            situacao (str): Situação da empresa (criada, ativada, inativada,
            suspensa).
        """
        self._pessoa_juridica_id = pessoa_juridica_id
        self.set_razao_social(razao_social)
        self.set_nome_fantasia(nome_fantasia)
        self.set_cnpj(cnpj)
        self._inscricao_estadual = inscricao_estadual
        self._administradores = administradores or []
        self._iniciador_id = iniciador_id
        self._enderecos = enderecos or []
        self._atividades_economicas = atividades_economicas or []
        self._website = website
        self._redes_sociais = redes_sociais or []
        self.set_situacao(situacao)

        # Valida os administradores
        self.validar_administradores()

    # Getters e Setters com Validações

    @property
    def pessoa_juridica_id(self) -> Optional[int]:
        return self._pessoa_juridica_id

    @property
    def razao_social(self) -> str:
        return self._razao_social

    def set_razao_social(self, razao_social: str) -> None:
        if not razao_social:
            raise InvalidInputException("A razão social não pode ser vazia.")
        self._razao_social = razao_social

    @property
    def nome_fantasia(self) -> str:
        return self._nome_fantasia

    def set_nome_fantasia(self, nome_fantasia: str) -> None:
        if not nome_fantasia:
            raise InvalidInputException("O nome fantasia não pode ser vazio.")
        self._nome_fantasia = nome_fantasia

    @property
    def cnpj(self) -> str:
        return self._cnpj

    def set_cnpj(self, cnpj: str) -> None:
        if not validar_cnpj(cnpj):
            raise InvalidInputException("O CNPJ informado é inválido.")
        self._cnpj = cnpj

    @property
    def inscricao_estadual(self) -> Optional[str]:
        return self._inscricao_estadual

    def set_inscricao_estadual(self, inscricao_estadual: Optional[str]) -> None:
        self._inscricao_estadual = inscricao_estadual

    @property
    def administradores(self) -> List[int]:
        return self._administradores

    def validar_administradores(self) -> None:
        """
        Valida se os administradores são no mínimo 1 e no máximo 2, garantindo que
        um dos administradores pode ser o iniciador.
        """
        if len(self._administradores) < 1:
            raise BusinessRuleViolationException("Deve haver no mínimo 1 administrador.")
        if len(self._administradores) > 2:
            raise BusinessRuleViolationException("Não pode haver mais de 2 administradores.")

    def adicionar_administrador(self, administrador_id: int) -> None:
        """
        Adiciona um administrador à lista, respeitando o limite de 2 administradores.
        """
        if len(self._administradores) >= 2:
            raise BusinessRuleViolationException("Não é possível adicionar mais de 2 administradores.")
        if administrador_id not in self._administradores:
            self._administradores.append(administrador_id)

    def remover_administrador(self, administrador_id: int) -> None:
        """
        Remove um administrador da lista, desde que não deixe menos de 1.
        """
        if len(self._administradores) <= 1:
            raise BusinessRuleViolationException("Deve haver no mínimo 1 administrador.")
        if administrador_id in self._administradores:
            self._administradores.remove(administrador_id)

    @property
    def iniciador_pessoa_juridica_id(self) -> int:
        return self._iniciador_id

    def set_iniciador_id(self, iniciador_id: int) -> None:
        if not iniciador_id:
            raise InvalidInputException("O iniciador deve ser informado.")
        self._iniciador_id = iniciador_id

    @property
    def enderecos(self) -> List[int]:
        return self._enderecos

    def adicionar_endereco(self, endereco_id: int) -> None:
        """Adiciona um novo endereço à pessoa jurídica."""
        if endereco_id not in self._enderecos:
            self._enderecos.append(endereco_id)

    def remover_endereco(self, endereco_id: int) -> None:
        """Remove um endereço da pessoa jurídica."""
        if endereco_id in self._enderecos:
            self._enderecos.remove(endereco_id)

    @property
    def atividades_economicas(self) -> List[int]:
        return self._atividades_economicas

    def adicionar_atividade_economica(self, atividade_id: int) -> None:
        """Adiciona uma atividade econômica à empresa."""
        if atividade_id not in self._atividades_economicas:
            self._atividades_economicas.append(atividade_id)

    def remover_atividade_economica(self, atividade_id: int) -> None:
        """Remove uma atividade econômica da empresa."""
        if atividade_id in self._atividades_economicas:
            self._atividades_economicas.remove(atividade_id)

    @property
    def website(self) -> Optional[str]:
        return self._website

    @website.setter
    def website(self, website: Optional[str]) -> None:
        self._website = website

    @property
    def redes_sociais(self) -> List[int]:
        return self._redes_sociais

    def adicionar_rede_social(self, rede_social_id: int) -> None:
        """Adiciona uma rede social à empresa."""
        if rede_social_id not in self._redes_sociais:
            self._redes_sociais.append(rede_social_id)

    def remover_rede_social(self, rede_social_id: int) -> None:
        """Remove uma rede social da empresa."""
        if rede_social_id in self._redes_sociais:
            self._redes_sociais.remove(rede_social_id)

    @property
    def situacao(self) -> str:
        return self._situacao

    def set_situacao(self, situacao: str) -> None:
        """
        Define a situação da empresa. Lança exceção se a situação for inválida.
        """
        if situacao not in ['criada', 'ativada', 'inativada', 'suspensa']:
            raise ValidationException("Situação inválida.")
        self._situacao = situacao

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da instância de PessoaJuridicaDomain.

        Returns:
            str: Representação textual da pessoa jurídica.
        """
        return (f"Empresa: {self._razao_social}, CNPJ: {self._cnpj}, "
                f"Administradores: {self._administradores}, "
                f"Atividades Econômicas: {self._atividades_economicas}")
