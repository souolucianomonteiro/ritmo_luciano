"""
Módulo responsável pela definição da classe de domínio EnderecoDomain.

Este módulo define a entidade EnderecoDomain, que representa um endereço 
dentro do contexto de domínio da aplicação. A classe de domínio é utilizada 
para encapsular a lógica de negócios relacionada a endereços, permitindo a 
associação de endereços a pessoas físicas e jurídicas. Ela inclui atributos 
como rua, número, complemento, bairro, cidade, estado, CEP, país, tipo de 
endereço (residencial, comercial ou correspondência), além de data de início 
e fim de validade, e um indicador de atividade.

Classes:
    EnderecoDomain: Entidade que representa um endereço no sistema.
"""

from typing import Literal, Optional
from datetime import datetime


class EnderecoDomain:
    """
    Classe de domínio que representa um endereço no sistema.

    Atributos:
        endereco_id (Optional[int]): Identificador único do endereço.
        rua (str): Nome da rua.
        numero (str): Número da casa ou prédio.
        complemento (Optional[str]): Complemento, como apartamento ou sala.
        bairro (str): Nome do bairro.
        cidade (str): Nome da cidade.
        estado (str): Nome do estado.
        cep (str): Código postal (CEP).
        pais (str): Nome do país.
        tipo (Literal): Tipo de endereço (residencial, comercial,
        correspondência).
        pessoa_fisica_id (Optional[int]): ID da pessoa física associada.
        pessoa_juridica_id (Optional[int]): ID da pessoa jurídica associada.
        is_active (bool): Indica se este é o endereço atual.
        data_inicio (datetime): Data de início de validade do endereço.
        data_fim (Optional[datetime]): Data de término de validade do endereço 
        (para histórico).
    """

    def __init__(self, 
                 rua: str,
                 numero: str,
                 complemento: Optional[str],
                 bairro: str,
                 cidade: str,
                 estado: str,
                 cep: str,
                 pais: str = 'Brasil',
                 tipo: Literal['residencial', 'comercial', 'correspondencia'] = 'residencial',
                 pessoa_fisica_id: Optional[int] = None,
                 pessoa_juridica_id: Optional[int] = None,
                 is_active: bool = True,
                 data_inicio: Optional[datetime] = None,
                 data_fim: Optional[datetime] = None,
                 endereco_id: Optional[int] = None):
        self.endereco_id = endereco_id
        self._rua = None
        self._numero = None
        self._complemento = complemento
        self._bairro = None
        self._cidade = None
        self._estado = None
        self._cep = None
        self._pais = None
        self._tipo = None
        self.set_rua(rua)
        self.set_numero(numero)
        self.set_bairro(bairro)
        self.set_cidade(cidade)
        self.set_estado(estado)
        self.set_cep(cep)
        self.set_pais(pais)
        self.set_tipo(tipo)
        self.pessoa_fisica_id = pessoa_fisica_id
        self.pessoa_juridica_id = pessoa_juridica_id
        self.is_active = is_active
        self.data_inicio = data_inicio if data_inicio else datetime.now()
        self.data_fim = data_fim

    # Getters e Setters com validações

    @property
    def rua(self):
        return self._rua

    def set_rua(self, rua: str):
        if not rua:
            raise ValueError("Rua não pode ser vazia.")
        self._rua = rua

    @property
    def numero(self):
        return self._numero

    def set_numero(self, numero: str):
        if not numero:
            raise ValueError("Número não pode ser vazio.")
        self._numero = numero

    @property
    def bairro(self):
        return self._bairro

    def set_bairro(self, bairro: str):
        if not bairro:
            raise ValueError("Bairro não pode ser vazio.")
        self._bairro = bairro

    @property
    def cidade(self):
        return self._cidade

    def set_cidade(self, cidade: str):
        if not cidade:
            raise ValueError("Cidade não pode ser vazia.")
        self._cidade = cidade

    @property
    def estado(self):
        return self._estado

    def set_estado(self, estado: str):
        if not estado:
            raise ValueError("Estado não pode ser vazio.")
        self._estado = estado

    @property
    def cep(self):
        return self._cep

    def set_cep(self, cep: str):
        if len(cep) != 8:
            raise ValueError("CEP inválido, deve ter 8 caracteres.")
        self._cep = cep

    @property
    def pais(self):
        return self._pais

    def set_pais(self, pais: str):
        if not pais:
            raise ValueError("País não pode ser vazio.")
        self._pais = pais

    @property
    def tipo(self):
        return self._tipo

    def set_tipo(self, tipo: Literal['residencial', 'comercial', 'correspondencia']):
        if tipo not in ['residencial', 'comercial', 'correspondencia']:
            raise ValueError("Tipo de endereço inválido.")
        self._tipo = tipo

    def __str__(self):
        """
        Retorna uma representação amigável do endereço.
        """
        return f"{self.rua}, {self.numero} - {self.cidade}, {self.estado}, {self.pais}"
