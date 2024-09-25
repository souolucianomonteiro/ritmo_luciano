# pylint: disable=no-member
"""
Módulo responsável pela implementação concreta do repositório de PessoaFisica.

Este módulo implementa o repositório concreto DjangoPessoaFisicaRepository,
utilizando o Django ORM para realizar as operações de persistência
e recuperação de dados relacionados à entidade PessoaFisica no banco de dados.
Agora também inclui a relação de endereços associados à PessoaFisica.
"""
from typing import List, Optional
from domain.marketing.repositories.pessoa_fisica import PessoaFisicaRepository
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from infrastructure.repositories.endereco import EnderecoRepository
from infrastructure.repositories.usuario_tipo import UsuarioTipoRepository


class PessoaFisicaRepositoryConcrete(PessoaFisicaRepository):
    """
    Repositório concreto para a entidade PessoaFisica.

    Implementa os métodos definidos no repositório abstrato, utilizando o 
    Django ORM.
    Faz a conversão entre o PessoaFisicaDomain e PessoaFisicaModel, delegando
    operações relacionadas a Endereco e UsuarioTipo para os repositórios 
    específicos.
    """

    def __init__(self, endereco_repo: EnderecoRepository, usuario_tipo_repo: UsuarioTipoRepository):
        """
        Inicializa o repositório concreto de Pessoa Física com as dependências
        necessárias.

        Parâmetros:
            endereco_repo (EnderecoRepository): Repositório para 
            manipulação dos endereços.
            usuario_tipo_repo (UsuarioTipoRepository): 
            Repositório para manipulação dos tipos de usuário.
        """
        self.endereco_repo = endereco_repo
        self.usuario_tipo_repo = usuario_tipo_repo

    def get_by_id(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        """
        Busca uma Pessoa Física pelo ID no banco de dados.

        Parâmetros:
            pessoa_fisica_id (int): ID da pessoa física a ser buscada.

        Retorna:
            PessoaFisicaDomain: A entidade do domínio correspondente à Pessoa
            Física.
            None: Se a pessoa física não for encontrada.
        """
        try:
            model = PessoaFisicaModel.objects.get(id=pessoa_fisica_id)
            enderecos = self.endereco_repo.get_by_pessoa_fisica_id(pessoa_fisica_id)
            usuario_tipos = self.usuario_tipo_repo.get_by_pessoa_fisica_id(pessoa_fisica_id)
            return self._model_to_domain(model, enderecos, usuario_tipos)
        except PessoaFisicaModel.DoesNotExist:
            return None

    def list_all(self) -> List[PessoaFisicaDomain]:
        """
        Lista todas as Pessoas Físicas no banco de dados e as converte para o
        domínio.

        Retorna:
            List[PessoaFisicaDomain]: Lista de entidades do domínio de
            Pessoa Física.
        """
        pessoas_fisicas = PessoaFisicaModel.objects.all()
        return [
            self._model_to_domain(
                pessoa, 
                self.endereco_repo.get_by_pessoa_fisica_id(pessoa.id), 
                self.usuario_tipo_repo.get_by_pessoa_fisica_id(pessoa.id)
            )
            for pessoa in pessoas_fisicas
        ]

    def save(self, pessoa_fisica: PessoaFisicaDomain) -> PessoaFisicaDomain:
        """
        Salva ou atualiza uma Pessoa Física no banco de dados.

        O método delega as operações relacionadas a Endereco e UsuarioTipo
        para os respectivos repositórios.

        Parâmetros:
            pessoa_fisica (PessoaFisicaDomain): A entidade de domínio a ser salva.

        Retorna:
            PessoaFisicaDomain: A entidade de domínio salva ou atualizada.
        """
        model = self._domain_to_model(pessoa_fisica)
        model.save()
        
        # Salvar endereços e tipos de usuário relacionados
        self.endereco_repo.save(pessoa_fisica.enderecos)
        self.usuario_tipo_repo.save(pessoa_fisica.usuario_tipos)
        
        return self._model_to_domain(model, pessoa_fisica.enderecos, pessoa_fisica.usuario_tipos)

    def delete(self, pessoa_fisica_id: int) -> None:
        """
        Remove uma Pessoa Física do banco de dados.

        Parâmetros:
            pessoa_fisica_id (int): O ID da Pessoa Física a ser removida.
        """
        PessoaFisicaModel.objects.filter(id=pessoa_fisica_id).delete()

    def _model_to_domain(self, model: PessoaFisicaModel, enderecos: List, usuario_tipos: List) -> PessoaFisicaDomain:
        """
        Converte o model de infraestrutura para a entidade de domínio.

        Parâmetros:
            model (PessoaFisicaModel): O model de infraestrutura.
            enderecos: A lista de endereços associados.
            usuario_tipos: A lista de tipos de usuário associados.

        Retorna:
            PessoaFisicaDomain: A entidade de domínio convertida.
        """
        return PessoaFisicaDomain(
            pessoa_fisica_id=model.id,
            primeiro_nome=model.first_name,
            sobrenome=model.last_name,
            email=model.email,
            data_nascimento=model.data_nascimento,
            cpf=model.cpf,
            genero=model.genero,
            profissao=model.profissao,
            ocupacao=model.ocupacao,
            whatsapp=model.whatsapp,
            redes_sociais=model.redes_sociais,
            conta_pessoa=model.conta_pessoa,
            iniciador_conta_empresa=model.iniciador_conta_empresa,
            foto=model.foto,
            bios=model.bios,
            enderecos=enderecos,
            usuario_tipos=usuario_tipos
        )

    def _domain_to_model(self, domain: PessoaFisicaDomain) -> PessoaFisicaModel:
        """
        Converte a entidade de domínio para o model de infraestrutura.

        Parâmetros:
            domain (PessoaFisicaDomain): A entidade de domínio a ser convertida.

        Retorna:
            PessoaFisicaModel: O model de infraestrutura convertido.
        """
        return PessoaFisicaModel(
            id=domain.pessoa_fisica_id,
            first_name=domain.primeiro_nome,
            last_name=domain.sobrenome,
            email=domain.email,
            data_nascimento=domain.data_nascimento,
            cpf=domain.cpf,
            genero=domain.genero,
            profissao=domain.profissao,
            ocupacao=domain.ocupacao,
            whatsapp=domain.whatsapp,
            redes_sociais=domain.redes_sociais,
            conta_pessoa=domain.conta_pessoa,
            iniciador_conta_empresa=domain.iniciador_conta_empresa,
            foto=domain.foto,
            bios=domain.bios
        )
