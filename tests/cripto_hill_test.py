import unittest
import sys
import os

# Añadir al path la ruta del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alfabeto import Alfabeto
from src.mensaje import Mensaje
from src.cripto_hill import Hill
from math import gcd


class TestHill(unittest.TestCase):
    def test_clave(self):
        """Comprobar que la clave generada es correcta, es decir,
        que m es mayor que 0 y t es una matriz m x m invertible y regular en Z/len(alfabeto)Z
        """
        alfabeto = Alfabeto()
        m = 8
        hill = Hill(m, alfabeto)
        clave = hill.get_clave()
        self.assertEqual(clave[0], m)
        self.assertNotEqual(clave[1], 0)
        self.assertIs(clave[1].is_invertible(), True)
        self.assertEqual(gcd(clave[1].det(), len(alfabeto)), 1)
        # print(f"Matriz identidad:\n{clave[1]*clave[1].inverse()}")

    def test_cifrado_descifrado(self):
        """Comprobar que al cifrar y descifrar el mismo mensaje da el mismo resultado."""

        alfabeto = Alfabeto()
        m = 2
        hill = Hill(m, alfabeto)
        mensaje = Mensaje(
            "Hola, esto es una prueba de  que el cifrado funciona correctamente. No multi de tres"
        )
        cifrado = hill.hill(mensaje, True)

        # Comprobar que el cifrado es distinto al mensaje original
        self.assertNotEqual(cifrado, mensaje)

        descifrado = hill.hill(Mensaje(cifrado), False)

        print(f"Mensaje original: {mensaje}")
        print(f"Mensaje cifrado: {cifrado}")
        print(f"Mensaje descifrado: {descifrado}")


if __name__ == "__main__":
    unittest.main()
