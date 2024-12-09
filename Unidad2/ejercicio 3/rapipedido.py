class moto:
    __patente=str
    __marca=str
    __nombre=str
    __apellido=str
    __kilometraje=int
    def __init__(self,patente,marca,nombre,apellido,kilometraje):
        self.__patente=patente
        self.__marca=marca
        self.__nombre=nombre
        self.__apellido=apellido
        self.__kilometraje=kilometraje
    def getPatente(self):
        return self.__patente
class pedido:
    patente=int
    identificador=int
    comidas=str
    tiempoEstimado=int
    tiempoEntrega=int
    precio=float
        