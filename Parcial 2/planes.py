from abc import ABC, abstractmethod
class Plan:
    __nombre=str
    __duracion=int
    __cobertura=str
    __precio=float
    def __init__(self,nombre,duracion,cobertura,precio):
        self.__nombre=nombre
        self.__duracion=duracion
        self.__cobertura=cobertura
        self.__precio=precio
    def __str__(self):
        return f"Plan:  {self.__nombre},Duracion{self.__duracion},Cobertura:{self.__cobertura},Precio:{self.calcular()}"
    def getprecio(self):
        return self.__precio
    def getnombre(self):
        return self.__nombre
    def getCobertura(self):
        return self.__cobertura

    @abstractmethod
    def calcular(self):
        pass    
    