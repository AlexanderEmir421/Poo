import datetime
from abc import ABC, abstractmethod

class agro(ABC):
    __nomproducto: str
    __fechaenva: datetime
    __fechavenci: datetime
    __temperatura: float
    __pais: str
    __numlote:str
    __costobase: int
    
    def __init__(self, namproducto, fechaenva, fechavenci, temperatura, pais, numlote, costobase):
        self.__nomproducto = namproducto
        self.__fechaenva = fechaenva
        self.__fechavenci = fechavenci
        self.__temperatura = temperatura
        self.__pais = pais
        self.__numlote = numlote
        self.__costobase = costobase


    def getnomproducto(self) -> str:
        return self.__nomproducto
    
    def getfechaenva(self) -> datetime:
        return self.__fechaenva
    
    def getfechavenci(self) -> datetime:
        return self.__fechavenci
    
    def gettemperatura(self) -> float:
        return self.__temperatura
    
    def getpais(self) -> str:
        return self.__pais
    
    def getnumlote(self) -> str:
        return self.__numlote
    
    def getcostobase(self) -> int:
        return self.__costobase
    
    @abstractmethod
    def imp_venta(self):
        pass