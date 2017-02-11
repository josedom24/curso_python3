# Curso: Introducción a python3

## Unidades

### Introducción

1. [Introducción a python](u1)
2. [Python2 us python3](u2)
3. [Instalación de python3](u3)
	* Instalación en linux debian/Ubuntu
	* Instalación en otras distribuciones linux
	* Instalación en Windows
	* Instalación en Mac
4. [Entornos de desarrollos y editores de texto](u4)
	* IDE python
	* Editores de textos
	* IDE us Editores de texto
	* Características de los editores de textos
5. [Mi primer programa en python3](u5)
	* Uso del interprete
	* Escribimos un programa
	* La importancia de la tabulación
	* Ejecutamos el programa con el interprete
	* Codificación de caracteres en el fichero fuente
	* Ejecución de programas usando [shebang](https://es.wikipedia.org/wiki/Shebang)
	* Guía de estilo

	### Estructura del lenguaje

6. [Estructura del programa](u6)
	* Instrucciones. Estructura secuencial
	* Los comentarios
	* La importancia de la tabulación
	* Palabras reservadas
	
7. [Funciones y constantes predefinidas](u7)
	* Se muestran las más utilizadas.
	* Función help()
	* A lo largo del curso se van utilizando las que necesitemos
	* Constantes: False,True,None, ...
8. Datos
	* Literales, variables y expresiones
	* Nombres de variables
	* Definición, borrado y ámbito de variables
	* Operación. Precedencia de operadores
9. Tipos de datos 
	* En Pytho3 tenemos el concepto de tipo.
	* Función type()
	* Los tipos más importantes en python3 son: numéricos, secuencias, mapas, cadenas, clases, objetos.
	* Otros tipos: Iterador, conjuntos
10. Asignando datos a las variables
	* En python todo es una referencia (puntero)
	* Función id()
	* Objetos mutables e inmutables
	* Inmutables son los números, las cadenas o las tuplas.
	* Mutables son otros objetos como los diccionarios o las listas.

	### Tipos de datos numéricos

11. Tipo de datos numéricos: 
	* enteros
	* reales
	* complejos
	* Operaciones aritméticas.
	* Funciones predefinidas que trabajan con números: abs(), divmod(), hex() oct(x), pow(), round()
	* Conversión de tipos
2. Tipo de dato booleanos. 
	* Tipo booleano es un subtipo de un tipo entero
	* Operadores booleanos
	* Operadores de comparación
	* ¿Qué valores se interpretan como FALSO?
	* Funciones all() y any()

	### Tipos de datos secuencia

1. Tipo de datos secuencia
	* Listas, tuplas, rangos
	* Características principales de las secuencias
2. Tipo de datos secuencia: Listas
	* Definición de una lista. Constructor list
	* Las listas son mutables
	* Indexación y recorrido de una lista
	* Funciones predefinidas: len, sum, max, min, sorted
	* Concatenación de listas
	* Operadores in, not in, +, *
	* Slice 
	* Función enumerate()
	* Listas multidimensionales
	* ¿Cómo se copian las listas?

3. Métodos principales de listas
	* Métodos de inserción: append, extend, insert
	* Métodos de eliminación: pop, remove
	* Métodos de ordenación: reverse, sort, 
	* Métodos de búsqueda: count, index

4. Operaciones avanzadas con listas

	* Función map
	* Función filter
	* Función reduce
	* list comprehension

5. Tipo de datos secuencia: Tuplas
	* Definición de una tupla. Constructor tuple
	* Las listas son inmutables
	* Indexación de una tubla
	* Métodos principales
	* Conversión entre listas y tuplas

6. Tipo de datos secuencia: Rangos
	* Definición de un rango. Constructor range
	* Recorrido de un rango
	* Métodos principales de range
	* Creación de listas a partir de rangos

7. Codificación de caracteres
	* Introducción a la codificación de caracteres
	* Funciones chr() y ord()

8. Tipo de datos cadenas de caracteres.
	* Definición de cadenas.  Constructor str
	* Indexación y recorrido de cadenas
	* Slice
	* Concatenación de cadenas
	* Funciones str, repr, ascii
	* Conversión de cadenas a números, y de números a cedenas. 
	* Función bin()

9. Métodos principales de cadenas
	* Métodos de formato: capitalize, lower, upper, swapcase, title, center, ljust, rjust, zfill
	* Métodos de búsqueda: count, find
	* Métodos de validación: statrswith, endswith, isalnum, isalpha, isdigit, islower, isupper, isspace, istitle
	* Métodos de sustitución: format, replace, strip, lstrip, rstrip
	* Métodos de unión y división: join, partition, split, splitlines, 

10. Tipo de datos: datos binarios (bytes)
	* Introducción al manejo de datos binarios
	* Métodos principales
11. Tipo de datos conjuntos
	* Set, frozenset
	* Métodos principales
12. Tipo de datos iterador y generador
	* Iteradores
	* Función next(), reversed()
	* Generadores

	### Tipos de datos mapas

1. Tipo de datos mapa
	* Definición de diccionarios. Constructor dict
	* Contar elementos de un diccionario: len
	* Acceso, modificación y recorrido de diccionarios
	* dictviews

2. Métodos principales de diccionarios
	* Métodos de eliminación: clear
	* Métodos de agregado y creación: copy, dict.fromkeys, update, setdefault
	* Métodos de retorno: get, has_ket, items, Keys, values

	### Entrada y salida de información

1. Entrada y salida estándar
	* Función print (palabra reservada end)
	* 4.7.2. printf-style String Formatting¶
	* Función input
	* Función format()

	### Ejercicios tipos de datos

1. Ejercicios de programas sencillos.
2. Ejercicios de listas
3. Ejercicios de cadenas
4. Ejercicios de diccionarios

	### Estructuras de control

5. Estructuras de control: Alternativas.
	* Alternativas simples
	* Alternativas dobles
	* Alternativas múltiples
	* Expresión reducida del if 
6. Estructuras de control: Repetitivas.
	* for
	* while
	* Instrucciones break, continue, else y pass
	* Recorriendo varias listas. Función zip()

	### Ejercicios estructuras de control

1. Ejercicios de alternativas
2. Ejercicios de repetitivas

	### Trabajar con ficheros

1. Lectura y escritura de ficheros de textos
	* Función open()
	* Objeto fichero
	* Modos de acceso
	* Metodos principales
2. Gestionar ficheros CSV
	* Módulo csv
	* Funciones principales
3. Gestionar ficheros json
	* Módulo json
	* Funciones principales

	### Errores y Excepciones

1. Excepciones
	* Errores sintácticos y errores de ejecución
	* Excepciones. Tipos.
	* Manejando excepciones. try, except, else, finally
	* Lanzando excepciones. raise

	### Módulos, paquetes y namespaces

1. Definición Módulos, paquetes y namespaces
2. Importando módulos
	* import
	* from ... import
	* Función dir()

3. Introducciones a los módulos estándares
	* Módulo os
	* Módulos sys. Ejecución se scripts con argumentos
	* Módulo glob
	* Módulo re
	* Módulo math
	* Módulo random
	* Módulo datetime
	* Módulo calendar
4. Instalación de módulos
	* pip

	### Programación imperativa

1. Introducción a las Funciones
	* Introducción a la programación imperativa
	* Definición de funciones
	* Ámbito de variables. Sentencia global
	* Argumentos formales y argumentos reales
	* Llamada a una función
	* La instrucción return

2. Conceptos avanzados sobre funciones
	* Parámetros con valores por defecto
	* Tipos de argumentos: posicionales o keyword
	* Lista de argumentos arbitrarios
	* Desempaquetar argumentos: pasar listas y diccionarios
	* Devolver múltiples resultados
	* Documentando las funciones
	* El método main()
	* Decoradores
3. Funciones lambda
4. Funciones recursivas

	### Ejercicios programación imperativa

1. Ejercicios con funciones
2. Programación imperativa: Ejemplo completo 

	### Programación orientada a objetos

1. Clases y objetos
	* Introducción a la POO
	* Definición de clases: atributos y métodos
	* Método constructor __init__
	* Atributos de objetos
	* Definiendo métodos. El parámetro self
	* Definición de objetos

2. Conceptos avanzados de clases y objetos
	* Atributos de clase (estáticas)
	* Atributos privados 
	* Métodos estáticos
	* Métodos de clase
	* Funciones getattr,setattr,delattr,hasattr
	* Propiedades: getters, setters, deleter
	* __str__ y __repr__
	* Comparación de objetos __eq__

3. Herencia
	* Concepto de herencia
	* La función super()
	* Herencia múltiple
	* Polimorfismo y delegación


	### Ejercicios programación orientada a objetos

1. Ejercicios de clases y objetos
2. POO: Ejemplo completo


