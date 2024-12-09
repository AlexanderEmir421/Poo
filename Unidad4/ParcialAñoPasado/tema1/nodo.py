from inmueble import Inmuebles
class Nodo:
    __inmuebles=Inmuebles
    __siguiente=object
    def __init__(self,inmueble):
        self.__inmuebles=inmueble
        self.__siguiente=None
    def setsiguiente(self,siguiente):
        self.__siguiente=siguiente
    def getSiguiente(self):
        return self.__siguiente
    def mostrar(self):
        return self.__inmuebles
    def numdormitorio(self):
        return self.__inmuebles.getNumdormitorios()
    def listar(self):
        return self.__inmuebles.mostrar()
    def __str__(self):
        return str(self.__inmuebles)