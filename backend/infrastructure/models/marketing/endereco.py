from django.db import models


class EnderecoModel(models.Model):
    """
    Model que representa um endereço associado a uma pessoa física ou jurídica.

    Atributos:
        rua (str): Nome da rua.
        numero (str): Número da casa ou edifício.
        complemento (Optional[str]): Complemento, como apartamento ou sala.
        bairro (str): Nome do bairro.
        cidade (str): Nome da cidade.
        estado (str): Nome do estado.
        cep (str): Código postal (CEP).
        pais (str): Nome do país.
        tipo (Literal): Tipo de endereço, como residencial ou comercial.
        pessoa_fisica (ForeignKey): Referência à pessoa física associada a este endereço.
        pessoa_juridica (ForeignKey): Referência à pessoa jurídica associada a este endereço.
        is_active (bool): Indica se este é o endereço atual.
        data_inicio (DateTime): Data de início de validade do endereço.
        data_fim (Optional[DateTime]): Data de término de validade do endereço (para histórico).
    """

    rua = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, null=True, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    cep = models.CharField(max_length=20)
    pais = models.CharField(max_length=100, default='Brasil')
    tipo = models.CharField(max_length=50, choices=[
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        ('correspondencia', 'Correspondência')
    ])
    pessoa_fisica = models.ForeignKey('PessoaFisicaModel', on_delete=models.CASCADE, null=True, blank=True, related_name='enderecos_fisica')
    pessoa_juridica = models.ForeignKey('PessoaJuridicaModel', on_delete=models.CASCADE, null=True, blank=True, related_name='enderecos_juridica')
    is_active = models.BooleanField(default=True)
    data_inicio = models.DateTimeField(auto_now_add=True)
    data_fim = models.DateTimeField(null=True, blank=True)

    class Meta:
        """
        Metadados para a model EnderecoModel.
        """
        app_label = 'infrastructure'
        db_table = 'infrastructure_endereco'
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    def __str__(self):
        return f"{self.rua}, {self.numero} - {self.cidade}, {self.estado}, {self.pais}"
