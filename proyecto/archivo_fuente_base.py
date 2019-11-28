# ----------------------------------------------------------
#
# Escribe aquí tu matrícula y nombre.
#
# ----------------------------------------------------------

# NOTA: El siguiente código solo es el esqueleto para inciar el
# proyecto. Los métodos provistos crean la estructura básica con
# todos los objetos que intervienen en el sistema de reservaciones
# de vuelos. Queda pendiente implementar el comportamiento
# descrito en la especificación y añadir la documentación
# correspondiente. Es posible que se requiera añadir nuevos
# métodos y propiedades a las clases definidas a continuación.

from datetime import date


class ReservadorDeVuelos:

    def __init__(self):
        self.__vuelos = {}

    def define_vuelo(self,
                     codigo,
                     origen,
                     destino,
                     fecha,
                     num_filas,
                     num_letras):
        self.__vuelos[codigo] = Vuelo(codigo, origen, destino,
                                      fecha, num_filas, num_letras)

    def imprime_info_vuelo(self, codigo):
        pass

    def reserva_vuelo(self, codigo, fila, letra):
        pass

    def busca_vuelos(self, origen, destino):
        pass


class Vuelo:

    def __init__(self,
                 codigo,
                 origen,
                 destino,
                 fecha,
                 num_filas,
                 num_letras):
        self.__codigo = codigo
        self.__origen = origen
        self.__destino = destino
        self.__fecha = fecha
        self.__num_filas = num_filas
        self.__num_letras = num_letras

        # Crear las filas de asientos desocupados.
        # A partir de este momento, si queremos
        # acceder al asiento 1A de este vuelo se
        # puede hacer de la siguiente manera:
        #
        #     self.__asientos[1]['A']
        #
        self.__asientos = {}
        for num_fila in range(1, num_filas + 1):
            fila = {}
            for letra in 'ABCDEFGHIJ'[:num_letras]:
                fila[letra] = Asiento()
            self.__asientos[num_fila] = fila


class Asiento:

    def __init__(self):
        self.__ocupado = False
