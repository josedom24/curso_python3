# Trabajando con variables

Como hemos indicado anteriormente las variables en python no se declaran, se determina su tipo en tiempo de ejecución empleando una técnica que se lama **tipado dinámico**.

## ¿Qué es el tipado dinámico?

En python cuando asignamos una variable, se crea una referencia (puntero) al objeto creado, en ese momento se determina el tipo de la variable. Por lo tanto cada vez que asignamos de nuevo la variable puede cambiar el tipo en tempo de ejecución.

	>>> var = 3
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>


## Objetos inmutables y mutables

### Objetos inmutables

Python procura no consumir más memoria que la necesaria. Ciertos objetos son **inmutables**, es decir, no pueden modificar su valor. El número 2 es siempre el núumero 2. Es un objeto inmutable. Python procura almacenar en memoria una sola vez cada valor inmutable. Si dos o más variables contienen ese valor, sus referencias apuntan a la misma zona de memoria.

**Ejemplo**

Para comprobar esto, vamos a utilizar la función `id`, que nos devuelve el identificador de la variable o el objeto en memoria.

Veamos el siguiente código:

	>>> a = 5

Podemos comprobar que `a` hace referencia al objeto `5`.
	
	>>> id(5)
	10771648
	>>> id(a)
	10771648

Esto es muy distinto a otros lenguajes de programación, donde una variable ocupa un espacio de memoria que almacena un valor. Desde este punto cuando asigno otro número a la variable estoy cambiando la referencia.

	>>> a = 6
	>>> id(6)
	10771680
	>>> id(a)
	10771680

Las cadenas también son un objeto **inmutable**, que lo sean tiene efectos sobre las operaciones que podemos efectuar con ellas. La asignación a un elemento de una
cadena, por ejemplo está prohibida:

	>>> a = "Hola"
	>>> a[0]="h"
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	TypeError: 'str' object does not support item assignment

De los tipos de datos principales, hay que recordar que son inmutables son los números, las cadenas o las tuplas.

### Objetos mutables

El caso contrario lo tenemos por ejemplo en los objetos de tipo listas, en este caso las listas son mutables. Se puede modificar un elemento de una lista.

**Ejemplo**

	>>> a = [1,2]
	>>> b = a
	>>> id(a)
	140052934508488
	>>> id(b)
	140052934508488

Como anteriormente vemos que dos variables referencia a la misma lista e memoria. Pero aquí viene la diferencia, al poder ser modificada podemos encontrar situaciones como la siguiente:

	>>> a[0] = 5
	>>> b
	[5, 2]

Cuando estudiamos las listas abordaremos este compartiendo de manera completa.
De los tipos de datos principales, hay que recordar que son mutables son las listas y los diccionarios.

## Operadores de identidad

Para probar esto de otra forma podemos usar los operadores de identidad:

* `is`: Devuelve True si dos variables u objetos están referenciando la misma posición de memoria. En caso contrario devuelve False.
* `is not`: Devuelve True si dos variables u objetos **no** están referenciando la misma posición de memoria. En caso contrario devuelve False.

**Ejemplo**

	>>> a = 5
	>>> b = a
	>>> a is b
	True
	>>> b = b +1
	>>> a is b
	False
	>>> b is 6
	True

	
## Operadores de asignación

Me permiten asignar una valor a una variable, o mejor dicho: me permiten cambiar la referencia a un nuevo objeto.

El operador principal es `=`:

	>>> a = 7
	>>> a
	7

Podemos hacer diferentes operaciones con la variable y luego asignar, por ejemplo sumar y luego asignar.

	>>> a+=2
	>>> a
	9

Otros operadores de asignación: `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

## Asignación múltiple

En python se permiten asignaciones múltiples de esta manera:

	>>> a, b, c = 1, 2, "hola"