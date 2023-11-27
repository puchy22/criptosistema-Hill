from .alfabeto import Alfabeto

"""Clase para representar un mensaje"""


class Mensaje:
    def __init__(self, mensaje: str):
        self.mensaje = self.__normalizar(mensaje)
        self.content = self.__str__()
        self.length = len(self.content)

    def __str__(self):
        return self.mensaje

    """Devuelve el mensaje normalizado a nuestro alfabeto"""

    def __normalizar(self, mensaje: str) -> str:
        alfabeto = Alfabeto()
        mensaje_normalizado = ""

        # Recorrer el mensaje caracter por caracter
        for caracter in mensaje:
            """Si el caracter es válido, lo añadimos al mensaje normalizado"""
            caracter_validado = alfabeto.validacion(caracter)
            if caracter_validado is not None:
                mensaje_normalizado += caracter_validado

        return mensaje_normalizado
