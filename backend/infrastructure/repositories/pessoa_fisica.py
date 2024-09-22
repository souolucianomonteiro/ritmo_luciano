# pylint: disable=no-member
"""
Módulo responsável pela implementação concreta do repositório de PessoaFisica.

Este módulo implementa o repositório concreto DjangoPessoaFisicaRepository,
utilizando o Django ORM para realizar as operações de persistência
e recuperação de dados relacionados à entidade PessoaFisica no banco de dados.
Agora também inclui a relação de endereços associados à PessoaFisica.
"""
from typing import Optional, List
from domain.website.entities.pessoa_fisica import PessoaFisicaDomain
from domain.website.repositories.pessoa_fisica import PessoaFisicaRepository
from infrastructure.models.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.usuario_tipo import UsuarioTipo
from infrastructure.models.endereco import EnderecoModel


class DjangoPessoaFisicaRepository(PessoaFisicaRepository):
    """
    Repositório concreto para a entidade PessoaFisica.

    Implementa os métodos definidos no repositório abstrato, utilizando
    o Django ORM.
    """

    def save(self, pessoa_fisica: PessoaFisicaDomain) -> PessoaFisicaDomain:
        pessoa_fisica_model = PessoaFisicaModel(
            id=pessoa_fisica.id,
            username=pessoa_fisica.email,  # Email como login
            first_name=pessoa_fisica.primeiro_nome,
            last_name=pessoa_fisica.sobrenome,
            data_nascimento=pessoa_fisica.data_nascimento,
            email=pessoa_fisica.email,
            profissao_id=pessoa_fisica.profissao.id if pessoa_fisica.profissao else None,
            ocupacao=pessoa_fisica.ocupacao,
            whatsapp=pessoa_fisica.whatsapp,
            redes_sociais=pessoa_fisica.redes_sociais,
            cpf=pessoa_fisica.cpf,
            genero=pessoa_fisica.genero,
            conta_pessoa=pessoa_fisica.conta_pessoa,
            iniciador_conta_empresa=pessoa_fisica.iniciador_conta_empresa,
            foto=pessoa_fisica.foto,  
            bios=pessoa_fisica.bios, 
        )
        pessoa_fisica_model.save()
        pessoa_fisica.id = pessoa_fisica_model.id

        # Salvando os endereços
        if pessoa_fisica.enderecos:
            enderecos_models = [
                EnderecoModel.objects.get_or_create(
                    rua=endereco.rua,
                    numero=endereco.numero,
                    complemento=endereco.complemento,
                    bairro=endereco.bairro,
                    cidade=endereco.cidade,
                    estado=endereco.estado,
                    cep=endereco.cep,
                    pais=endereco.pais,
                    pessoa_fisica_id=pessoa_fisica_model.id,  # Correção aplicada: agora é um argumento de palavra-chave
                    is_active=endereco.is_active
                )[0]
                for endereco in pessoa_fisica.enderecos
            ]
            pessoa_fisica_model.enderecos.set(enderecos_models)

        # Verifica se o usuário já tem um tipo associado. Se não, define como "Titular"
        if not UsuarioTipo.objects.filter(pessoas_fisicas=pessoa_fisica_model).exists():
            tipo_titular, created = UsuarioTipo.objects.get_or_create(nome='Titular', defaults={'descricao': 'Usuário Titular'})
            pessoa_fisica_model.usuario_tipos.add(tipo_titular)

        pessoa_fisica_model.save()

        # Salvando os tipos de usuário associados
        tipos_usuario = [
            UsuarioTipo(
                id=tipo_usuario.id if hasattr(tipo_usuario, 'id') else None,  # Verifica se há ID
                nome=tipo_usuario.nome,
                descricao=tipo_usuario.descricao
            )
            for tipo_usuario in UsuarioTipo.objects.filter(pessoas_fisicas=pessoa_fisica_model)
        ]

        return PessoaFisicaDomain(
            id=pessoa_fisica_model.id,
            primeiro_nome=pessoa_fisica_model.first_name,
            sobrenome=pessoa_fisica_model.last_name,
            email=pessoa_fisica_model.email,
            data_nascimento=pessoa_fisica_model.data_nascimento,
            idade_anos=None,  # Será calculado
            idade_meses=None,  # Será calculado
            cpf=pessoa_fisica_model.cpf,
            genero=pessoa_fisica_model.genero,
            profissao=None if pessoa_fisica_model.profissao is None else pessoa_fisica_model.profissao,
            ocupacao=pessoa_fisica_model.ocupacao,
            whatsapp=pessoa_fisica_model.whatsapp,
            redes_sociais=pessoa_fisica_model.redes_sociais,
            conta_pessoa=pessoa_fisica_model.conta_pessoa,
            iniciador_conta_empresa=pessoa_fisica_model.iniciador_conta_empresa,
            enderecos=pessoa_fisica.enderecos,  # Inclui os endereços
            usuario_tipos=tipos_usuario,  # Inclui os tipos de usuário
            foto=pessoa_fisica_model.foto,  # Novo campo
            bios=pessoa_fisica_model.bios,
        )

    def get_by_id(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        try:
            pessoa_fisica_model = PessoaFisicaModel.objects.get(id=pessoa_fisica_id)
            tipos_usuario = [
                UsuarioTipo(
                    id=tipo_usuario.id if hasattr(tipo_usuario, 'id') else None,
                    nome=tipo_usuario.nome,
                    descricao=tipo_usuario.descricao
                )
                for tipo_usuario in UsuarioTipo.objects.filter(pessoas_fisicas=pessoa_fisica_model)
            ]

            enderecos = [
                EnderecoModel(
                    rua=endereco.rua,
                    numero=endereco.numero,
                    complemento=endereco.complemento,
                    bairro=endereco.bairro,
                    cidade=endereco.cidade,
                    estado=endereco.estado,
                    cep=endereco.cep,
                    pais=endereco.pais
                )
                for endereco in pessoa_fisica_model.enderecos.all()
            ]

            return PessoaFisicaDomain(
                id=pessoa_fisica_model.id,
                primeiro_nome=pessoa_fisica_model.first_name,
                sobrenome=pessoa_fisica_model.last_name,
                email=pessoa_fisica_model.email,
                data_nascimento=pessoa_fisica_model.data_nascimento,
                idade_anos=None,  # Será calculado
                idade_meses=None,  # Será calculado
                cpf=pessoa_fisica_model.cpf,
                genero=pessoa_fisica_model.genero,
                profissao=None if pessoa_fisica_model.profissao is None else pessoa_fisica_model.profissao,
                ocupacao=pessoa_fisica_model.ocupacao,
                whatsapp=pessoa_fisica_model.whatsapp,
                redes_sociais=pessoa_fisica_model.redes_sociais,
                conta_pessoa=pessoa_fisica_model.conta_pessoa,
                iniciador_conta_empresa=pessoa_fisica_model.iniciador_conta_empresa,
                enderecos=enderecos,
                usuario_tipos=tipos_usuario,
                foto=pessoa_fisica_model.foto,  # Novo campo
                bios=pessoa_fisica_model.bios,
            )
        except PessoaFisicaModel.DoesNotExist:
            return None

    def delete(self, pessoa_fisica: PessoaFisicaDomain) -> None:
        PessoaFisicaModel.objects.filter(id=pessoa_fisica.id).delete()

    def list_all(self) -> List[PessoaFisicaDomain]:
        pessoas_fisicas = PessoaFisicaModel.objects.all()
        return [
            PessoaFisicaDomain(
                id=pessoa.id,
                primeiro_nome=pessoa.first_name,
                sobrenome=pessoa.last_name,
                email=pessoa.email,
                data_nascimento=pessoa.data_nascimento,
                idade_anos=None,  # Será calculado
                idade_meses=None,  # Será calculado
                cpf=pessoa.cpf,
                genero=pessoa.genero,
                profissao=None if pessoa.profissao is None else pessoa.profissao,
                ocupacao=pessoa.ocupacao,
                whatsapp=pessoa.whatsapp,
                redes_sociais=pessoa.redes_sociais,
                conta_pessoa=pessoa.conta_pessoa,
                iniciador_conta_empresa=pessoa.iniciador_conta_empresa,
                enderecos=[
                    EnderecoModel(
                        rua=endereco.rua,
                        numero=endereco.numero,
                        complemento=endereco.complemento,
                        bairro=endereco.bairro,
                        cidade=endereco.cidade,
                        estado=endereco.estado,
                        cep=endereco.cep,
                        pais=endereco.pais
                    )
                    for endereco in pessoa.enderecos.all()
                ],
                usuario_tipos=[
                    UsuarioTipo(
                        id=tipo_usuario.id if hasattr(tipo_usuario, 'id') else None,
                        nome=tipo_usuario.nome,
                        descricao=tipo_usuario.descricao
                    )
                    for tipo_usuario in UsuarioTipo.objects.filter(pessoas_fisicas=pessoa)
                ],
                foto=pessoa.foto,  # Novo campo
                bios=pessoa.bios,
            )
            for pessoa in pessoas_fisicas
        ]
