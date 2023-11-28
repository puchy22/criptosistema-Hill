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

    def __len__(self):
        return len(self.alfabeto)

    """Devuelve el valor númerico de una letra del alfabeto"""

    def valor_letra(self, letra: str) -> int | None:
        letra = letra.upper()
        if len(letra) == 1:
            if letra in self.traduccion_alfabeto_especial:
                return self.alfabeto.index(self.traduccion_alfabeto_especial[letra])
            else:
                return self.alfabeto.index(letra)
        else:
            return None

    """Evalua si la letra es válida, es decir, si está en el alfabeto, hay que traducirla o no es válida"""

    def validacion(self, letra: str) -> str | None:
        letra = letra.upper()
        if len(letra) == 1:
            if letra in self.traduccion_alfabeto_especial:
                return self.traduccion_alfabeto_especial[letra]
            elif letra in self.alfabeto:
                return letra
            else:
                return None
        else:
            return None
