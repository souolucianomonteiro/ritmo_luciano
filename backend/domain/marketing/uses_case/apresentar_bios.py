"""Módulo que implementa o caso de uso exibir bios do titular"""
from domain.marketing.repositories.pessoa_fisica import PessoaFisicaRepository
from domain.marketing.domain_service.calcular_idade_titular import                              (CalcularIdadePessoaFisicaService)
from domain.marketing.entities.pessoa_fisica import PessoaFisicaDomain


class ExibirPerfilPessoaFisicaUseCase:
    """
    Caso de uso para exibir o perfil completo de uma pessoa física, incluindo foto, bios, idade calculada e profissão.
    """

    def __init__(self, pessoa_fisica_repository: PessoaFisicaRepository, calcular_idade_service: CalcularIdadePessoaFisicaService):
        self.pessoa_fisica_repository = pessoa_fisica_repository
        self.calcular_idade_service = calcular_idade_service

    def executar(self, pessoa_fisica_id: int) -> Optional[PessoaFisicaDomain]:
        """
        Executa a exibição do perfil de uma pessoa física, incluindo foto, bios, idade calculada e profissão.

        :param pessoa_fisica_id: ID da pessoa física a ser exibida.
        :return: PessoaFisicaDomain com os dados completos ou None se não for encontrada.
        """
        # Busca a pessoa física pelo ID no repositório
        pessoa_fisica = self.pessoa_fisica_repository.get_by_id(pessoa_fisica_id)

        if pessoa_fisica:
            # Calcula a idade usando o serviço de domínio
            pessoa_fisica = self.calcular_idade_service.calcular_idade(pessoa_fisica)

        return pessoa_fisica
