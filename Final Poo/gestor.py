from pacientes import Paciente
from pacienteO import PacienteO
from pacienteH import PacienteH
from lista import Lista
from nodo import Nodo
import csv
from os import path
class Gestor:
    def __init__(self):
        self.__lista=Lista()
    def cargar(self):
        archivo=open(path.dirname(__file__)+ "./pacientes.csv")
        reader=csv.reader(archivo,delimiter=";")
        band=False
        for fila in reader:
            if band==False:
                band=True
            else:
                print(f"Fila{fila[0]}")
                if fila[0]=="P":
                    paciente=Nodo(Paciente(fila[1],fila[2],fila[3],int(fila[4])))
                elif fila[0]=="O":
                    paciente=Nodo(PacienteO(fila[1],fila[2],fila[3],int(fila[4]),fila[5],fila[6],fila[7]))
                elif fila[0]=="H":
                    paciente=Nodo(PacienteH(fila[1],fila[2],fila[3],int(fila[4]),int(fila[5]),fila[6],fila[7],int(fila[8]),float(fila[9])))
                self.__lista.agregar(paciente)
    def mostrar(self):
        self.__lista.mostrar()
    def puntob(self):
        print(self.__lista.pacientesneumonia())
    def puntoc(self):
        self.__lista.importetotal()
    def puntod(self,posicion):
        try:
            self.__lista.buscar(posicion)
        except IndexError:
            print("Posicion Fuera de rango")
    def puntoe(self,consulta):
        self.__lista.setiar(consulta)