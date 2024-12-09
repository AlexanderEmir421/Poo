from lista import Lista
if __name__=='__main__':
    L=Lista()
    L.cargar()
    L.mostrar()
    print("-------------------------Main-------------------------\n")
    pos=int(input("Ingresa una posicion de la lista:\n"))
    try:
        L.obtenerposicion(pos)
    except IndexError:
        print("\nÍndice fuera de rango")
    
    cober=input("\n Ingresa una cobertura geografica")
    L.contarcober(cober)
    canti=int(input("\n Ingresa una cantidad de canales internacionales: "))
    L.getcompainternacionales(canti)