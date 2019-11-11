"""Esta es una pequeña prueba.
Todo bien.
"""

otro = 'Hola a todos'

def iniciales(nombre, paterno, materno):
    """Devuelve las inciales de nombre, paterno y materno.
    """
    nombres = nombre.split()
    if len(nombres) > 1:
        inicial1 = nombres[0][0] + nombres[1][0]
    else:
        inicial1 = nombre[0]
    inicial2 = paterno[0]
    inicial3 = materno[0]
    todo = (inicial1 + inicial2 + inicial3).upper()
    return todo