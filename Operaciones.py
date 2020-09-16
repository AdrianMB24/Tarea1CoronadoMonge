# -*- coding: cp1252 -*-
# import pytest

'''****************************************************************************
ITCR Curso MT-7003 Mirocpocesadores y Microcontroladores
Tarea 1 Github, Pytest Y Flake 8
Creadores: Carlos Coronado Zu�iga y Adri�n Monge Barahona
*****************************************************************************
-   basic_ops(operando_1, operando_2, operacion): Este m�todo recibe 3
par�metros; operando_1 , operando_2 y operaci�n. Los 2 primeros son para
ingresar los operandos para realizar alguna de las 4 posibles operaciones
que puede realizar este m�todo. El tercer par�metro corresponde a la elecci�n
de la operaci�n que se quiere realizar.
Para elegir la operaci�n, se debe ingreasar como par�metro operacion alguno de
los siguientes n�meros:
                            1  ----> Suma
                            2 ----> Resta
                            3 ----> AND
                            4 ----> OR
Este m�todo retorna el resultado de la operaci�n que se eligi�, o bien, un
mensaje de error. Estos mensajes de error aparecir�n  si ocurre alguno de los
siguientes eventos:
* Si alguno de los par�metros ingresados al m�todo no corresponden a un n�mero
entero -----> Error_1 = TypeError.
* Si el par�metro operando_1, o bien, el par�metro operando_2  no est�n dentro
del rango que va desde -127 hasta 127 -----> Error_2 = RangeError.
* Si el numero ingrasado como par�metro operacion no coincida a ninguna de
las opciones mencionadas anteriormente -----> Error_3 = OpOutOfRangeError.


-   array_ops(operando_1, operando_2, operacion): Este m�todo recibe igualmente
3 par�metros. Sin embargo, los par�metros operando_1 y operando_2 ahora deben
ser arreglos de n�meros enteros, ambos, con n cantidad de elementos, los cuales
son determinados por el usuario a su conveniencia. El par�metro operaci�n,
igual que en el m�todo anterior, sirve para selecionar la operaci�n que se
desea realizar y tiene la misma funcionalidad.
Este m�todo retorna como resultado un arreglo con la misma cantidad n de
elementos anterior, y sus elementos corresponden al resultado de realizar
la operaci�n seleccionada entre el mismo indice de ambos operandos. Ejemplo:
[a, b, c]+[d, e, f] = [a+d, b+e, c+f]
Este m�todo tiene los mismos mensajes de error que el m�todo anterior y ocurren
con solo que uno de los elementos, ya sea de los arreglos de los operandos, o
bien, del par�metro operaci�n no cumpla con las restricciones y por lo tanto,
no se realizar� ninguna operaci�n hasta que todos los elementos ingresados
cumplan con las restricciones.
Tambi�n, para este m�todo, se agreg� otra restricci�n con su respectivo c�digo
de error y es el siguiente:
* Si los arreglos ingresados como par�metros, operando_1 y operando_2, no
tienen el mismo tama�o -----> Error_4 = LenError
''''''**********************************************************************'''


def basic_ops(operando_1, operando_2, operacion):
    if (type(operando_1) == int and type(operando_2) == int
            and type(operacion) == int):  # Cond.Error_1
        if (-128 < operando_1 < 128 and -128 < operando_2 < 128):
            # ^Cond.Error_2
            if operacion == 1:
                resultado = operando_1 + operando_2  # Operaci�n 1
                return resultado
            elif operacion == 2:
                resultado = operando_1 - operando_2  # Operaci�n 2
                return resultado
            elif operacion == 3:
                resultado = operando_1 & operando_2  # Operaci�n 3
                return resultado
            elif operacion == 4:
                resultado = operando_1 | operando_2  # Operaci�n 4
                return resultado
            else:                  # Cond.Error_3
                print("Error_3 = OpOutOfRangeError: la operaci�n ingresada "
                      "no est� dentro de las opciones.")  # Mensaje Error_3
        else:
            print("Error_2 = RangeError: Entrada fuera del rango v�lido.")
            # ^Mensaje Error_2
    else:
        print("Error_1 = TypeError: Valores ingresados no corresponden a "
              "n�meros enteros")  # Mensaje Error_1


'''
El m�todo array_ops llama a la funci�n basic_ops para realizar las operaciones
entre los elementos de ambos operandos.
Con la funci�n len () se obtiene el tama�os de los arreglos.
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
                        ''' ^con esto se a�ade un nuevo indice al areglo
                        y as� comenzar a ingresar los resultados de las
                        operaciones '''
                        resultado[i] = a  # Se ingresa el resultado al arreglo
                    else:
                        print("Error_3 = OpOutOfRangeError: la operaci�n "
                              "ingresada no est� dentro de las opciones")
                        # ^Mensaje Error_3
                        resultado = None  # Vac�a el arreglo en caso de error
                        break       # Termina el ciclo for en caso de error
                else:
                    print("Error_2 = RangeError: Entrada fuera del rango "
                          "v�lido ")  # Mensaje Error_2
                    resultado = None    # Vac�a el arreglo en caso de error
                    break     # Termina el ciclo for en caso de error
            else:
                print("Error_1 = TypeError: Valores ingresados no "
                      "corresponden a n�meros enteros")     # Mensaje Error_1
                resultado = None    # Vac�a el arreglo en caso de error
                break                   # Termina el ciclo for en caso de error
        return resultado    # Se retorna el arreglo final
    else:
        print("Error_4 = LenError: Los arreglos no son del mismo tama�o")
        # ^Mensaje Error_4
