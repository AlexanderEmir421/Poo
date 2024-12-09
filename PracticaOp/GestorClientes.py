from GestorMovimientos import GestorMovimiento
from Clientes import Cliente
from os import path
import csv
class GestorCliente:
    def __init__(self):
        self.__list=[]
    def Carga(self):
        archivo=open(path.dirname(__file__) + './ClientesAbril2024.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            C=Cliente(fila[0],fila[1],fila[2],fila[3],float(fila[4]))
            self.__list.append(C)
            
        archivo.close()
    def Mostrar(self):
        for i in self.__list:
            print(i)
    def Buscar(self,dni,M):
        e=False
        for i in self.__list:
            if i.getDni()==dni:
                print(i)
                e=True
                sal=M.Actualizar(i.getNum(),i.getSaldo())
                i.newSaldo(sal)
        if e==False:
            print("No se encontro el DNi")
    def ActualizarSaldo(self,saldo,dni):
          for i in self.__list:
            if i.getDni()==dni:
                  i.newSaldo(saldo)
    
    def BuscarNum(self,num):
        for i in self.__list:
            if i.getNum()==num:
                i.getNyA()