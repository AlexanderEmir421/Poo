class Departamento:
    __Nombre:str
    __NumP:str
    def __init__(self,id,nom,nump,numd,canth,cantb,sup):
        self.__Id=id
        self.__Nombre=nom
        self.__NumP=nump
        self.__NumD=numd
        self.__CantH=canth
        self.__CantB=cantb
        self.__Superficie=sup
    def __str__(self):
        return f"Propetario del Depa {self.__NumD}:N y A: {self.__Nombre}"
    
        