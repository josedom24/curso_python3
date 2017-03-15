class Telefono:
    "Clase teléfono"
    def __init__(self,numero):
        self.numero=numero
    def telefonear(self):
        print('llamando')
    def colgar(self):
        print('colgando') 
    def __str__(self):
        return self.numero

class Camara:
    "Clase camara fotográfica"
    def __init__(self,mpx):
        self.mpx=mpx
    def fotografiar(self):
        print('fotografiando')        
    def __str__(self):
        return self.mpx
class Reproductor:
    "Clase Reproductor Mp3"
    def __init__(self,capcidad):
        self.capacidad=capcidad
    def reproducirmp3(self):
        print('reproduciendo mp3')                  
    def reproducirvideo(self):
        print('reproduciendo video')                  
    def __str__(self):
        return self.capacidad

class Movil(Telefono, Camara, Reproductor):
    def __init__(self,numero,mpx,capacidad):
        Telefono.__init__(self,numero)
        Camara.__init__(self,mpx)
        Reproductor.__init__(self,capacidad)
    def __str__(self):
        return "Número: {0}, Cámara: {1},Capacidad: {2}".format(Telefono.__str__(self),Camara.__str__(self),Reproductor.__str__(self))
