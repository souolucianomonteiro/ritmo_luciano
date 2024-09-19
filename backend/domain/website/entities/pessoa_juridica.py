from dataclasses import dataclass, field
from typing import Optional, List
from domain.website.entities.pessoa_fisica import PessoaFisicaDomain
from domain.website.entities.endereco import EnderecoDomain


@dataclass
class PessoaJuridicaDomain:
    """
    Classe de domínio que representa uma Pessoa Jurídica (empresa).

    Atributos:
        id (Optional[int]): Identificador único da pessoa jurídica.
        razao_social (str): Razão social da empresa.
        nome_fantasia (str): Nome fantasia da empresa.
        cnpj (str): CNPJ da empresa.
        inscricao_estadual (Optional[str]): Inscrição estadual da empresa.
        usuario_titular (PessoaFisicaDomain): Titular da empresa (pessoa física).
        iniciador_id (PessoaFisicaDomain): Pessoa que criou a conta da empresa (iniciador).
        enderecos (List[EnderecoDomain]): Lista de endereços associados à pessoa jurídica.
    """
    id: Optional[int]
    razao_social: str
    nome_fantasia: str
    cnpj: str
    inscricao_estadual: Optional[str]
    usuario_titular: PessoaFisicaDomain
    iniciador_id: PessoaFisicaDomain
    enderecos: List[EnderecoDomain] = field(default_factory=list)
