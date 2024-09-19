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
                 data_inicio: datetime = None,
                 data_fim: Optional[datetime] = None,
                 endereco_id: Optional[int] = None):
        self.endereco_id = endereco_id
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep
        self.pais = pais
        self.tipo = tipo
        self.pessoa_fisica_id = pessoa_fisica_id
        self.pessoa_juridica_id = pessoa_juridica_id
        self.is_active = is_active
        self.data_inicio = data_inicio if data_inicio else datetime.now()
        self.data_fim = data_fim

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}, {self.estado}, {self.pais}"

