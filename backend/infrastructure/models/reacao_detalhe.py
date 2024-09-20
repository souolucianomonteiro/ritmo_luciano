from django.db import models


class ReacaoDetalhe(models.Model):
    """
    Model que representa o tipo de reação que um usuário pode realizar.

    Atributos:
        nome (CharField): O nome da reação (ex: 'curtida', 'amor', 'raiva').
        descricao (TextField): Uma breve descrição da reação (opcional).
        icone (CharField): O ícone associado à reação, que pode ser o nome de
        uma classe de ícone ou o caminho para o arquivo.
    """
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.TextField(null=True, blank=True)
    icone = models.CharField(max_length=100, null=True, blank=True)  # Nome da classe do ícone ou caminho do arquivo

    class Meta:
        """
        Metadados para a model ReacaoDetalhe.

        Define o nome da tabela no banco de dados e os nomes legíveis no
        Django Admin.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_reacao_detalhe'
        verbose_name = 'Detalhe da Reação'
        verbose_name_plural = 'Detalhes das Reações'

    def __str__(self):
        return str(self.nome)
