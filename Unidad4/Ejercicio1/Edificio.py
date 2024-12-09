from os import path
import csv
from Ejercicio1.Departamento import Departamento

class Edificio:
    def __init__(self,id,nom,dir,nomE,cP,cD):
        self.__id=id
        self.__nombre=nom
        self.__direcciom=dir
        self.__nombreEmpresa=nomE
        self.__cantidadPisos=cP
        self.__cantidadDepartamento=cD
        self.__departamentos=[]
    def agregarDepartamento(self,idD,nom,nump,numd,canth,cantb,sup):
        self.__departamentos.append(Departamento(idD,nom,nump,numd,canth,cantb,sup))
    def getNombre(self):
        return self.__nombre
    def getDepartamentos(self):
        for depar in self.__departamentos:
            print(depar)
    
        
        