from rapipedido import moto
import csv
from os import path
import numpy as np

class GestorMotos:
    def __init__(self):
        self.lista=[]
    def cargar(self):
        archivo=open(path.dirname(__file__) + './datosMotos.csv')
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            motos=moto(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.lista.append(motos)
                  
    def mostrar(self):
        for i in self.lista:
            print(i.getPatente())
    def buscarM(self,patenteM):
       encontrar=False
       for i in self.lista:
           if(i.getPatente()==patenteM):
               encontrar=True
       if(encontrar==False):
            print("No se encontro la moto")
       else:
            print("Se encontro la moto")           