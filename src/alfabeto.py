"""Clase que contiene el alfabeto a usar"""


class Alfabeto:
    def __init__(self):
        self._alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self._traduccion_alfabeto_especial = {
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

    def __len__(self) -> int:
        return len(self._alfabeto)

    """Devuelve el valor númerico de una letra del alfabeto"""

    def valor_letra(self, letra: str) -> int | None:
        letra = letra.upper()
        if len(letra) == 1:
            if letra in self._traduccion_alfabeto_especial:
                return self._alfabeto.index(self._traduccion_alfabeto_especial[letra])
            else:
                return self._alfabeto.index(letra)
        else:
            return None

    """Devuelve la letra del alfabeto que tiene el valor númerico indicado"""

    def letra_valor(self, valor: int) -> str | None:
        # Comprueba que el valor esté en el rango del alfabeto
        if 0 <= valor < len(self._alfabeto):
            return self._alfabeto[valor]
        else:
            return None

    """Evalua si la letra es válida, es decir, si está en el alfabeto, hay que traducirla o no es válida"""

    def validacion(self, letra: str) -> str | None:
        letra = letra.upper()
        if len(letra) == 1:
            if letra in self._traduccion_alfabeto_especial:
                return self._traduccion_alfabeto_especial[letra]
            elif letra in self._alfabeto:
                return letra
            else:
                return None
        else:
            return None
