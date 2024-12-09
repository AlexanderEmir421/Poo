from cliente import Cliente
from clienteN import Nacionales
from lista import Lista
from nodo import Nodo
class GestorL:
    
    def __init__(self,lista=Lista()):
        self.__lista=lista
    def carga(self):
        i=1
        while i!=0:
            seleccion=input("\n-------Seleccione------\n1)Cliente Local\n2)Cliente Nacional")
            if seleccion=="1":
                self.__lista.agregar(Nodo(Cliente(input("\n Ingrese Nombre:"),input("\n Apellido:"),input("\n Contra:"),input("\n Direccion:"),input("\n email:"),input("\n telefono:"))))
            elif seleccion=="2":
                self.__lista.agregar(Nodo(Nacionales(input("\n Ingrese Nombre:"),input("\n Apellido:"),input("\n Contra:"),input("\n Direccion:"),input("\n email:"),input("\n telefono:"),input("\nProvincia:"),input("\nLocalidad:"),int(input("\nCodigo:")))))
            elif seleccion=="":
                i=0
            
            
                #
                #cliente = Cliente(nom)
                #nodo = Nodo(cliente)
                #self.__lista.agregar(nodo)
    def mostrarN(self):
        self.__lista.nac()
    def mostrartodo(self):
        self.__lista.mostrar()
    def buscar(self):
        num=int(input("Ingrese la posicion que deseas buscar: "))
        while num!=0:
            self.__lista.buscar(num)
            num=int(input("Ingrese la posicion que deseas buscar: "))
            
            
            
            