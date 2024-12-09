from gestorL import GestorL

if __name__=='__main__':
    G=GestorL()
    G.carga()
    print("\n Clientes Nacionales:")
    G.mostrarN()
    G.buscar()