import numpy as np
from MiClase import Persona


if __name__=='__main__':
    arreglo = np.empty(3, dtype=object)
    for i in range(3):
        edad=int(input("Edad:"))
        dni=int(input("Dni:"))
        genero=input("Genero: M o F")
        nombre=input("Nombre:")
        apellido=input("Apellido:")
        Objeto=Persona(edad,dni,genero,nombre,apellido)
        arreglo[i]=Objeto
    
    for x in arreglo:
        x.mostrar()