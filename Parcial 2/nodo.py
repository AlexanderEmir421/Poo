from planes import Plan
class Nodo:
    __objeto=Plan
    __siguiente=object
    def __init__(self,plan):
        self.__objeto=plan
        self.__siguiente=None
    def getobjeto(self):
        return self.__objeto
    def getsiguiente(self):
        return self.__siguiente
    def setsiguiente(self,siguiente):
        self.__siguiente = siguiente
    def getcobetura(self):
        return self.__objeto.getCobertura()
    def getcanales(self):
        return self.__objeto.getCanales()
    def getNombre(self):
        return self.__objeto.getnombre()
    def mostrarobjeto(self):
        return self.__objeto()