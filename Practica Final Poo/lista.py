from nodo import Nodo
class Lista:
    __cabeza=Nodo
    def __init__(self,obj=None):
        self.__cabeza=obj
    def agregar(self,nodo):
        if self.__cabeza==None:
            self.__cabeza=nodo
        else:
            #INSERTAR AL FINAL
            aux=self.__cabeza
            while aux.get_sig() != None:
                aux=aux.get_sig()
            aux.set_sig(nodo)
            print("Insertado al final correctamente")
    def mostrar(self):
        aux=self.__cabeza
        while aux != None:
            print(aux.mostrar())
            aux=aux.get_sig()
    def nac(self):
        aux=self.__cabeza
        while aux!= None:
            print(aux.tipoN())
            aux=aux.get_sig()
    def buscar(self,num):
        aux=self.__cabeza
        i=0
        while i!= num and aux.get()!=None:
            i=i+1
            aux=aux.get_sig()
        if aux.get()!=None:
            print(aux.tipo())
            print("Se encontro con exito")
        else:
            print("No se pudo encontrar")