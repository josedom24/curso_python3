# Tipo de datos booleanos

## Tipo booleano

El tipo booleano o lógico se considera en python3 como un subtipo del tipo entero. Se puede representar dos valores: verdadero o false (True, False).

## ¿Qué valores se interpretan como FALSO?

Cuando se evalua una expresión, hay determinados valores que se interpretan como False:

* `None`
* `False`
* Cualquier número 0. (0, 0.0, 0j)
* Cualquier secuencia vacía ([], (), '')
* Cualquir diccionario vacío ({})

## Operadores booleanos

Los operadores booleanos se utilizan para operar sobre expresiones booleanas y se suelen utilizar en las estructuras de control alternativas (if, while):

* `x or y`: Si x es falso entonces y, sino x. Este operados sólo evalua el segundo argumento si el primero es False.
* `x and y`: Si x es falso entonces x, sino y. Este operados sólo evalua el segundo argumento si el primero es True.
* `not x`: Si x es falso entonces True, sino False.

## Operadores de comparación

`== != >= > <= <`

## Funciones all() y any()

* `all(iterador)`: Recibe un iterador, por ejemplo una lista, y devuelve True si todos los elementos son verdaderos o el iterador está vacío. 
* `any(iterador)`: Recibe un iterador, por ejemplo una lista, y devuelve True si alguno de sus elemento es verdadero, sino devuelve False.
