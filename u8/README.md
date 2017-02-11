# Datos

## Literales, variables y expresiones

### Literales

Los literales nos permiten representar valores. Estos valores pueden ser de diferentes tipos, de esta manera tenemos diferentes tipos de literales:

**Literales numéricos**

* Para representar números enteros utilizamos cifras enteras (Ejemplos: 3, 12, -23). Si queremos representarlos de forma binaria comenzaremos por la secuencia `0b` (Ejemplos: 0b10101, 0b1100). La representación octal la hacemos comenzando por `0o` (Ejemplos: 0o377, 0o7) y por último, la representación hexadecimal se comienza por `0x` (Ejemplos: 0xdeadbeef, 0xfff).

Para los números reales utilizamos un punto para separar la parte entera de la decimal (12.3, 45.6). Podemos indicar que la parte decimal es 0, por ejemplo 10., o la parte entera es 0, por ejemplo .001, Para la representación de números muy grandes o muy pequeños podemos usar la representación exponencial (Ejemplos: 3.14e-10,1e100).

**Literales cadenas**

Nos permiten representar cadenas de caracteres. Para delimitar las cadenas podemos usar el carácter ' o el carácter ". También podemos utilizar la combinación ''' cuando la cadena ocupa más de una línea. Ejemplos.

	'hola que tal!'
	"Muy bien"
	'''Podemos \n
	ir al cine'''

Las cadenas anteriores son del tipo `str`, si queremos representar una cadena de tipo `byte` podremoas hacerlo de la siguiente nera:

	b'Hola'
	B"Muy bien"

Con el carácter /, podemos escapar algunos caracteres, veamos algunos ejemplos:

	\\ 	Backslash (\) 	 
	\' 	Single quote (') 	 
	\" 	Double quote (") 	 
	\a 	ASCII Bell (BEL) 	 
	\b 	ASCII Backspace (BS) 	 
	\f 	ASCII Formfeed (FF) 	 
	\n 	ASCII Linefeed (LF) 	 
	\r 	ASCII Carriage Return (CR) 	 
	\t 	ASCII Horizontal Tab (TAB) 	 
	\v 	ASCII Vertical Tab (VT)

### Variables

Una variables es un identificador que referencia a un valor. Estudiaremos más adelante que python utiliza tipado dinámico, lo tan no se usa el concepto de variable como almacén de información. Para que una variable reverencie a un valor se utiliza el operador de asignación `=`.

El nombre de una variable, ha de empezar por una letra o por el carácter guión bajo, seguido de letras, números o guiones bajos. No hay que declarar la variable antes de usarla, el tipo de la variable será el mismo que el del valor al que hace referencia. Por lo tanto su tipo puede cambiar en cualquier momento:

	>>> var = 5
	>>> type(var)
	<class 'int'>
	>>> var = "hola"
	>>> type(var)
	<class 'str'>

Hay que tener en cuanta que python distingue entre mayúsculas y minúsculas en el nombre de una variable, pero se recomienda usar sólo minúsculas.

### Expresiones

Una expresión es una combinación de variables, literales, operadores, funciones y expresiones, que tras su evaluación o cálculo nos devuelven un valor de un determinado tipo. Los operadores que podemos utilizar se clasifican según el tipo de datos con los que trabajen y podemos poner algunos ejemplos:

	+       -       *       **      /       //      %
	<<      >>      &       |       ^       ~
	<       >       <=      >=      ==      !=
	-=      *=      /=      //=     %=

Veamos ejemplos de expresiones:

	a + 7
	(a ** 2) + b

### 
