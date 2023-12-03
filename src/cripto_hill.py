from .alfabeto import Alfabeto
from .mensaje import Mensaje
from sage.matrix.constructor import matrix, random_matrix
from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.arith.misc import GCD

"""Clase que representa el criptosistema de Hill"""


class Hill:
    def __init__(self, m: int, alfabeto: Alfabeto):
        if m > 0:
            # Generar un anillo de enteros del tamaño del alfabeto
            self._Z = IntegerModRing(len(alfabeto))

            # Generar una matriz aleatoria y no parar hasta que tenga inversa (matriz regular)
            T = random_matrix(self._Z, m, m)

            while not T.is_invertible() or GCD(T.det(), len(alfabeto)) != 1:
                T = random_matrix(self._Z, m, m)

            self._clave = (m, T)
            self._alfabeto = alfabeto
        else:
            raise ValueError("m debe ser mayor que 0")

    """Cifra o descifra el mensaje usando el criptosistema de Hill y la clave <m, T>
    :param mensaje: Mensaje a cifrar o descifrar
    :param cifrar: True si se quiere cifrar, False si se quiere descifrar
    """

    def hill(self, mensaje: Mensaje, cifrar: bool) -> str:
        mensaje_corregido = str(mensaje)

        # Mientras que el mensaje no tenga el tamaño correcto (múltiplo de m) añadir W al final
        while (len(mensaje_corregido) % self._clave[0]) != 0:
            mensaje_corregido += "W"

        # Cifrar o descifrar el mensaje en función de la variable cifrar
        if cifrar:
            return self.__traducir(mensaje_corregido, self._clave[1])
        else:
            return self.__traducir(mensaje_corregido, self._clave[1].inverse())

    """Lógica que hace el cifrado de Hill mediante la multiplicación de matrices"""

    def __traducir(self, mensaje_orig: str, matriz_clave: matrix) -> str:
        mensaje_trad = ""
        for i in range(0, len(mensaje_orig), self._clave[0]):
            # Crear una matriz columna con los valores de las letras del mensaje_orig
            M = matrix(
                self._Z,
                self._clave[0],
                1,
                [
                    self._alfabeto.valor_letra(letra)
                    for letra in mensaje_orig[i : i + self._clave[0]]
                ],
            )
            # print(f"Matriz sin traducir:\n{M}")
            # Multiplicar la matriz columna del mensaje_orig por la matriz de la clave
            M = matriz_clave * M

            # print(f"Matriz traducida:\n{M}")

            # Pasar la matriz columna con los valores traducidos a letras y añadirlos al mensaje_trad

            for vector in M:
                for valor in vector:
                    letra = self._alfabeto.letra_valor(int(valor))
                    if letra is not None:
                        mensaje_trad += letra

        return mensaje_trad

    """Obtener la clave del criptosistema de Hill"""

    def get_clave(self) -> tuple[int, matrix]:
        return self._clave

    """Regenerar la clave del criptosistema de Hill"""

    def regenerar_clave(self, m: int):
        if m > 0:
            self._clave = (m, random_matrix(self._Z, m, algorithm="unimodular"))
        else:
            raise ValueError("m debe ser mayor que 0")

    """Establecer la clave del criptosistema de Hill, cumpliendo las condiciones de la clave"""

    def set_clave(self, m: int, M: list[list[int]]):
        T = matrix(self._Z, M)
        if m > 0 and T.is_invertible() and GCD(T.det(), len(self._alfabeto)) == 1:
            self._clave = (m, T)
        else:
            raise ValueError("m debe ser mayor que 0 y T debe ser regular")
