from .alfabeto import Alfabeto
from .cripto_hill import Hill
from .mensaje import Mensaje

from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.matrix.constructor import matrix
from sage.symbolic.ring import SR, var
from sage.symbolic.relation import solve_mod
from sage.arith.misc import GCD


from pprint import pprint


class ataqueHill:
    def __init__(
        self, m: int, texto_plano: Mensaje, texto_cifrado: Mensaje, alfabeto: Alfabeto
    ):
        if m > 0:
            # Generar un anillo de enteros del tamaño del alfabeto
            self._Z = IntegerModRing(len(alfabeto))
            self._m = m
            self._texto_plano = str(texto_plano)
            self._texto_cifrado = str(texto_cifrado)
            self._alfabeto = alfabeto
        else:
            raise ValueError("m debe ser mayor que 0")

    def ataque_hill(self):
        # Crear una lista de variables independientes

        var_list = [var("x" + str(i)) for i in range(self._m * self._m)]

        # Crear una matriz con las variables independientes
        T = matrix(SR, self._m, self._m, var_list)

        # Crear una matriz de m filas para almacenar las ecuaciones
        ecuaciones = [[] for _ in range(self._m)]

        # Recorrer el texto plano y el texto cifrado de m en m
        for i in range(0, len(self._texto_plano), self._m):
            # Si al texto plano le quedan bloques de m, seguir construyendo ecuaciones
            if len(self._texto_plano[i:]) >= self._m:
                # Crear una matriz columna con los valores de las letras del texto plano
                M = matrix(
                    SR,
                    self._m,
                    1,
                    [
                        self._alfabeto.valor_letra(letra)
                        for letra in self._texto_plano[i : i + self._m]
                    ],
                )

                # Crear una matriz columna con los valores de las letras del texto cifrado
                C = matrix(
                    SR,
                    self._m,
                    1,
                    [
                        self._alfabeto.valor_letra(letra)
                        for letra in self._texto_cifrado[i : i + self._m]
                    ],
                )

                # Obtener una ecuación con T * M = C, devuelve m ecuaciones
                ecuacion = T * M

                # Introducir las m ecuaciones en su respectiva fila de la matriz ecuaciones convertidas a Expresiones Simbólicas
                for fila in range(self._m):
                    ecuaciones[fila].append(ecuacion[fila, 0] == C[fila, 0])

        # Resolver los distintos sistemas de ecuaciones
        soluciones = []

        for sistema in ecuaciones:
            solucion = solve_mod(sistema, len(self._alfabeto))
            # Convertir los valores de forma tupla a enteros
            solucion = [int(valor) for valor in solucion[0]]
            soluciones.append(solucion)

        return soluciones

    def __comprobar_regularidad(self, T: matrix):
        # Comprobar que la matriz T es regular
        if T.is_invertible() and GCD(T.det(), len(self._alfabeto)) == 1:
            return True
        else:
            return False
