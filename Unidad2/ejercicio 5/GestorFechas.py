from Infofechas import fechas
from os import path
import csv

class GestorFecha:
    def __init__(self):
        self.__fecha=[]
    def cargaFechas(self):
        archivo=open(path.dirname(__file__)+'/fechasFutbol.csv')
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            fecha=fechas(fila[0],fila[1],fila[2],fila[3],fila[4])
            self.__fecha.append(fecha)
    def mostrarFechas(self):
        for i in range(len(self.__fecha)):
            print(self.__fecha[i])
    def actualizartablas(self,indice):
        gf=gc=gd=p=0
        print("---------------------------------------------------------------------------")
        print("Equipo: ",indice.getNombre())
        print("Fecha\tGoles a favor\tGoles en contra\tDiferencia de goles\tPuntos")
        for fechaPartido in self.__fecha :
            if indice.getId()==fechaPartido.getIdlocal() or indice.getId()==fechaPartido.getIdvisit():
                    print(fechaPartido.getFechapartido(),"\t\t",fechaPartido.getGollocal(),"\t\t",fechaPartido.getGolvisit(),"\t\t",int(fechaPartido.getGollocal())-int(fechaPartido.getGolvisit()),"\t",indice.getPuntos())
                    gf+=int(fechaPartido.getGollocal())
                    gc+=int(fechaPartido.getGolvisit())
                    gd+=(int(fechaPartido.getGollocal())-int(fechaPartido.getGolvisit()))
                    if fechaPartido.getGollocal()==fechaPartido.getGolvisit():
                        p+=1
                    if fechaPartido.getGollocal()<fechaPartido.getGolvisit():
                            p+=0
                    else:
                            p+=3
        print("---------------------------------------------------------------------------")
        print("Total\t\t",gf,"\t\t",gc,"\t\t",gd,"\t\t",p)