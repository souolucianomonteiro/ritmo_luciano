# pylint: disable=no-member

"""
Módulo responsável pela implementação concreta do repositório de 
PessoaJuridica.

Este módulo implementa o repositório concreto DjangoPessoaJuridicaRepository,
utilizando o Django ORM para realizar as operações de persistência
e recuperação de dados relacionados à entidade PessoaJuridica no banco de 
dados.
Agora também inclui a relação de endereços associados à PessoaJuridica.
"""
from typing import Optional, List
from infrastructure.models.pessoa_juridica import PessoaJuridicaModel
from infrastructure.models.endereco import EnderecoModel
from domain.website.entities.pessoa_juridica import PessoaJuridicaDomain
from domain.website.repositories.pessoa_juridica import (
                                PessoaJuridicaRepository)
from domain.website.entities.endereco import EnderecoDomain


class DjangoPessoaJuridicaRepository(PessoaJuridicaRepository):
    """
    Repositório concreto para a entidade PessoaJuridica.

    Implementa os métodos definidos no repositório abstrato, utilizando
    o Django ORM.
    """

    def save(self, pessoa_juridica: PessoaJuridicaDomain) -> PessoaJuridicaDomain:
        pessoa_juridica_model = PessoaJuridicaModel(
            id=pessoa_juridica.id,
            razao_social=pessoa_juridica.razao_social,
            nome_fantasia=pessoa_juridica.nome_fantasia,
            cnpj=pessoa_juridica.cnpj,
            inscricao_estadual=pessoa_juridica.inscricao_estadual,
            usuario_titular_id=pessoa_juridica.usuario_titular_id
        )
        pessoa_juridica_model.save()

        # Atualizando os endereços associados
        self._salvar_enderecos(pessoa_juridica_model, pessoa_juridica.enderecos)

        pessoa_juridica.id = pessoa_juridica_model.id
        return pessoa_juridica

    def _salvar_enderecos(self, pessoa_juridica_model: PessoaJuridicaModel, enderecos: List[EnderecoDomain]) -> None:
        """
        Função privada para salvar os endereços associados a uma Pessoa Jurídica.
        """
        endereco_models = []
        for endereco in enderecos:
            endereco_model, _ = EnderecoModel.objects.get_or_create(
                rua=endereco.rua,
                numero=endereco.numero,
                complemento=endereco.complemento,
                bairro=endereco.bairro,
                cidade=endereco.cidade,
                estado=endereco.estado,
                cep=endereco.cep,
                pais=endereco.pais,
                tipo=endereco.tipo,
                pessoa_juridica_id=pessoa_juridica_model.id,
                pessoa_fisica_id=endereco.pessoa_fisica_id,
                is_active=endereco.is_active,
                data_inicio=endereco.data_inicio,
                data_fim=endereco.data_fim
            )
            endereco_models.append(endereco_model)

        pessoa_juridica_model.enderecos.set(endereco_models)

    def get_by_id(self, pessoa_juridica_id: int) -> Optional[PessoaJuridicaDomain]:
        try:
            pessoa_juridica_model = PessoaJuridicaModel.objects.get(id=pessoa_juridica_id)

            # Mapeando endereços
            enderecos = [
                EnderecoDomain(
                    endereco_id=endereco.id,
                    rua=endereco.rua,
                    numero=endereco.numero,
                    complemento=endereco.complemento,
                    bairro=endereco.bairro,
                    cidade=endereco.cidade,
                    estado=endereco.estado,
                    cep=endereco.cep,
                    pais=endereco.pais,
                    tipo=endereco.tipo,
                    pessoa_fisica_id=endereco.pessoa_fisica_id,
                    pessoa_juridica_id=endereco.pessoa_juridica_id,
                    is_active=endereco.is_active,
                    data_inicio=endereco.data_inicio,
                    data_fim=endereco.data_fim
                )
                for endereco in pessoa_juridica_model.enderecos.all()
            ]

            return PessoaJuridicaDomain(
                id=pessoa_juridica_model.id,
                razao_social=pessoa_juridica_model.razao_social,
                nome_fantasia=pessoa_juridica_model.nome_fantasia,
                cnpj=pessoa_juridica_model.cnpj,
                inscricao_estadual=pessoa_juridica_model.inscricao_estadual,
                usuario_titular_id=pessoa_juridica_model.usuario_titular_id,
                enderecos=enderecos
            )
        except PessoaJuridicaModel.DoesNotExist:
            return None  

    def delete(self, pessoa_juridica: PessoaJuridicaDomain) -> None:
        PessoaJuridicaModel.objects.filter(id=pessoa_juridica.id).delete()

    def list_all(self) -> List[PessoaJuridicaDomain]:
        pessoas_juridicas = PessoaJuridicaModel.objects.all()
        return [
            PessoaJuridicaDomain(
                id=pessoa_juridica.id,
                razao_social=pessoa_juridica.razao_social,
                nome_fantasia=pessoa_juridica.nome_fantasia,
                cnpj=pessoa_juridica.cnpj,
                inscricao_estadual=pessoa_juridica.inscricao_estadual,
                usuario_titular_id=pessoa_juridica.usuario_titular_id,
                enderecos=[
                    EnderecoDomain(
                        endereco_id=endereco.id,
                        rua=endereco.rua,
                        numero=endereco.numero,
                        complemento=endereco.complemento,
                        bairro=endereco.bairro,
                        cidade=endereco.cidade,
                        estado=endereco.estado,
                        cep=endereco.cep,
                        pais=endereco.pais,
                        tipo=endereco.tipo,
                        pessoa_fisica_id=endereco.pessoa_fisica_id,
                        pessoa_juridica_id=endereco.pessoa_juridica_id,
                        is_active=endereco.is_active,
                        data_inicio=endereco.data_inicio,
                        data_fim=endereco.data_fim
                    )
                    for endereco in pessoa_juridica.enderecos.all()
                ]
            )
            for pessoa_juridica in pessoas_juridicas
        ]
