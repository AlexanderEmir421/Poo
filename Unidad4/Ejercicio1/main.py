from Ejercicio1.GestorEdificios import Gestor

if __name__=="__main__":
    G=Gestor()
    print("\n--------------------Menu-------------------\n")
    G.imprime()
    num=int(input("1)Propetarios \n2)Superficie total Edificio\n 3)Superficie total Departamento\n 4)Cantidad de departamentos con 3 dormitorios y mas de un baño\n 6)Cerrar\n"))
    while num > 0 and num < 6:
        if num==1:
            nombre=input("\nIngrese el nombre de un edificio:") 
            G.getEdificio(nombre)      
        elif num==2:
            pass
        elif num==3:
            pass
        elif num==4:
            pass
        else:
            pass
        
        num=int(input("\n 1)Propetarios \n2)Superficie total Edificio\n 3)Superficie total Departamento\n 4)Cantidad de departamentos con 3 dormitorios y mas de un baño\n 6)Cerrar\n"))
    