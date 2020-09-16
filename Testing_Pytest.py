'''****************************************************************************
ITCR Curso MT-7003 Mirocpocesadores y Microcontroladores
Tarea 1 Github, Pytest Y Flake 8
Creadores: Carlos Coronado Zuñiga y Adrián Monge Barahona
****************************************************************************'''


#  Se importan las libreria pytest para la ejecucion de las pruebas
#  Se importa el modulo que contiene las funciones a probar


import Operaciones


# Funciones
#  ---------------------------------------------------------------------------------


def test_basic_ops():
    ''' Definicion de funcion de prueba para compobar el
    correcto funcionamiento de la funcion basic_ops '''

    # llamados a la funcion con afirmaciones de prueba

    assert Operaciones.basic_ops(1, 2, 1) == 3      # Suma
    assert Operaciones.basic_ops(3, 4, 2) == -1     # Resta
    assert Operaciones.basic_ops(1, 2, 3) == 0      # AND
    assert Operaciones.basic_ops(1, 2, 4) == 3      # OR


def test_basic_ops_error__tipo_dato():
    # Definicion de funcion de prueba error

    assert Operaciones.basic_ops(1, 1.0, 1) == 2
    # Afirmacion con entrada de valor decimal


def test_basic_ops_error_fuera_rango():
    # Definicion de funcion de prueba error

    assert Operaciones.basic_ops(7, 220, 4) == 227
    # Afirmacion con entrada de valor fuera de rango[-127,127]


def test_basic_ops_error_op_invalida():
    # Definicion de funcion de prueba error

    assert Operaciones.basic_ops(8, 9, 9) == 0
    # Afirmacion con entrada de operacion no soportada


#  ------------------------------------------------------------------------------------------


def test_array_ops():    # Definicion de funcion de prueba

    #  Prueba para compobar el correcto funcionamiento de la funcion array_ops

    #  llamados a la funcion con afirmaciones de prueba

    assert Operaciones.array_ops([1, 2, 3], [4, 5, 6], 1) == [5, 7, 9]  # Suma
    assert Operaciones.array_ops([4, 5, 8], [1, 5, 6], 2) == [3, 0, 2]  # Resta
    assert Operaciones.array_ops([1, 1, 1], [1, 2, 3], 3) == [1, 0, 1]  # AND
    assert Operaciones.array_ops([1, 2, 3], [1, 1, 0], 4) == [1, 3, 3]  # OR


def test_array_ops_error_tipo_dato():
    # Definicion de funcion de prueba error

    assert Operaciones.array_ops([1, "5", 8], [4, 5, 6], 2) == [-3, 0, 2]
    # Afirmacion con entrada de valor no numerico


def test_array_ops_error_fuera_rango():
    # Definicion de funcion de prueba error

    assert Operaciones.array_ops([1, 1, 1], [1, -800, 3], 3) == [1, 0, 1]
    # Afirmacion con entrada de valor fuera de rango[-127,127]


def test_array_ops_error_op_invalida():
    # Definicion de funcion de prueba error

    assert Operaciones.array_ops([1, 2, 3], [1, 1, 0], 9) == [1, 3, 3]
    # Afirmacion con entrada de operacion no soportada
