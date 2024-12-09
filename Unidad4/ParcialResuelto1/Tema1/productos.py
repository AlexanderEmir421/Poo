class Productos:
    def __init__(self,nombre,fEnvasado,fVencimiento,tempertura,pais,numeroLote,costobase):
        self.__nombre=nombre
        self.__fEnvasado=fEnvasado
        self.__fVencimient=fVencimiento
        self.__tempertura=tempertura
        self.__pais=pais
        self.__numeroLote=numeroLote
        self.__costobase=costobase
    def __str__(self):
        return f"Nombre: {self.__nombre},Pais: {self.__pais},temperatura:{self.__tempertura}"
    def precio(self):
        pass
    def getcosto(self):
        return self.__costobase
    def getFechaEnvasado(self):
        return self.__fEnvasado
    def getFechaVencimiento(self):
        return self.__fVencimient