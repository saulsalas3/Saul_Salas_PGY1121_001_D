class Asistente:
    rut = ''
    nombre = ''
    apellido= ''
    num_asiento = 0
    valor = 0

    def __init__(self):
        self.rut = '12345678'
        self.nombre = 'elpepe'
        self.apellido = 'etesech'
        self.num_asiento = 100
        self.valor = 120000


    def setRut(self,rut):
        if len(rut) == 8:
            self.rut = rut
            return True
        else:
            print("Rut no valido")
            return False


    def setNombre(self,nombre):
        if len(nombre >=3) and len(nombre) <= 32:
            self.Nombre = nombre
            return True
        else:
            print("Nombre no valido")
            return False


    def setApellido(self,apellido):
        if len(apellido) >=3 and len(apellido) <=32:
            self.apellido = apellido
            return True
        else:
            print("Apellido no valido")
            return False


