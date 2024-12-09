class Edificio:
    def __init__(self,id,nombre,direccion,NomE,CP,CD):
        self.__id=id
        self.__nombre=nombre
        self.__dire=direccion
        self.__NomE=NomE
        self.__CantiP=CP
        self.__CantiD=CD
        self.__departamentos=[]
        
    def cargadepartamento(self,depar):
        self.__departamentos.append(depar)
        