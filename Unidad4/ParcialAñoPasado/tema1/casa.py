from inmueble import Inmuebles
class Casa(Inmuebles):
    def __init__(self,localidad,direccion,superficie,metros):
        self.__metros=metros
        super().__init__(localidad,direccion,superficie)
    def precioConstruction(self):
        return self.__metros*1.80*20000