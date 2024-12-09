from GestorEquipos import GestorEquipo
from GestorFechas import GestorFecha

def test():
    gestorequipo=GestorEquipo()
    gestorfecha=GestorFecha()
    gestorequipo.cargaEquipo()
    gestorfecha.cargaFechas()
    c=1
    while c!=0:
        print("0-Para finalizar")
        print("1-Mostrar informacion de un equipo")
        print("2-Actualizar informacion de los equipos")
        print("3-Ordenar tablas ")
        print("4-Almacenar tablas en un archivo")
        opcion=int(input(">>> "))
        if opcion==1:
            equipo=input("Ingrese nombre del equipo: ")
            indice=gestorequipo.buscarequipo(equipo)
            if indice == None:
                print("No encontrado")
            else:
                print("Encontrado")
                gestorfecha.cargaFechas()
                gestorfecha.actualizartablas(indice)
                print("Actualizado")
        if opcion==2:
            for fecha in gestorfecha.getFechapartido():
                for id in gestorequipo.getId():
                    if gestorfecha.getIdlocal()==gestorequipo.getId():
                        golf=gestorequipo.getGolfavor()+gestorfecha.getGollocal()
                        golc=gestorequipo.getGolcontra()+gestorfecha.getGolvisit()
                        gestorequipo.setGolfavor(golf)
                        gestorequipo.setGolcontra(golc)
            print(gestorequipo.__str__)
        if opcion==3:
            gestorequipo.ordenarequipos()
            print(gestorequipo.mostrar)
        if opcion==4:
            print("Archivo creado y cargado")
        if opcion ==0:
            break

if __name__=='__main__':
    test()