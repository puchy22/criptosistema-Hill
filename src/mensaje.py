from .alfabeto import Alfabeto

"""Clase para representar un mensaje"""


class Mensaje:
    def __init__(self, mensaje: str):
        self.mensaje = mensaje

    """Devuelve el mensaje en mayúsculas y sin espacios"""

    def __str__(self):
        return self.mensaje
