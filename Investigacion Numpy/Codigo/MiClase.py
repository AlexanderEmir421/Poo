class Persona:
    __edad=int
    __dni=int
    __genero=str
    __nombre=str
    __apellido=str
    def __init__(self,edad,dni,genero,nombre,apellido):
        self.__edad=edad
        self.__dni=dni
        self.__genero=genero
        self.__nombre=nombre
        self.__apellido=apellido
    def mostrar(self):
        print(self.__nombre, self.__apellido)
    def mostrarEdad(self):
        print(self.__edad)
    def mostrarDni(self):
        print(self.__dni)
    def __lt__(self,otraEdad):
        return self.__edad>otraEdad
        