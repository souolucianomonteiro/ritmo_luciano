"""
Módulo responsável pela definição da entidade Pessoa Física.

Este módulo contém a definição da classe de domínio PessoaFisicaDomain, que 
representa uma pessoa física no sistema, bem como suas interações com os 
endereços e demais atributos associados.

Classes:
    - PessoaFisicaDomain: Classe de domínio que modela os dados e comportamento de uma pessoa física, 
    incluindo seus endereços e outras informações pessoais.
"""
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
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
    id: Optional[int] = None
    primeiro_nome: str = ''
    sobrenome: str = ''
    email: str = ''
    data_nascimento: Optional[date] = None
    idade_anos: Optional[int] = None
    idade_meses: Optional[int] = None
    cpf: str = ''
    genero: str = ''
    profissao: Optional[str] = None
    ocupacao: str = ''
    whatsapp: str = ''
    redes_sociais: str = ''
    conta_pessoa: Optional[bool] = None
    iniciador_conta_empresa: Optional[bool] = None
    foto: Optional[str] = None
    bios: Optional[str] = None
    situacao: Optional[str] = None
    enderecos: List[str] = field(default_factory=list)  # Use default_factory para listas
    usuario_tipos: List[str] = field(default_factory=list)  # Também use para tipos de usuário
