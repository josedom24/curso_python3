#!/usr/bin/env python
import shutil, os, stat

# Antes:
# -r--r--r-- 1 usuario usuario origen.txt
# -rw-rw-r-- 1 usuario usuario destino.txt

ruta = os.getcwd() + os.sep
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'
if os.path.exists(origen) and os.path.exists(destino):
    print('Antes  :', oct(stat.S_IMODE(os.stat(destino).st_mode)))
    shutil.copymode(origen, destino)
    print('Después:', oct(stat.S_IMODE(os.stat(destino).st_mode)))

# Después:
# -r--r--r-- 1 usuario usuario origen.txt
# -r--r--r-- 1 usuario usuario destino.txt