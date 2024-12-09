from lista import Lista
from casa import Casa
from depar import Departamento

def carga(coleccion):
    Casa1=Casa("Localidad1", "Direccion1", 120, 300)
    Casa2=Casa("Localidad2", "Direccion2", 150, 350)
    Casa3=Casa("Localidad3", "Direccion3", 100, 250)
    Departamento1=Departamento("Localidad1", "Direccion1", 80, 2, 1, 101, 1)
    Departamento2=Departamento("Localidad2", "Direccion2", 90, 3, 2, 202, 2)
    Departamento3=Departamento("Localidad3", "Direccion3", 70, 1, 3, 303, 3)
    coleccion.agregar(Casa1)
    coleccion.agregar(Casa2)
    coleccion.agregar(Casa3)
    coleccion.agregar(Departamento1)
    coleccion.agregar(Departamento2)
    coleccion.agregar(Departamento3)
    
def menu():
    coleccion=Lista()
    carga(coleccion)
    num=int(input("_________________MENU________________\n 1)BUSCAR DORMITORIOS DE DEPAR\n 2)DEPARTAMENTOS UBI\n 3)VERIFICAR IMPORTE VENTA 4)SALIR\t\t"))
    while num<4 and num >0:
        if(num==1):
            num=int(input("\n Ingrese Cantidad de dormitorios: \t"))
            coleccion.dormitorios(num)
        elif(num==2):#RECORRER LISTA
            coleccion.listar()
        elif(num==3):
            pass
        num=int(input("_________________MENU________________\n 1)INSERTAR INMUEBLE\n 2)BUSCAR DORMITORIOS DE DEPAR\n 3)DEPARTAMENTOS UBI\n 4)VERIFICAR IMPORTE VENTA 5)SALIR\t\t"))
if __name__=="__main__":
    menu()
    