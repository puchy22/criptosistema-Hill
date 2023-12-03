import unittest
import sys
import os

# Añadir al path la ruta del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alfabeto import Alfabeto
from src.mensaje import Mensaje
from src.cripto_hill import Hill
from src.ataque_hill import ataqueHill


class TestAtaqueHill(unittest.TestCase):
    def test_ataque_hill(self):
        # Crear alfabeto
        alfabeto = Alfabeto()

        # Crear mensaje
        mensaje = Mensaje("Esto es un mensaje altamente secreto")

        # Crear criptosistema de Hill
        hill = Hill(2, alfabeto)

        # Guardar la clave del sistema
        clave = hill.get_clave()

        # Cifrar el mensaje
        mensaje_cifrado = hill.hill(mensaje, True)

        mensaje_cifrado = Mensaje(mensaje_cifrado)

        # Crear ataque
        ataque = ataqueHill(clave[0], mensaje, mensaje_cifrado, alfabeto)

        # Realizar ataque
        T = ataque.ataque_hill()

        # Comprobar que la matriz T es correcta
        self.assertEqual(clave[1], T)


if __name__ == "__main__":
    unittest.main()
