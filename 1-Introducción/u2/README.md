# Python2 us Python3
# Notas

## python 2.x y python 3.x

La ultima versión 2.x fue la 2.7 de 2010, contando con soporte hasta el final de su vida útil. No está en desarrollo.
La versión 3.x está bajo desarrollo activo, la última versión 3.6 salió el 23 de diciembre de 2016. Las modificaciones que se han incluido en python 3.x en sintaxis y módulos claves han hecho que no sea compatible con python 2.x.

En el [post: What’s New In Python 3.0](https://docs.python.org/3.0/whatsnew/3.0.html) escrito por Guido van Rossum podemos encontrar los cambios introducidos en la versión 3.x. En la documentación podéis encontrar la página [What’s New in Python](https://docs.python.org/3/whatsnew/index.html) donde podéis estudiar las mejoras de cada una de las versión que van saliendo.

## Entonces, ¿Qué versión debería utilizar? 

Te debes asegurar si las bibliotecas que vas a utilizar son compatibles con la versión que vas a utilizar. El problema en los últimos años ha sido que no todas las librerías se habían exportado a la versión 3. En los últimos tiempo la versión 3 es suficientemente madura para se utilizada y muchos de las librerías y software más utilizado ya está exportado. Puedes ver la lista de los paquetes exportados a la versión 3 en la página [http://python3wos.appspot.com/](http://python3wos.appspot.com/).

Si es totalmente necesario, porque la librería que necesito no está portada tendríamos que usar la versión 2, pero hay que tener en cuenta que python 2.x es un lenguaje antiguo con errores, por lo tanto merece la pena hacer un esfuerzo y buscad alternativas para usar la versión 3. Si tienes código en la antigua versión, también existen herramientas para realizar la portabilidad: [Porting Python Code to 3.x](https://wiki.python.org/moin/PortingPythonToPy3k).

## Las principales difreencia entre python 2.x y 3.x

1. Print es una función en python3
2. Las "cadenas" (strings) son Unicode de forma predeterminada en python 3
3. Generación de listas de número
4. Input es una cadena de texto en python 3
5. Comparando tipos
6. Manejo de excepciones



