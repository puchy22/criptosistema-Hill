import unittest
import sys
import os

# Añadir al path la ruta del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alfabeto import Alfabeto
from src.mensaje import Mensaje
from src.cripto_hill import Hill
from src.ataque_hill import ataqueHill
from pprint import pprint


class TestAtaqueHill(unittest.TestCase):
    def test_ataque_hill(self):
        # Crear alfabeto
        alfabeto = Alfabeto()

        # Crear mensaje
        mensaje = Mensaje(
            "Esto es un mensaje altamente secreto. Cuanto más largo sea el mensaje, más fácil será descifrarlo, para m mayores, si no podemos encontrarnos con demasiados errores por falta de matrices."
        )

        m = 5

        # Crear criptosistema de Hill
        hill = Hill(m, alfabeto)

        # Guardar la clave del sistema
        clave = hill.get_clave()

        # Cifrar el mensaje
        mensaje_cifrado = hill.hill(mensaje, True)

        mensaje_cifrado = Mensaje(mensaje_cifrado)

        # Crear ataque
        ataque = ataqueHill(clave[0], mensaje, mensaje_cifrado, alfabeto)

        # Realizar ataque
        T = ataque.ataque_hill()

        # Descifrar el mensaje con la clave del ataque

        hill.set_clave(m, T)

        mensaje_descifrado = hill.hill(mensaje_cifrado, False)

        # Normalizar el mensaje original para que sea múltiplo de m
        mensaje = str(mensaje)
        while len(mensaje) % m != 0:
            mensaje += "W"

        # Comprobar que la matriz T es correcta
        self.assertEqual(mensaje, mensaje_descifrado)


if __name__ == "__main__":
    unittest.main()
