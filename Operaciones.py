# -*- coding: cp1252 -*-
# import pytest

'''****************************************************************************
ITCR Curso MT-7003 Mirocpocesadores y Microcontroladores
Tarea 1 Github, Pytest Y Flake 8
Creadores: Carlos Coronado Zuñiga y Adrián Monge Barahona
*****************************************************************************
-   basic_ops(operando_1, operando_2, operacion): Este método recibe 3
parámetros; operando_1 , operando_2 y operación. Los 2 primeros son para
ingresar los operandos para realizar alguna de las 4 posibles operaciones
que puede realizar este método. El tercer parámetro corresponde a la elección
de la operación que se quiere realizar.
Para elegir la operación, se debe ingreasar como parámetro operacion alguno de
los siguientes números:
                            1  ----> Suma
                            2 ----> Resta
                            3 ----> AND
                            4 ----> OR
Este método retorna el resultado de la operación que se eligió, o bien, un
mensaje de error. Estos mensajes de error aparecirán  si ocurre alguno de los
siguientes eventos:
* Si alguno de los parámetros ingresados al método no corresponden a un número
entero -----> Error_1 = TypeError.
* Si el parámetro operando_1, o bien, el parámetro operando_2  no están dentro
del rango que va desde -127 hasta 127 -----> Error_2 = RangeError.
* Si el numero ingrasado como parámetro operacion no coincida a ninguna de
las opciones mencionadas anteriormente -----> Error_3 = OpOutOfRangeError.


-   array_ops(operando_1, operando_2, operacion): Este método recibe igualmente
3 parámetros. Sin embargo, los parámetros operando_1 y operando_2 ahora deben
ser arreglos de números enteros, ambos, con n cantidad de elementos, los cuales
son determinados por el usuario a su conveniencia. El parámetro operación,
igual que en el método anterior, sirve para selecionar la operación que se
desea realizar y tiene la misma funcionalidad.
Este método retorna como resultado un arreglo con la misma cantidad n de
elementos anterior, y sus elementos corresponden al resultado de realizar
la operación seleccionada entre el mismo indice de ambos operandos. Ejemplo:
[a, b, c]+[d, e, f] = [a+d, b+e, c+f]
Este método tiene los mismos mensajes de error que el método anterior y ocurren
con solo que uno de los elementos, ya sea de los arreglos de los operandos, o
bien, del parámetro operación no cumpla con las restricciones y por lo tanto,
no se realizará ninguna operación hasta que todos los elementos ingresados
cumplan con las restricciones.
También, para este método, se agregó otra restricción con su respectivo código
de error y es el siguiente:
* Si los arreglos ingresados como parámetros, operando_1 y operando_2, no
tienen el mismo tamaño -----> Error_4 = LenError
''''''**********************************************************************'''


def basic_ops(operando_1, operando_2, operacion):
    if (type(operando_1) == int and type(operando_2) == int
            and type(operacion) == int):  # Cond.Error_1
        if (-128 < operando_1 < 128 and -128 < operando_2 < 128):
            # ^Cond.Error_2
            if operacion == 1:
                resultado = operando_1 + operando_2  # Operación 1
                return resultado
            elif operacion == 2:
                resultado = operando_1 - operando_2  # Operación 2
                return resultado
            elif operacion == 3:
                resultado = operando_1 & operando_2  # Operación 3
                return resultado
            elif operacion == 4:
                resultado = operando_1 | operando_2  # Operación 4
                return resultado
            else:                  # Cond.Error_3
                print("Error_3 = OpOutOfRangeError: la operación ingresada "
                      "no está dentro de las opciones.")  # Mensaje Error_3
        else:
            print("Error_2 = RangeError: Entrada fuera del rango válido.")
            # ^Mensaje Error_2
    else:
        print("Error_1 = TypeError: Valores ingresados no corresponden a "
              "números enteros")  # Mensaje Error_1


'''
El método array_ops llama a la función basic_ops para realizar las operaciones
entre los elementos de ambos operandos.
Con la función len () se obtiene el tamaños de los arreglos.
'''


def array_ops(operando_1, operando_2, operacion):
    if len(operando_1) == len(operando_2):  # Cond.Error_4
        resultado = []  # Inicializa el arreglo de salida
        for i in range(0, len(operando_1)):
            # ^Ciclo for que recorre todos los indices de los arreglos
            if (type(operando_1[i]) == int and type(operando_2[i]) == int
                    and type(operacion) == int):  # Cond.Error_1
                if (-128 < (operando_1[i]) < 128
                        and -128 < (operando_2[i]) < 128):  # Cond.Error_2
                    if 1 <= operacion <= 4:             # Cond.Error_3
                        a = basic_ops(operando_1[i], operando_2[i], operacion)
                        # ^"a" almacena el valor que retorna llamar a basic_ops
                        resultado = resultado + [0]
                        ''' ^con esto se añade un nuevo indice al areglo
                        y así comenzar a ingresar los resultados de las
                        operaciones '''
                        resultado[i] = a  # Se ingresa el resultado al arreglo
                    else:
                        print("Error_3 = OpOutOfRangeError: la operación "
                              "ingresada no está dentro de las opciones")
                        # ^Mensaje Error_3
                        resultado = None  # Vacía el arreglo en caso de error
                        break       # Termina el ciclo for en caso de error
                else:
                    print("Error_2 = RangeError: Entrada fuera del rango "
                          "válido ")  # Mensaje Error_2
                    resultado = None    # Vacía el arreglo en caso de error
                    break     # Termina el ciclo for en caso de error
            else:
                print("Error_1 = TypeError: Valores ingresados no "
                      "corresponden a números enteros")     # Mensaje Error_1
                resultado = None    # Vacía el arreglo en caso de error
                break                   # Termina el ciclo for en caso de error
        return resultado    # Se retorna el arreglo final
    else:
        print("Error_4 = LenError: Los arreglos no son del mismo tamaño")
        # ^Mensaje Error_4
