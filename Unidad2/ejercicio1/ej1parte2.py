from ej2 import Contenedor
from Ej1 import ahorro
def test():
    cuentabancaria=Contenedor()
    for i in range(2):
        Nro=input("Ingrese Numero ")
        cuil=input("Ingrese Cuil ")
        nombre=input("Ingrese Nombre ")
        apellido=input("Ingrese Apellido ")
        saldo=float(input("Ingrese saldo "))
        nuevo=ahorro(Nro,cuil,apellido,nombre,saldo)
        cuentabancaria.recolectar(nuevo)
    cuentabancaria.mostrar()  
if __name__=="__main__":
    test()
    
    
    
