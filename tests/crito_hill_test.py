import unittest
import sys
import os

# Añadir al path la ruta del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cripto_hill import Hill


class TestMensaje(unittest.TestCase):
    def test_clave(self):
        """Comprobar que la clave generada es correcta, es decir,
        que m es mayor que 0 y t es una matriz m x m invertible
        """
        m = 2
        hill = Hill(m)
        clave = hill.get_clave()
        self.assertEqual(clave[0], 2)
        self.assertEqual(clave[1].determinant(), 1)


if __name__ == "__main__":
    unittest.main()
