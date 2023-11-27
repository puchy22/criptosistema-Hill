"""Clase que contiene el alfabeto a usar"""


class Alfabeto:
    def __init__(self):
        self.alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.traduccion_alfabeto_especial = {
            "Á": "A",
            "Ä": "A",
            "É": "E",
            "Ë": "E",
            "Í": "I",
            "Ï": "I",
            "Ó": "O",
            "Ö": "O",
            "Ú": "U",
            "Ü": "U",
            "Ñ": "N",
        }

    # Datos sobre el alfabeto

    def get_longitud(self):
        return len(self.alfabeto)

    # Métodos para traducir a valor númerico las letras

    def valor_letra(self, letra: str) -> int | None:
        letra = letra.upper()
        if len(letra) == 1:
            if letra in self.traduccion_alfabeto_especial:
                return self.alfabeto.index(self.traduccion_alfabeto_especial[letra])
            else:
                return self.alfabeto.index(letra)
        else:
            return None
