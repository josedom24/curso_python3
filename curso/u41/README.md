## Módulos estándares: módulos de sistema

Python tiene sus propios módulos, los cuales forman parte de su librería de módulos estándar, que también pueden ser importados. En esta unidad vamos a estudiar las funciones porincipales de módulos realacionados con el sistema operativo.

## Módulo os

El módulo [os](https://docs.python.org/3.4/library/os.html#module-os) nos permite acceder a funcionalidades dependientes del Sistema Operativo. Sobre todo, aquellas que nos refieren información sobre el entorno del mismo y nos permiten manipular la estructura de directorios.

   <table>
<thead>
<tr>
  <th>Descripción</th>
  <th>Método</th>
</tr>
</thead>
<tbody>
<tr>
  <td>Saber si se puede acceder a un archivo o directorio</td>
  <td><code>os.access(path, modo_de_acceso)</code></td>
</tr>
<tr>
  <td>Conocer el directorio actual</td>
  <td><code>os.getcwd()</code></td>
</tr>
<tr>
  <td>Cambiar de directorio de trabajo</td>
  <td><code>os.chdir(nuevo_path)</code></td>
</tr>
<tr>
  <td>Cambiar al directorio de trabajo raíz</td>
  <td><code>os.chroot()</code></td>
</tr>
<tr>
  <td>Cambiar los permisos de un archivo o directorio</td>
  <td><code>os.chmod(path, permisos)</code></td>
</tr>
<tr>
  <td>Cambiar el propietario de un archivo o directorio</td>
  <td><code>os.chown(path, permisos)</code></td>
</tr>
<tr>
  <td>Crear un directorio</td>
  <td><code>os.mkdir(path[, modo])</code></td>
</tr>
<tr>
  <td>Crear directorios recursivamente</td>
  <td><code>os.mkdirs(path[, modo])</code></td>
</tr>
<tr>
  <td>Eliminar un archivo</td>
  <td><code>os.remove(path)</code></td>
</tr>
<tr>
  <td>Eliminar un directorio</td>
  <td><code>os.rmdir(path)</code></td>
</tr>
<tr>
  <td>Eliminar directorios recursivamente</td>
  <td><code>os.removedirs(path)</code></td>
</tr>
<tr>
  <td>Renombrar un archivo</td>
  <td><code>os.rename(actual, nuevo)</code></td>
</tr>
<tr>
  <td>Crear un enlace simbólico</td>
  <td><code>os.symlink(path, nombre_destino)</code></td>
</tr>
</tbody>
</table>

	>>> import os
	>>> os.getcwd()
	'/home/jose/github/curso_python3/curso/u40'
	>>> os.chdir("..")
	>>> os.getcwd()
	'/home/jose/github/curso_python3/curso'


