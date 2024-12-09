from anucio import Anucio
from anucioA import AnucioA
from anucioAD import AnucioAudioVisual
import csv
from os import path

class Gestor:
    def __init__(self):
        self.__lista=[]
    def generar(self):
        archivo=open(path.dirname(__file__)+ "./anuncios.csv")
        reader=csv.reader(archivo,delimiter=";")
        band=False
        for fila in reader:
            if band == False:
                band=True
            else:
                print(f"Fila{fila[0]}")
                if fila[0]=="AA":
                    self.__lista.append(AnucioA(fila[1],int(fila[2]),fila[3],float(fila[4]),fila[5],fila[6]))
                else:
                    self.__lista.append(AnucioAudioVisual(fila[1],int(fila[2]),fila[3],float(fila[4]),fila[5],int(fila[6])))
    def mostrar(self):
        for i in self.__lista:
            print(i.mostrar())
    def punto2(self):
        titulo=input("Ingrese el titulo:")
        for i in self.__lista:
            if titulo == i.mostrar():        
                if isinstance(i,AnucioA):
                    print(f"Tipo: Audio, {str(i)}")
                else:
                    print(f"Tipo AudioVisual, {str(i)}")
                