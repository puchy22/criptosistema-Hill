import unittest
import sys
import os

# Añadir al path la ruta del proyecto
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.mensaje import Mensaje


class TestMensaje(unittest.TestCase):
    def test_mensaje_normalizado_1(self):
        # Crear un mensaje con espacios y minúsculas
        mensaje = Mensaje("Este es un mensaje de prueba")

        resultado_esperado = "ESTEESUNMENSAJEDEPRUEBA"
        resultado_real = str(mensaje)

        # Comprobar si el resultado obtenido es igual al esperado
        self.assertEqual(resultado_real, resultado_esperado)

    def test_mensaje_normalizado_2(self):
        # Crear un mensaje con espacios y minúsculas
        mensaje = Mensaje("Hola, prueba   de mensaje normalizado")

        # Obtener el mensaje en mayúsculas y sin espacios
        resultado_esperado = "HOLAPRUEBADEMENSAJENORMALIZADO"
        resultado_real = str(mensaje)

        # Comprobar si el resultado obtenido es igual al esperado
        self.assertEqual(resultado_real, resultado_esperado)

    def test_mensaje_normalizado_3(self):
        # Crear un mensaje con espacios y minúsculas
        mensaje = Mensaje(
            """Hola. Última prueba de mensaje normalizado.
                            Este mensaje tiene saltos de línea,
                            Envidado desde España por Rubén."""
        )

        # Obtener el mensaje en mayúsculas y sin espacios
        resultado_esperado = "HOLAULTIMAPRUEBADEMENSAJENORMALIZADOESTEMENSAJETIENESALTOSDELINEAENVIDADODESDEESPANAPORRUBEN"
        resultado_real = str(mensaje)

        # Comprobar si el resultado obtenido es igual al esperado
        self.assertEqual(resultado_real, resultado_esperado)


if __name__ == "__main__":
    unittest.main()
