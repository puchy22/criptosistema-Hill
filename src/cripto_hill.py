from .alfabeto import Alfabeto
from .mensaje import Mensaje
from sage.matrix.constructor import matrix, random_matrix
from sage.rings.integer_ring import ZZ

"""Clase que representa el criptosistema de Hill"""


class Hill:
    def __init__(self, m: int):
        if m > 0:
            self.clave = (m, random_matrix(ZZ, m, algorithm="unimodular"))
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

    """Obtener la clave del criptosistema de Hill"""

    def get_clave(self) -> tuple[int, matrix]:
        return self.clave

    """Regenerar la clave del criptosistema de Hill"""

    def regenerar_clave(self, m: int):
        if m > 0:
            self.clave = (m, random_matrix(ZZ, m, algorithm="unimodular"))
        else:
            raise ValueError("m debe ser mayor que 0")
