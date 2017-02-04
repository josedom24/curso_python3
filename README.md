# Curso: Introducción a python3

## Unidades

### Introducción

1. [Introducción a python](u1)
2. Python2 us python3
3. Instalación de python3
4. Entornos de desarrollos y editores de texto
5. Interprete mejorado: ipython3
5. Mi primer programa en python3
	* Uso del interprete
	* Escribimos un programa
	* La importancia de la tabulación
	* Ejecutamos el programa con el interprete
	* Codificación de caracteres en el fichero fuente
	* Ejecución de programas usando [shebang](https://es.wikipedia.org/wiki/Shebang)
	* Guía de estilo

### Estructura del lenguaje

5. Estructura del programa
	* Instrucciones. Estructura secuencial
	* Los comentarios
	* La importancia de la tabulación
	* Función help()
6. Funciones predefinidas
	* Se muestran las más utilizadas.
	* A lo largo del curso se van utilizando las que necesitemos
7. Constantes predefinidas
	* False,True,None, ...
7. Datos
	* Literales, variables y expresiones
	* Nombres de variables y palabras reservadas
	* Definición, borrado y ámbito de variables
	* Operación. Precedencia de operadores
6. Tipos de datos 
	* En Pytho3 tenemos el concepto de tipo.
	* Función type()
	* Los tipos más importantes en python3 son: numéricos, secuencias, mapas, cadenas, clases, objetos.
	* Otros tipos: Iterador, conjuntos
7. Asignando datos a las variables
	* En python todo es una referencia (puntero)
	* Objetos mutables e inmutables
	* Inmutables son los números, las cadenas o las tuplas.
	* Mutables son otros objetos como los diccionarios o las listas.


### Tipos de datos numéricos

7. Tipo de datos numéricos: 
	* enteros
	* reales
	* complejos
	* Operaciones aritméticas.
	* Funciones predefinidas que trabajan con números
	* Conversión de tipos
8. Tipo de dato booleanos. 
	* Tipo booleano es un subtipo de un tipo entero
	* Operadores booleanos
	* Operadores de comparación
	* ¿Qué valores se interpretan como FALSO?

### Tipos de datos secuencia

9. Tipo de datos secuencia
	* Listas, tuplas, rangos
	* Características principales de las secuencias
10. Tipo de datos secuencia: Listas
	* Definición de una lista. Constructor list
	* Las listas son mutables
	* Indexación y recorrido de una lista
	* Funciones predefinidas: len,sum, max, min,...
	* Operadores in, not in, +, *
	* Slice 
	* Métodos principales
	* Listas multidimensionales
	* ¿Cómo se copian las listas?

11. Tipo de datos secuencia: Tuplas
	* Definición de una tupla. Constructor tuple
	* Las listas son inmutables
	* Indexación de una tubla
	* Métodos principales
	* Conversión entre listas y tuplas

12. Tipo de datos secuencia: Rangos
	* Definición de un rango. Constructor range
	* Recorrido de un rango
	* Métodos principales de range
	* Creación de listas a partir de rangos
10. Codificación de caracteres
12. Tipo de datos cadenas de caracteres.
	* Definición de cadenas.  Constructor str
	* Indexación y recorrido de cadenas
	* Slice
	* Métodos principales
	* Funciones str, repr, ascii
	* Conversión de cadenas a números, y de números a cedenas
	* Codificación de las cadenas en python3

14. Tipo de datos: datos binarios (bytes)
	* Introducción al manejo de datos binarios
	* Métodos principales
15. Tipo de datos conjuntos
	* Set, frozenset
	* Métodos principales

### Tipos de datos mapas

16. Tipo de datos mapa
	* Definición de diccionarios. Constructor dict
	* Acceso, modificación y recorrido de diccionarios
	* Métodos principales
	* dictviews


### Entrada y salida de información

6. Entrada y salida estándar
	* Función print (palabra reservada end)
	* 4.7.2. printf-style String Formatting¶
	* Función input

### Ejercicios tipos de datos

11. Ejercicios de programas sencillos.
12. Ejercicios de listas
12. Ejercicios de cadenas
12. Ejercicios de diccionaios

### Estructuras de control

12. Estructuras de control: Alternativas.
	* Alternativas simples
	* Alternativas dobles
	* Alternativas múltiples
	* Expresión reducida del if 
15. Estructuras de control: Repetitivas.
	* for
	* while
	* Instrucciones break, continue, else y pass
	* Recorriendo varias listas. Función zip()

### Ejercicios estructuras de control

16. Ejercicios de alternativas
16. Ejercicios de repetitivas


### Trabajar con ficheros

27. Lectura y escritura de ficheros de textos
	* Objeto fichero
	* Modos de acceso
	* Metodos principales
28. Gestionar ficheros CSV
	* Módulo csv
	* Funciones principales
29. Gestionar ficheros json
	* Módulo json
	* Funciones principales

### Errores y Excepciones

28. Excepciones
	* Errores sintácticos y errores de ejecución
	* Excepciones. Tipos.
	* Manejando excepciones. try, except, else, finally
	* Lanzando excepciones. raise

### Módulos, paquetes y namespaces

29. Definición Módulos, paquetes y namespaces
30. Importando módulos
	* import
	* from ... import
	* Función dir()
	

30. Introducciones a los módulos estándares
	* Módulo os
	* Módulos sys. Ejecución se scripts con argumentos
	* Módulo glob
	* Módulo re
	* Módulo math
	* Módulo random
	* Módulo datetime
	* Módulo calendar
31. Instalación de módulos
	* pip

### Programación imperativa

32. Introducción a las Funciones
	* Introducción a la programación imperativa
	* Definición de funciones
	* Ámbito de variables. Sentencia global
	* Argumentos formales y argumentos reales
	* Llamada a una función
	* La instrucción return

33. Conceptos avanzados sobre funciones
	* Parámetros con valores por defecto
	* Tipos de argumentos: posicionales o keyword
	* Lista de argumentos arbitrarios
	* Desempaquetar argumentos: pasar listas y diccionarios
	* Devolver múltiples resultados
	* Documentando las funciones
	* El método main()
	* Decoradores

34. Funciones recursivas

### Ejercicios programación imperativa

33. Ejercicios con funciones
34. Programación imperativa: Ejemplo completo 

### Programación funcional

1. Función map
2. Función filter
3. Función reduce
4. Función lambda
5. list comprehension


### Programación orientada a objetos

35. Clases y objetos
	* Introducción a la POO
	* Definición de clases: atributos y métodos
	* Método constructor __init__
	* Atributos de objetos
	* Definiendo métodos. El parámetro self
	* Definición de objetos

36. Conceptos avanzados de clases y objetos
	* Atributos de clase (estáticas)
	* Atributos privados 
	* Métodos estáticos
	* Métodos de clase
	* Propiedades: getters, setters, deleter
	* __str__ y __repr__
	* Comparación de objetos __eq__

37. Herencia
	* Concepto de herencia
	* La función super()
	* Herencia múltiple
	* Polimorfismo y delegación


### Ejercicios programación orientada a objetos

36. Ejercicios de clases y objetos
40. POO: Ejemplo completo


