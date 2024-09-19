"""
Módulo responsável pela definição da entidade Pessoa Física.

Este módulo contém a definição da classe de domínio PessoaFisicaDomain, que 
representa uma pessoa física no sistema, bem como suas interações com os 
endereços e demais atributos associados.

Classes:
    - PessoaFisicaDomain: Classe de domínio que modela os dados e comportamento de uma pessoa física, 
    incluindo seus endereços e outras informações pessoais.
"""
from typing import List
from typing import Optional, Literal
from dataclasses import dataclass
from datetime import date
from domain.website.entities.endereco import EnderecoDomain

@dataclass
class PessoaFisicaDomain:
    """
    Classe de domínio que representa uma pessoa física no sistema.

    Atributos:
        id (Optional[int]): Identificador único da pessoa física.
        primeiro_nome (str): Primeiro nome da pessoa física.
        sobrenome (str): Sobrenome da pessoa física.
        email (str): Email da pessoa física, utilizado como login.
        data_nascimento (Optional[date]): Data de nascimento da pessoa física.
        idade_anos (Optional[int]): Idade da pessoa física em anos.
        idade_meses (Optional[int]): Idade da pessoa física em meses.
        cpf (str): CPF da pessoa física, identificador único.
        genero (Literal['homem', 'mulher', 'homem bissexual', 'homem trans', 'mulher bissexual', 'mulher trans']):
            Identidade de gênero da pessoa física.
        profissao (Optional[str]): Profissão da pessoa física.
        ocupacao (Optional[str]): Ocupação atual da pessoa física.
        whatsapp (Optional[str]): Número de WhatsApp da pessoa física.
        redes_sociais (Optional[str]): Links para as redes sociais da pessoa física.
        conta_pessoa (bool): Indica se essa pessoa física é também uma conta no sistema.
        iniciador_conta_empresa (bool): Indica se essa pessoa física iniciou uma conta de pessoa jurídica.
    """
    id: Optional[int]
    primeiro_nome: str
    sobrenome: str
    email: str
    data_nascimento: Optional[date]
    idade_anos: Optional[int]
    idade_meses: Optional[int]
    cpf: str
    genero: Literal['homem', 'mulher', 'homem bissexual', 'homem trans', 'mulher bissexual', 'mulher trans']
    profissao: Optional[str]
    ocupacao: Optional[str]
    whatsapp: Optional[str]
    redes_sociais: Optional[str]
    conta_pessoa: bool
    iniciador_conta_empresa: bool
    enderecos: List[EnderecoDomain] = []
