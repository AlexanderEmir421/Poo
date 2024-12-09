from nodo import Nodo
from depar import Departamento
class Lista:
    __cabeza=Nodo
    def __init__(self):
        self.__cabeza=None
    def agregar(self,inmueble):
        nodo=Nodo(inmueble)
        if self.__cabeza is None:
            nodo.setsiguiente(self.__cabeza)
            self.__cabeza=nodo
        else:
            aux=self.__cabeza
            while aux.getSiguiente() != None:
                aux=aux.getSiguiente()
            aux.setsiguiente(nodo)
    def dormitorios(self,num):
        aux=self.__cabeza
        while aux is not None:
            if  isinstance(aux.mostrar(),Departamento):
                if num >= aux.numdormitorio():
                    print("\n")
                    print(aux) 
            aux=aux.getSiguiente()
    def listar(self):
        aux=self.__cabeza
        while aux is not None:
            if  isinstance(aux.mostrar(),Departamento):
                print(aux.listar())
            aux=aux.getSiguiente()
        
        
        