class equipos:
    __id=""
    __nombre=""
    __golfavor=int
    __golcontra=int
    __difgol=int
    __puntos=int
    def __init__(self,id,nombre,golfavor,golcontra,difgol,puntos):
        self.__id=id
        self.__nombre=nombre
        self.__golfavor=golfavor
        self.__golcontra=golcontra
        self.__difgol=difgol
        self.__puntos=puntos
    def __str__(self):
        return f'id:{self.__id},nombre:{self.__nombre},golfavor:{self.__golfavor},golcontra:{self.__golcontra},difgol:{self.__difgol},puntos:{self.__puntos}'
    def getId(self):
        return(self.__id)
    def getNombre(self):
        return(self.__nombre)
    def getGolfavor(self):
        return(self.__golfavor)
    def getGolcontra(self):
        return(self.__golcontra)
    def getDifgol(self):
        return(self.__difgol)
    def getPuntos(self):
        return(self.__puntos)
    def setId(self,id):
        self.__id=id
    def setNombre(self,nombre):
        self.__nombre=nombre
    def setGolfavor(self,golfavor):
        self.__golfavor=golfavor
    def setGolcontra(self,golcontra):
        self.__golcontra=golcontra
    def setDifgol(self,difgol):
        self.__difgol=difgol
    def setPuntos(self,puntos):
        self.__puntos=puntos
    def __gt__(self,otro_equipo):
        if self.getPuntos()!=otro_equipo.getPuntos():
            return self.getPuntos()>otro_equipo.getPuntos()
        elif self.getDifgol()!=otro_equipo.getDifgol():
            return self.getDifgol()>otro_equipo.getDifgol()
        elif self.getGolfavor()!=otro_equipo.getGolfavor():
            return self.getGolfavor()>otro_equipo.getGolfavor()