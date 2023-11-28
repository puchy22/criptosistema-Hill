from .alfabeto import Alfabeto
from .mensaje import Mensaje
from sage.matrix.constructor import matrix, random_matrix
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing

"""Clase que representa el criptosistema de Hill"""


class Hill:
    def __init__(self, m: int, alfabeto: Alfabeto):
        if m > 0:
            # Generar un anillo de enteros del tamaño del alfabeto
            self._Z = IntegerModRing(len(alfabeto))

            # Generar una matriz aleatoria y no parar hasta que tenga inversa (matriz regular)
            T = random_matrix(self._Z, m, m)

            while not T.is_invertible():
                T = random_matrix(self._Z, m, m)

            self._clave = (m, T)
        else:
            raise ValueError("m debe ser mayor que 0")

    """Cifra o descifra el mensaje usando el criptosistema de Hill y la clave <m, T>
    :param mensaje: Mensaje a cifrar o descifrar
    :param cifrar: True si se quiere cifrar, False si se quiere descifrar
    """

    def hill(self, mensaje: Mensaje, cifrar: bool) -> str:
        mensaje_str = str(mensaje)

        if cifrar:
            return self.__traducir(mensaje_str, self._clave[1])
        else:
            return self.__traducir(mensaje_str, self._clave[1].inverse())

    def __traducir(self, mensaje: str, matriz: matrix) -> str:
        """Lógica que hace el cifrado de Hill mediante la multiplicación de matrices"""
        return ""

    """Obtener la clave del criptosistema de Hill"""

    def get_clave(self) -> tuple[int, matrix]:
        return self._clave

    """Regenerar la clave del criptosistema de Hill"""

    def regenerar_clave(self, m: int):
        if m > 0:
            self._clave = (m, random_matrix(self._Z, m, algorithm="unimodular"))
        else:
            raise ValueError("m debe ser mayor que 0")
