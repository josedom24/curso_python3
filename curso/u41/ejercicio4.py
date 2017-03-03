#!/usr/bin/env python
import shutil, os

ruta = os.getcwd() + os.sep
origen = ruta + 'origen.txt'
destino = ruta + 'destino.txt'
if os.path.exists(origen):
    try:
        archivo = shutil.copy(origen, destino)
        print('Copiado...', archivo)
    except:
        print('Error en la copia')