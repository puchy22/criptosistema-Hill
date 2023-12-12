from .alfabeto import Alfabeto
from .cripto_hill import Hill
from .mensaje import Mensaje

from sage.rings.finite_rings.integer_mod_ring import IntegerModRing
from sage.matrix.constructor import matrix
from sage.symbolic.ring import SR, var
from sage.symbolic.relation import solve_mod
from sage.arith.misc import GCD
from sage.rings.universal_cyclotomic_field import UniversalCyclotomicField

from concurrent.futures import ThreadPoolExecutor

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
        # Límites para no saturar la memoria con un sistema de ecuaciones muy grande

        limite_bloques_mensaje = self._m * 10

        # Crear una lista de variables independientes

        var_list = [
            var("x" + str(i) + str(j)) for i in range(self._m) for j in range(self._m)
        ]

        # Crear una matriz con las variables independientes
        T = matrix(SR, self._m, self._m, var_list)

        # Crear una matriz de m filas para almacenar las ecuaciones
        ecuaciones = [[] for _ in range(self._m)]

        # Recorrer el texto plano y el texto cifrado de m en m
        for i in range(0, limite_bloques_mensaje, self._m):
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
            else:  # Si no, parar de construir ecuaciones
                break

        # Resolver los distintos sistemas de ecuaciones
        soluciones = []

        # Usar hilos para resolver los sistemas de ecuaciones

        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(
                    self.__resolver_sistema_mod, sistema, len(self._alfabeto)
                )
                for sistema in ecuaciones
            ]

            for future in futures:
                solucion = future.result()
                if solucion is not None:
                    soluciones.append(solucion)

        # Comprobar que la matriz de soluciones es regular
        if self.__comprobar_regularidad(matrix(self._Z, soluciones)):
            return soluciones
        else:
            raise ValueError(
                "A partir del mensaje dado no se puede obtener la clave con este ataque"
            )

    def __comprobar_regularidad(self, T: matrix):
        # Comprobar que la matriz T es regular
        if T.is_invertible() and GCD(T.det(), len(self._alfabeto)) == 1:
            return True
        else:
            return False

    def __resolver_sistema_mod(self, sistema: list[int], mod: int):
        try:
            solucion = solve_mod(sistema, mod)
            # Convertir los valores de forma tupla a enteros
            solucion = [int(valor) for valor in solucion[0]]
            return solucion
        except Exception as e:
            print(f"Error al resolver el sistema de ecuaciones: {e}")
            return None
