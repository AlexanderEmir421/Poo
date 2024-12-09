from abc import ABC, abstractmethod
class Anucio(ABC):
    def __init__(self,titulo,duracion,fecha_creacion,costo,formato):
        self.__titulo=titulo
        self.__duracion=duracion
        self.__fecha=fecha_creacion
        self.__costo=costo
        self.__format=formato
    def getformato(self):
        return self.__format
    @abstractmethod
    def get_costo(self):
        pass
    @abstractmethod
    def __str__(self):
        pass
    
    def mostrar(self):
        return self.__titulo