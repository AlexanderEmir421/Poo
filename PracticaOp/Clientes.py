class Cliente:
    __nombre=str
    __apellido=str
    __dni=str
    __Num=str
    __saldoA=float
    def __init__(self,nombre,apellido,dni,num,saldoA):
        self.__nombre=nombre
        self.__apellido=apellido
        self.__dni=dni
        self.__Num=num
        self.__saldoA=saldoA
    def __str__(self):
        return f"Cliente:{self.__nombre} {self.__apellido}\t\t Numero de Tarjeta:{self.__Num}\n Saldo Anterior:{self.__saldoA}"
    def getDni(self):
        return self.__dni
    def getNyA(self):
        print(f"Nombre:{self.__nombre} Apellido:{self.__apellido}")
    def getNum(self):
        return self.__Num
    def getSaldo(self):
        return self.__saldoA
    def newSaldo(self,a):
        self.__saldoA=a
        print(self.__saldoA)