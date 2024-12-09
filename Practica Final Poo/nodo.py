from cliente import Cliente
from clienteN import Nacionales
class Nodo:
    __p=object
    def __init__(self,cliente):
        self.__cliente=cliente
        self.__p=None
    def get(self):
        return self.__cliente
    def get_sig(self):
        return self.__p
    def set_sig(self,nodo):
        self.__p=nodo
    def mostrar(self):
        return self.__cliente
    def tipoN(self):
        if isinstance(self.__cliente,Nacionales):
            return self.__cliente
    def tipo(self):
        if isinstance(self.__cliente,Nacionales):
            return f"Cliente Nacional"
        else:
            return  f"Cliente Local"