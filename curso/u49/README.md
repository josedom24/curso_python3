# Programación estructurada y modular: Ejemplo completo

Partiendo del fichero csv `liga.csv` con los resultados de las jornadas de liga 2015-2016, realizar un programa que muestre la tabla de clasificación al final de la liga, en el que debe aparece el orden que ha quedado cada equipo, los partidos ganados, los empatados y perdidos, y por último los puntos conseguidos.

Para realizar este programa vamos a construir varias funciones:

* `LeerPartidos()`: Función que lee el fichero CSV y devuelve los datos del mismo en una lista de diccionarios.
* `impClasificacion(liga)`:Recibe la lista de diccionarios generado a parir de la función anterior, genera los datos de la clasificación y los imprime por pantalla.

Esta función utiliza interna las siguinetes funciones:

* `Equipos(datosliga)`: Función que recibe la lista de diccionarios con los datos de la liga y devuelve un conjunto con los equipos de la liga.
* `InfoEquipos(datosliga,equipos)`: Función que recibe la lista de diccionarios con los datos de la liga y el conjunto de equipos y devuelve una lista de tuplas, en cada tupla se guarda un equipo con los partidos ganados, empatados y perdidos y los puntos obtenidos.

	Esta función utiliza internamente:

	* `QuienGana(resultado)`: Función que recibe un resultado y devuelve un 0 si es un empate, un 1 si gana el equipo de casa y -1 si gana el equipo visitante.
	* `Puntos(info)`: Función que recibe una lista con los partidos ganados, empatados y perdidos y devuelve los puntos obtenidos.

* `Clasificacion(datos)`: Recibe la lista generada con la función anterior y la ordena según el número de puntos.
