class Movimiento:
    __Num=str
    __fecha=str
    __des=str
    __tipoM=str
    __importe=float
    def __init__(self,num,fecha,des,tipo,saldo):
        self.__Num=num
        self.__fecha=fecha
        self.__des=des
        self.__tipoM=tipo
        self.__importe=saldo
    def __str__(self):
        return f"fecha:{self.__fecha} \t\t Descripcion:{self.__des} \t\t Importe :{self.__importe}\t\t Tipo De Movimiento:{self.__tipoM}"
    def getNum(self):
        return self.__Num
    def getTipo(self):
        return self.__tipoM
    def getImporte(self):
        return self.__importe
    def getFecha(self):
        return self.__fecha
    def __lt__(self,otro):
        return self.__Num>otro.__Num
    