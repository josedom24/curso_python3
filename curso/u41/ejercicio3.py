#!/usr/bin/env python
import shutil, os

ruta = os.getcwd() + os.sep
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'

# Antes:
# -r--r--r-- 1 usuario usuario 84 oct 13 20:33 origen.txt
# -rw-rw-rw- 1 usuario usuario 63 oct 13 21:45 destino.txt

if os.path.exists(origen) and os.path.exists(destino):
    shutil.copystat(origen, destino)
    print("Estado copiado")

# Después:
# -r--r--r-- 1 usuario usuario 84 oct 13 20:33 origen.txt
# -r--r--r-- 1 usuario usuario 63 oct 13 20:33 destino.txt