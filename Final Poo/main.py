from gestor import Gestor
if __name__=="__main__":
    G=Gestor()
    G.cargar()
    G.mostrar()
    G.puntob()
    G.puntoc()
    posicion=int(input("\nIngrese una posicion: "))
    G.puntod(posicion)
    consulta=float(input("Ingrese Un nuevo valor de Consulta: "))
    G.puntoe(consulta)
    G.mostrar()