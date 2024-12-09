from os import path
import csv
from Edificio import Edificio
from Departamento import Departamento
class GestorEdificio:
    def __init__(self):
        self.__list=[]

    def cargaArchivo(self):
        archivo=open(path.dirname(__file__)+"./EdificioNorte.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            a=-1
            if fila[0]==a:
                D=Departamento(a,fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
                E.cargadepartamento(D)
            else: 
                a=fila[0]
                E=Edificio(a,fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8])
                
                    
        