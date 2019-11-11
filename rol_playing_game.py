"""Ejemplos de clases requeridas para implementar un juego simple de tipo 
RPG (Rol-Playing Game)."""


from random import choice


class Aventurero:
    """Una instancia de esta clase representa un personaje aventurero."""

    def __init__(self, nombre):
        """Inilializa una instancia de la clase Aventurero."""
        self.__nombre = nombre
        self.__vitalidad = 50
        self.__fortuna = 50

    @property
    def vitalidad(self):
        """Propiedad de solo lectura que devuelve la vitalidad de este
        aventurero."""
        return self.__vitalidad

    def pelea(self, monstruo):
        """Realizar una pelea entre este aventurero y un monstruo. Si el
        monstruo gana, la vitalidad se reduce a la mitad, de lo contrario
        la fortuna crece por 20 puntos."""
        if monstruo.vence():
            self.__vitalidad //= 2
        else:
            self.__fortuna += 20

    def __str__(self):
        """Devuelve una cadena de caracteres con una representación
        informal de este aventurero."""
        return (
f'''Soy un aventurero, me llamo {self.__nombre}.
Mi vitalidad es: {self.__vitalidad}.
Mi fortuna es: {self.__fortuna}.''')


class HombreLobo:
    """Una instancia de esta clase representa un hombre lobo."""

    def vence(self):
        """Devuelve True o False de manera aleatoria pare indicar si este 
        hombre lobo venció a un adversario."""
        return choice([True, False])


# -------------------------------------------------------------------
# Código de prueba
        
a1 = Aventurero('Juan sin miedo')
a2 = Aventurero('Indiana Jones')
lobo1 = HombreLobo()

print(a1)
print()
print(a2)
print()

print('Peleando con un hombre lobo...')
print()
a1.pelea(lobo1)
print('Resultado:')
print(a1)
