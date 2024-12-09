class Inmuebles:
    def __init__(self,localidad,direccion,superficie):
        self.__localidad=localidad
        self.__direccion=direccion
        self.__superficie=superficie
    def calcular(self):
        return self.__superficie*15*self.precioConstruction()
    def precioConstruction(self):
        pass
    def get_localidad(self):
        return self.__localidad
    def get_direccion(self):
        return self.__direccion
    def get_superficie(self):
        return self.__superficie
    
    