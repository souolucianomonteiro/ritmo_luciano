from django.db import models


class ProfissaoModel(models.Model):
    """
    Model que representa uma profissão no sistema.

    Atributos:
        codigo (str): Código único da profissão.
        descricao (str): Descrição da profissão.
    """
    codigo = models.CharField(max_length=10, unique=True)
    descricao = models.CharField(max_length=255)

    class Meta:
        """
        Metadados para a model Profissão.

        Define o comportamento do modelo no Django, incluindo o nome da tabela 
        no banco de dados, e nomes legíveis para o Django Admin.
        """
        app_label = "infrastructure"
        db_table = 'infrastructure_profissao'
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'

    def __str__(self):
        return str(self.descricao)
