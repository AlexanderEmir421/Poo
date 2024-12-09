from Agroalimentaria import agro
from refrigerados import refri
from congelados import conge
import datetime
import csv

class gestoragro:
    __listaAgro : list

    def __init__(self) -> None:
        self.__listaAgro = []
    
    def agregar(self,agro):
        self.__listaAgro.append(agro)

    def cargar(self):
        archivo = open('EJParcial2.tema1/productos.csv')
        reader = csv.reader(archivo, delimiter=';')   
        bandera = False
        for fila in reader:
            if bandera == False:
                bandera = True

            elif (fila[0]== 'C'):
                nomproducto = fila[1]
                fechasplit = fila[2].split('/')
                fechaenva = datetime.datetime(int(fechasplit[2]),int(fechasplit[1]),int(fechasplit[0]))
                fechasplit = fila[3].split('/')
                fechavenci = datetime.datetime(int(fechasplit[2]),int(fechasplit[1]),int(fechasplit[0]))
                temperatura = float(fila[4])
                pais = fila[5]
                numlote = fila[6]
                costobase = int(fila[7])
                nitro = int(fila[8])
                oxigeno = int(fila[9])
                dioxido = int(fila[10])
                vapor = int(fila[11])
                metodo = fila[12]
                xconge = conge(nomproducto, fechaenva, fechavenci, temperatura, pais, numlote, costobase,nitro,oxigeno,dioxido,vapor , metodo)
                self.agregar(xconge)
            elif (fila[0]=='R'):
                nomproducto = fila[1]
                fechaenva = fila[2]
                fechavenci = fila[3]
                temperatura = float(fila[4])
                pais = fila[5]
                numlote = fila[6]
                costobase = int(fila[7])
                codigo = (fila[8])
                xrefri = refri(nomproducto, fechaenva, fechavenci, temperatura, pais, numlote, costobase, codigo)
                self.agregar(xrefri)
        archivo.close()

    def agrega_nuevo_prod (self,nuevo_prod):
        self.__listaAgro.append(nuevo_prod)

    def muestra_archi(self):
        for prod in self.__listaAgro:
            print (prod)

    def mostrarposi(self, posi):
        indice = 0
        while indice < len(self.__listaAgro):
            if indice == posi:
                if isinstance(self.__listaAgro[indice], refri):
                    print("es refrigerados")
                else:
                    print("es congelados")
                    
                indice = len(self.__listaAgro)
                
            else:
                indice = indice + 1

    def mostrarcantidad(self):
        contrefri = 0
        contconge = 0
        for prod in self.__listaAgro:
            if isinstance(prod, refri):
                contrefri = contrefri + 1
            else:
                contconge = contconge + 1
        print("Cantidad de refrigerados: ", contrefri)
        print("Cantidad de congelados: ", contconge)
        print("Cantidad total de productos: ", contrefri + contconge)

    def mostarTodos(self):
        for prod in self.__listaAgro:
            if isinstance (prod,refri) or isinstance (prod,conge):
                print (f"Nombre : {prod.getnomproducto()} Pais de Origen : {prod.getpais()} Temperatura Recomendada: {prod.gettemperatura()} Importe de Venta: {prod.imp_venta()}")


    




    
                         

    


