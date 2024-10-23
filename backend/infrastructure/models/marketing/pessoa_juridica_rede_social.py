# pylint: disable=no-member

"""
Módulo responsável pela definição da model associativa PessoaJuridicaRedeSocialModel.

Este módulo define a tabela intermediária que estabelece o relacionamento 
entre PessoaJuridica e RedeSocial, permitindo que uma pessoa jurídica tenha 
várias redes sociais associadas e armazene o nome de usuário ou URL em cada 
uma delas.

Classes:
    PessoaJuridicaRedeSocialModel: Classe que define a tabela associativa entre
    PessoaJuridica e RedeSocial, armazenando o nome de usuário/URL na rede social.
"""
from django.db import models
from infrastructure.models.marketing.pessoa_juridica import PessoaJuridicaModel
from infrastructure.models.shared.resources.rede_social import RedeSocialModel


class PessoaJuridicaRedeSocialModel(models.Model):
    """
    Model associativa entre PessoaJuridica e RedeSocial.

    Representa a relação de uma pessoa jurídica com as redes sociais
    e o respectivo nome de usuário.
    """
    pessoa_juridica = models.ForeignKey(PessoaJuridicaModel, on_delete=models.CASCADE)
    rede_social = models.ForeignKey(RedeSocialModel, on_delete=models.CASCADE)
    usuario = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        """
        Metadados da model PessoaJuridicaRedeSocialModel.

        Define restrições e comportamentos específicos da model, como a 
        unicidade do relacionamento entre PessoaJuridica e RedeSocial, 
        garantindo que uma pessoa jurídica só possa ter uma associação única 
        com cada rede social.

        Atributos:
        unique_together (tuple): Define que a combinação de pessoa_juridica e 
        rede_social deve ser única, evitando duplicidade de entradas.
        """
        unique_together = ('pessoa_juridica', 'rede_social')

    def __str__(self):
        return f'{self.pessoa_juridica.razao_social} - {self.rede_social.nome} ({self.usuario})'
