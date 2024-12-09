from productos import Productos
from congelados import Congelados
from refrigerados import Refrigerado
from os import path
import csv



class Gestor:
    def __init__(self):
        self.__list=[]
    def carga(self):
        archivo=open(path.dirname(__file__)+"./productos.csv")
        reader=csv.reader(archivo,delimiter=";")
        for fila in reader:
            if fila[0] == "C":
                self.__list.append(Congelados(fila[1],fila[2],fila[3],float(fila[4]),fila[5],fila[6],float(fila[7]),float(fila[8]),float(fila[9]),float(fila[10]),float(fila[11]),fila[12]))
            else:
                self.__list.append(Refrigerado(fila[1],fila[2],fila[3],float(fila[4]),fila[5],fila[6],float(fila[7]),fila[8]))
    def mostrar(self):
        for i in self.__list:
            print (f"({i} ,Precio : {i.precio()}")
            