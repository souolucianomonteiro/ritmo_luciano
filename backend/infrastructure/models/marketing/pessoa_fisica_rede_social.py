# pylint: disable=E1101
"""
Módulo responsável pela definição da model PessoaFisicaRedeSocialModel.

Este módulo define a model associativa entre PessoaFisicaModel e RedeSocialModel,
permitindo armazenar as redes sociais selecionadas por uma pessoa física e o 
respectivo nome de usuário em cada rede social.

Classes:
    PessoaFisicaRedeSocialModel: Tabela associativa entre PessoaFisicaModel e RedeSocialModel.
"""
from django.db import models
from infrastructure.models.marketing.pessoa_fisica import PessoaFisicaModel
from infrastructure.models.shared.resources.rede_social import RedeSocialModel


class PessoaFisicaRedeSocialModel(models.Model):
    """
    Model associativa que relaciona PessoaFisicaModel com RedeSocialModel.
    Essa tabela armazena o endereço (nome de usuário) que a pessoa física
    utiliza em cada rede social.

    Atributos:
        pessoa_fisica (ForeignKey): Relaciona a pessoa física à rede social.
        rede_social (ForeignKey): Referência à rede social predefinida.
        endereco (CharField): Nome de usuário ou endereço da pessoa física nessa rede social.
    """
    pessoa_fisica = models.ForeignKey(
        PessoaFisicaModel, on_delete=models.CASCADE, related_name='redes_sociais'
    )
    rede_social = models.ForeignKey(
        RedeSocialModel, on_delete=models.CASCADE, related_name='pessoas'
    )
    endereco = models.CharField(max_length=255)  # Nome de usuário na rede social

    class Meta:
        """
        Metadados da model PessoaFisicaRedeSocialModel.

        Define o nome da tabela no banco de dados, a aplicação de uma restrição
        de unicidade (unique_together) para garantir que cada pessoa física tenha
        apenas um endereço por rede social.
    
        Atributos:
        db_table (str): Nome da tabela no banco de dados.
        unique_together (tuple): Garante que a combinação de pessoa_fisica e 
        rede_social seja única.
        """
        db_table = 'pessoa_fisica_rede_social'  # Nome da tabela no banco
        unique_together = ('pessoa_fisica', 'rede_social')  # Garante que cada pessoa física tenha apenas um endereço por rede social

    def __str__(self):
        # Acessa o campo first_name da instância relacionada de PessoaFisicaModel
        return f'{self.pessoa_fisica.first_name} - {self.rede_social.nome}: {self.endereco}'
