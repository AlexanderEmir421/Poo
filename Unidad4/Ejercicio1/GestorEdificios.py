import csv
from os import path
from Ejercicio1.Edificio import Edificio

class Gestor:
    def __init__(self):
        self.__listEdificios=[]
        archivo=open(path.dirname(__file__)+ "./EdificioNorte (2).csv" )
        reader=csv.reader(archivo,delimiter=";")
        k= -1
        for fila in reader:
            print(f"{int(fila[0])} != {k}")
            if int(fila[0]) != k:
                k=int(fila[0])
                print(k)
                self.__listEdificios.append(Edificio(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]),int(fila[5])))
            else:
                print(f"{k} - {1}")
                self.__listEdificios[k-1].agregarDepartamento(int(fila[1]),fila[2],int(fila[3]),int(fila[4]),int(fila[5]),int(fila[6]),float(fila[7]))
    def getEdificio(self,nom):
        i=0
        while i<len(self.__listEdificios) and nom != self.__listEdificios[i].getNombre() :
            i+=1
        if i < len(self.__listEdificios):
            print("Encontro")
            self.__listEdificios[i].getDepartamentos()
        else:
            print("NO SE ENCONTRO ESE EDIFICIO")
    
    def imprime(self):
        for i in self.__listEdificios:
            print("Para el edificio" + i.getNombre())
            print(i.getDepartamentos())