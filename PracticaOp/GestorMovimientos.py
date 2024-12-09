from Movimientos import Movimiento
from os import path
import csv
class GestorMovimiento:
    def __init__(self):
        self.__list=[]
    def Carga(self):
        archivo=open(path.dirname(__file__) + './MovimientosAbril2024.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            M=Movimiento(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
            self.__list.append(M)
            
        archivo.close()
        
    def Actualizar(self,num,saldo):
        for i in self.__list:
            if i.getNum()==num:
                print(i)
                if i.getTipo()=="C":
                    saldo += i.getImporte()
                else: 
                    saldo -= i.getImporte()
        return saldo
    def getMovimiento(self,num):
        for i in self.__list:
            if i.getNum()==num:        
                if i.getTipo()=="P" or i.getTipo()=="C":
                    print(i)
    def Ordenar(self):
        self.__list.sort()
        for i in self.__list:
            print(i.getNum(),i.getImporte(),i.getFecha(),i.getTipo())