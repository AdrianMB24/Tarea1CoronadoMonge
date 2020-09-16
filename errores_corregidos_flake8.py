# Se corrigió Error1 borrando el import pytest
# Se corrigió Error2 dejando doble línea en blanco entre el import y el def
# Se corrigió Error3 dejando un espacio después de la coma
# Se corrigió Error4 eliminando espacio entre nombre de la función y paréntesis
# Se corrigió Error5 agregando un espacio después del operador ==
import Operaciones


def test_basic_ops():
    assert Operaciones.basic_ops(1, 2, 1) == 3
    assert Operaciones.basic_ops(1, 2, 2) == -1
    assert Operaciones.basic_ops(1, 2, 3) == 0
    assert Operaciones.basic_ops(2, 5, 4) == 7


def test_array_ops():
    assert Operaciones.array_ops([4, 7, -59], [5, 8, 2], 1) == [9, 15, -57]
    assert Operaciones.array_ops([87, 4, -27], [6, 7, -2], 2) == [81, -3, -25]
    assert Operaciones.array_ops([76, -2, 7], [76, 3, 1], 3) == [76, 2, 1]
    assert Operaciones.array_ops([5, -28, 12], [9, 30, 12], 4) == [13, -2, 12]
