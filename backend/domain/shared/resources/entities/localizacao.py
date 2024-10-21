"""Módulo implementa a classe localização"""

from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass
class LocalizacaoDomain:
    """Classe que implementa o entidade localização"""
    ip_address: str
    latitude: float
    longitude: float
    precisao: Optional[float] = None
    cidade: Optional[str] = None
    estado: Optional[str] = None
    pais: Optional[str] = None
    data_hora_captura: datetime = datetime.now()

    def __str__(self):
        return f"IP: {self.ip_address} - Coordenadas: ({self.latitude}, {self.longitude})"
