import unittest
import sys
import os

# Añadir al path la ruta del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.alfabeto import Alfabeto
from src.mensaje import Mensaje
from src.cripto_hill import Hill


class TestMensaje(unittest.TestCase):
    def test_clave(self):
        """Comprobar que la clave generada es correcta, es decir,
        que m es mayor que 0 y t es una matriz m x m invertible (determinante != 0)
        """
        alfabeto = Alfabeto()
        m = 2
        hill = Hill(m, alfabeto)
        clave = hill.get_clave()
        self.assertEqual(clave[0], 2)
        self.assertNotEqual(clave[1], 0)
        self.assertIs(clave[1].is_invertible(), True)

        men = Mensaje("hola me llamo juan")

        hill.hill(men, True)


if __name__ == "__main__":
    unittest.main()
