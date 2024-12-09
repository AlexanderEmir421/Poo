from GestorClientes import GestorCliente
from GestorMovimientos import GestorMovimiento

if __name__=="__main__":
    G=GestorCliente()
    M=GestorMovimiento()
    G.Carga()
    M.Carga()
    print("----------------------------------------\n")
    dni=input("Ingrese el Dni de un Cliente: ")
    print("----------------------------------------\n")
    G.Buscar(dni,M)
    print("----------------------------------------\n")
    num=input("Ingrese el Numero de tarjeta: ")
    print("----------------------------------------\n")
    G.BuscarNum(num)
    print("----Movimientos Encontrados----: \n")
    M.getMovimiento(num)
    print("----------------------------------------\n")
    print("Lista ordenada por numero de tarjeta\n ")
    M.Ordenar()
    print("----------------------------------------\n")