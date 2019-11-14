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
            print(f'Ganó {monstruo}')
            self.__vitalidad //= 2
        else:
            print(f'Perdió {monstruo}')
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
    
    def __init__(self, nombre):
        """Inicializa uan instancia de la clase HombreLobo."""
        self.nombre = nombre
        self.__fuerza = [True, False]
        
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, valor):
        if type(valor) == str and valor != '':
            self.__nombre = valor
        else:
            raise Exception(f'Nombre no válido: "{valor}"')
    
    @property
    def fuerza(self):
        return len(self.__fuerza)

    def vence(self):
        """Devuelve True o False de manera aleatoria pare indicar si este 
        hombre lobo venció a un adversario."""
        resultado = choice(self.__fuerza)
        if resultado:
            self.__fuerza.append(True)
        else:
            self.__fuerza = [False]
        return resultado
    
    def __str__(self):
        return f'Hombre Lobo: {self.nombre}'

# -------------------------------------------------------------------
# Código de prueba
        
def juego():
    aventurero = Aventurero('Abraham Van Helsing')
    hombre_lobo = HombreLobo('Larry Talbot')
    
    contador = 1
    while aventurero.vitalidad > 0 and contador <= 20:
        print('A punto de pelear...')
        aventurero.pelea(hombre_lobo)
        print(aventurero)
        contador += 1
    print(f'Fuerza del hombre lobo: {hombre_lobo.fuerza}')

juego()
