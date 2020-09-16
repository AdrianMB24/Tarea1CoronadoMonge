# El archivo Operaciones.py debe estar en la misma carpeta que este código
# Para este código se ingresaron 5 errores detectables por flake8

import pytest  # Error1: No se utilizará esta librería
import Operaciones  # Se llama al código de las funciones basic_ops y array_ops

# Error 2: Se debe dejar doble línea en blanco

# Se define un método que prueba cada operación de basic_ops mediante asserts
def test_basic_ops():
    assert Operaciones.basic_ops(1, 2,1) == 3
    # Error3: coma sin espacio depués
    assert Operaciones.basic_ops(1, 2, 2) == -1
    assert Operaciones.basic_ops (1, 2, 3) == 0
    # Error4: espacio despues de func.
    assert Operaciones.basic_ops(2, 5, 4) ==7
    # Error5: espacio despues de operad.


# Se define funcion que prueba cada operación de array_ops mediante asserts
def test_array_ops():
    assert Operaciones.array_ops([4, 7, -59], [5, 8, 2], 1) == [9, 15, -57]
    assert Operaciones.array_ops([87, 4, -27], [6, 7, -2], 2) == [81, -3, -25]
    assert Operaciones.array_ops([76, -2, 7], [76, 3, 1], 3) == [76, 2, 1]
    assert Operaciones.array_ops([5, -28, 12], [9, 30, 12], 4) == [13, -2, 12]
