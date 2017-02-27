# Curso: Introducción a python3

## Unidades

### Introducción

1. [Introducción a python](curso/u1)
2. [Python2 us python3](curso/u2)
3. [Instalación de python3](curso/u3)
	* Instalación en linux debian/Ubuntu
	* Instalación en otras distribuciones linux
	* Instalación en Windows
	* Instalación en Mac
4. [Entornos de desarrollos y editores de texto](curso/u4)
	* IDE python
	* Editores de textos
	* IDE us Editores de texto
	* Características de los editores de textos
5. [Mi primer programa en python3](curso/u5)
	* Uso del interprete
	* Escribimos un programa
	* Ejecución de programas usando [shebang](https://es.wikipedia.org/wiki/Shebang)
	* Guía de estilo

	### Estructura del lenguaje

6. [Estructura del programa](curso/u6)
	* Estrucutra de programa
	* Los comentarios
	* Palabras reservadas
	* Ejemplo
7. [Funciones y constantes predefinidas](curso/u7)
	* Funciones predefinidas
	* Algunos ejemplos de funciones
	* Constantes predefinidas: False,True,None, ...
	* Ayuda, función help()
8. [Datos](curso/u8)
	* Literales, variables y expresiones
	* Definición, borrado y ámbito de variables
	* Operadores. Precedencia de operadores
9. [Tipos de datos](curso/u9)
	* Clasificación de tipos de datos
	* Función type()
	* Función isistance()
10. [Trabajando con variables](curso/u10)
	* ¿Qué es el tipado dinámico?
	* Objetos inmutables y mutables
	* Función id()
	* Operadores de identidad
	* Operadores de asignación
	* Asignación múltiple

11. [Entrada y salida estándar](curso/u11)
	* Función input
	* Función print
	* Formateando cadenas de caracteres
	* Función format()

	### Tipos de datos numéricos

12. [Tipo de datos numéricos](curso/u12) 
	* Enteros
	* Reales
	* Complejos
	* Operadores aritmético
	* Funciones predefinidas que trabajan con números: abs(), divmod(), hex() oct(x), pow(), round()
	* Operadores a nivel de bit
	* Conversión de tipos
13. [Tipo de dato booleanos](curso/u13) 
	* Tipo booleano
	* ¿Qué valores se interpretan como FALSO?
	* Operadores booleanos
	* Operadores de comparación
	* Funciones all() y any()

14. [Ejercicios de programas sencillos](curso/u14)

	### Estructuras de control

15. [Estructura de control: Alternativas](curso/u15)
	* Alternativas simples
	* Alternativas dobles
	* Alternativas múltiples
	* Expresión reducida del if 

16. [Ejercicios de alternativas](curso/u16)

17. [Estructura de control: Repetitivas](curso/u17)
	* while
	* for
	* Instrucciones break, continue y pass
	* Recorriendo varias secuencias. Función zip()

18. [Ejercicios de repetitivas](curso/u18)

	### Tipos de datos secuencia

19. [Tipo de datos secuencia](curso/u19)
	* Enumeración de los tipos secuencias
	* Características principales de las secuencias
20. [Tipo de datos secuencia: listas](curso/u20)
	* Construcción de una lista
	* Operaciones básicas con listas
	* Las listas son mutables. ¿Cómo se copian las listas?
	* Listas multidimensionales
	
21. [Métodos principales de listas](curso/u21)
	* Métodos de inserción: append, extend, insert
	* Métodos de eliminación: pop, remove
	* Métodos de ordenación: reverse, sort, 
	* Métodos de búsqueda: count, index
	* Método de copia: copy

22. [Operaciones avanzadas con secuencias](curso/u22)
	* Función map
	* Función filter
	* Función reduce
	* list comprehension

23. [Ejercicios de listas](curso/u23)	

24. [Tipo de datos secuencia: Tuplas](curso/u24)
	* Construcción de una tupla
	* Empaquetado y desempaquetado de tuplas
	* Operaciones básicas con tuplas
	* Las tuplas son inmutables
	* Métodos principales

25. [Tipo de datos secuencia: Rangos](curso/u25)
	* Definición de un rango. Constructor range
	* Recorrido de un rango
	* Operaciones básicas con range

26. [Codificación de caracteres](curso/u26)
	* Introducción a la codificación de caracteres
	* La codificación de caracteres en python3
	* Funciones chr() y ord()

27. [Tipo de datos cadenas de caracteres](curso/u27)
	* Definición de cadenas. Constructor str
	* Operaciones básicas con listas
	* Las cadenas son inmutables
	* Comparación de cadenas
	* Funciones str, repr, ascii, bin

28. [Métodos principales de cadenas](curso/u28)
	* Métodos de formato
	* Métodos de búsqueda
	* Métodos de validación
	* Métodos de sustitución
	* Métodos de unión y división

29. [Ejercicios de cadenas](curso/u29)

30. [Tipo de datos binarios: bytes, bytearray](curso/u30)
	* Definición de bytes. Constructor bytes
	* Definición de bytearray. Constructor bytearray
	* Operaciones básicas con bytes y bytearray
	* Los bytes son inmutables, los bytearray son inmutables
	* Métodos de bytes y bytearray
	* Métodos encode(), decode()
31. [Tipo de datos conjuntos: set, frozenset](curso/u31)
	* Definición de conjuntos. Constructor set
	* Definición de frozenset. Constructor frozenset
	* Operaciones básicas con set y frozenset
	* Los set son inmutables, los frozenset son mutables
	* Métodos principales
32. [Tipo de datos iterador y generador](curso/u32)
	* Iteradores
	* Función next(), reversed()
	* Generadores

 ### Tipos de datos mapas

33. [Tipo de datos mapa: diccionario](curso/u33)
	* Definición de diccionarios. Constructor dict
	* Operaciones básicas con diccionarios
	* Los diccionarios son tipos mutables

34. [Métodos principales de diccionarios](curso/u34)
	* Métodos de eliminación: clear
	* Métodos de agregado y creación: copy, dict.fromkeys, update, setdefault
	* Métodos de retorno: get, has_key, items, keys, values
	* Recorridos de diccionarios
	* dictviews

35. Ejercicios de diccionarios


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


