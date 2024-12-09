from MiClase import Persona
import numpy as np



if __name__=='__main__':
    arreglo=np.empty(4,dtype=object)
    objeto1=Persona(10,2214124,"F","Rosa","Gimenez")
    objeto2=Persona(21,4214214,"M","Manuel","Ortega")
    objeto3=Persona(18,42564214,"M","Miguel","Florentino")
    objeto4=Persona(30,66234124,"F","Flor","Naranja")
    arreglo[0]=objeto1
    arreglo[1]=objeto2
    arreglo[2]=objeto3
    arreglo[3]=objeto4
    print("Arreglo Edades:")
    for x in arreglo:
        x.mostrarEdad()
    arreglordenado=np.sort(arreglo)
    print("Arreglo Ordenado por edad:")
    for x in arreglordenado:
        x.mostrarEdad()