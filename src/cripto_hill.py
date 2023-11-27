from .alfabeto import Alfabeto
from .mensaje import Mensaje

"""Clase que representa el criptosistema de Hill"""


class Hill:
    def __init__(self, m: int):
        if m > 0:
            self.m = m
            self.t = list[list[int]]
            self.__alfabeto = Alfabeto()
        else:
            raise ValueError("m debe ser mayor que 0")

    """Cifra o descifra el mensaje usando el criptosistema de Hill y la clave <m, T>
    :param mensaje: Mensaje a cifrar o descifrar
    :param cifrar: True si se quiere cifrar, False si se quiere descifrar
    """

    def hill(self, mensaje: Mensaje, cifrar: bool) -> str:
        return ""

    def __traducir(self, mensaje: str, matriz: list[list[int]]) -> str:
        return ""
