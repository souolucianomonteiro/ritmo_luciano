"""
Módulo responsável pela modelagem de dados de geolocalização.

Este módulo define a model Localizacao, que armazena informações sobre 
geolocalização e visitas de usuários. Ele permite capturar dados sobre 
a localização geográfica (latitude, longitude, cidade, estado e país) 
e associá-los a interações com posts, blogs, comentários, reações e 
pessoas físicas.

**Objetivos**:
- Capturar informações de localização quando ações importantes ocorrem, 
  como visualizações de posts, comentários ou reações em blogs.
- Armazenar dados de IP e localização para análise posterior.
- Relacionar geolocalização com entidades como Pessoa Física, Post, Blog, 
  Comentário e Reação.

**Relacionamentos**:
- **Pessoa_Fisica**: Captura a geolocalização associada a uma ação realizada 
  por uma pessoa física.
- **Post**: Relaciona a localização com a interação ou visualização de um post.
- **Blog**: Associa a geolocalização com uma visita ao blog.
- **ComentarioPost**: Captura a localização de onde um comentário foi feito.
- **ReacaoPost**: Captura a localização de onde uma reação foi registrada.

Classes:
    - Localizacao: Model que representa os dados de geolocalização 
      capturados durante interações de usuários.
"""


from django.db import models


class Localizacao(models.Model):
    """
    Model para armazenar informações de geolocalização e visitas.
    """
    ip_address = models.GenericIPAddressField()
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    precisao = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    cidade = models.CharField(max_length=100, null=True, blank=True)
    estado = models.CharField(max_length=100, null=True, blank=True)
    pais = models.CharField(max_length=100, null=True, blank=True)
    data_hora_captura = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        Metadados para o modelo Localizacao.
        """
        db_table = 'localizacao'
        verbose_name = 'Localização'
        verbose_name_plural = 'Localizações'

    def __str__(self):
        return f"IP: {self.ip_address} - Coordenadas: ({self.latitude}, {self.longitude})"
