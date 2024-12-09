class fechas:
    __fechapartido=""
    __idlocal=int
    __idvisit=int
    __gollocal=int
    __golvisit=int
    def __init__(self,fechapartido,idlocal,idvisit,gollocal,golvisit,):
        self.__fechapartido=fechapartido
        self.__idlocal=idlocal
        self.__idvisit=idvisit
        self.__gollocal=gollocal
        self.__golvisit=golvisit
    def __str__(self):
        return f'fechapartido:{self.__fechapartido},idlocal:{self.__idlocal},idvisit:{self.__idvisit},gollocal:{self.__gollocal},golvisit:{self.__golvisit}'
    def getFechapartido(self):
        return self.__fechapartido
    def getIdlocal(self):
        return self.__idlocal
    def getIdvisit(self):
        return self.__idvisit
    def getGollocal(self):
        return self.__gollocal
    def getGolvisit(self):
        return self.__golvisit
    def setFechapartido(self,fechapartido):
        self.__fechapartido=fechapartido
    def setIdlocal(self,idlocal):
        self.__idlocal=idlocal
    def setIdvisit(self,idvisit):
        self.__idvisit=idvisit
    def setGollocal(self,gollocal):
        self.__gollocal=gollocal
    def setGolvisit(self,golvisit):
        self.__golvisit=golvisit
