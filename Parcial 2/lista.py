from nodo import Nodo
from planes import Plan
from telefonia import Telefonia
from television import Television
from os import path
import csv

class Lista:
    __comienzo=Nodo

    def __init__(self):
        self.__comienzo=None
   
    def cargar(self):
        archivo = open(path.dirname(__file__) + './planes.csv')
        reader = csv.reader(archivo, delimiter=";")
        for fila in reader:
            if fila[0] == "T":
                plan=Television(fila[1],int(fila[2]),fila[3],float(fila[4]),int(fila[5]),int(fila[6]))
            else:
                plan=Telefonia(fila[1],int(fila[2]),fila[3],float(fila[4]),fila[5],int(fila[6]))
            self.agregaralfinal(plan)

  
    def agregaralfinal(self,plan):
        nuevo_nodo=Nodo(plan)
        if self.__comienzo is None:
            self.__comienzo = nuevo_nodo
        else:
            actual = self.__comienzo
            while actual.getsiguiente() is not None:
                actual = actual.getsiguiente()
            actual.setsiguiente(nuevo_nodo)
    
    def mostrar(self):
        aux=self.__comienzo
        while aux != None:
            print(aux.getobjeto())
            aux=aux.getsiguiente()
            
                   
    def obtenerposicion(self,pos):
        i=1
        aux=self.__comienzo
        while aux != None:
            if i==pos:
                if(isinstance(aux.getobjeto(),Telefonia)):
                    print(f'Posicion:{pos}Telefonia: Se encuentra plan de telefonia')
                elif(isinstance(aux.getobjeto(),Television)):
                    print(f'Posicion:{pos}Television: Se encuentra plan de televisión')
                return
            aux=aux.getsiguiente()
            i+=1
        raise IndexError 
    def contarcober(self,cober):
        aux=self.__comienzo
        contar=0
        while(aux == None):
            if(aux.getcobetura()== cober):
                contar+=1  
            aux=aux.getsiguiente()
              
        print(f"canti cobertura: {contar}")
    def getcompainternacionales(self,canti):
        aux=self.__comienzo
        print(f"\n EMPRESAS QUE OFRECEN UNA CANTIDAD MAYOR A { canti } DE CANALES INTERNACIONALES")
        while aux != None:
            if(isinstance(aux.getobjeto(),Television)):
                if(aux.getcanales()>=canti):
                    print(f"{aux.getNombre()}\t")
            aux=aux.getsiguiente()
            
    def calculatodo(self):
        aux=self.__comienzo
        while aux != None:
            print(aux.mostrarobjeto())
            aux=aux.getsiguiente()
        
        