from Infoequipo import equipos
from os import path
import csv

class GestorEquipo:
    def __init__(self):
        self.__equipo=[]
    def cargaEquipo(self):
        archivo=open(path.dirname(__file__)+'/equipos2024.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            equipo=equipos(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5])
            self.__equipo.append(equipo)
    def mostrar(self):
        for i in range(len(self.__equipo)):
            print(self.__equipo[i])
    def buscarequipo(self,equipo):
        indice=0
        valorRetorno=0
        bandera=False
        while not bandera and indice< len(self.__equipo):
            if self.__equipo[indice].getNombre()==equipo:
                bandera=True
                valorRetorno=self.__equipo[indice]
            else:
                indice+=1
        return valorRetorno
    def ordenarequipos(self):
        self.__equipo.sort(reverse=True)
        with open('tablaposiciones.csv', mode='w', newline='') as archivo:
            writer=csv.writer(archivo,delimiter=';')
            writer.writerow(['ID','Nombre','GolFavor','GolContra','Diferencia Goles','Puntos'])
            for equipo in self.__equipo:
                writer.writerow([equipo.getId(),equipo.getNombre(),equipo.getGolfavor(),equipo.getGolcontra(),equipo.getDifgol(),equipo.getPuntos()])


    