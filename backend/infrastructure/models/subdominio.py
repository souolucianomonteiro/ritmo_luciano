# pylint: disable=no-member
"""
Módulo responsável pela definição da model Subdominio.

Este módulo define a model Subdominio, que representa um subdomínio
relacionado a um site específico no sistema. A model inclui campos para
armazenar o nome do subdomínio e a relação com o site ao qual pertence,
garantindo que a combinação site-subdomínio seja única.

Classes:
    Subdominio: Model que representa um subdomínio de um site.
"""
from typing import TYPE_CHECKING
from django.db import models
from infrastructure.models.site import CustomSite


if TYPE_CHECKING:
    pass
    

class Subdominio(models.Model):
    """
    Model que representa um subdomínio de um site.

    A model Subdominio inclui campos para armazenar o nome do subdomínio 
    e a relação com o site ao qual pertence. Cada subdomínio é único dentro 
    do contexto de um site específico, garantido pela combinação de site
    e nome.

    Atributos:
        site (ForeignKey): Relaciona o subdomínio a um site específico.
        nome (CharField): O nome do subdomínio.
        created_at (DateTimeField): Data de criação do subdomínio.
    """

    site = models.ForeignKey(CustomSite, on_delete=models.CASCADE,
                             related_name='subdominios')
    nome = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para a model Subdominio.

        Define a combinação única de site e nome, garantindo que cada
        subdomínio seja único dentro de um site.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_subdominio'
        constraints = [
                        models.UniqueConstraint(fields=['site', 'nome'],
                                                name='unique_site_nome')
        ]

    def __str__(self):
        return f"{self.nome}.{self.site.domain}"
