class ahorro:
    __nrocuenta=""
    __cuil=""
    __apellido=""
    __nombre=""
    __saldo=float 
    def __init__(self,nrocuenta,cuil,apellido,nombre,saldo):
        self.__nrocuenta=nrocuenta
        self.__cuil=cuil
        self.__apellido=apellido
        self.__nombre=nombre
        self.__saldo=saldo
    def MostrarDatos(self):
        print(self.__nrocuenta  ,self.__cuil,self.__apellido,self.__nombre,self.__saldo)
    def extraerImporte(self,monto):
        
        self.__saldo-=monto
        return self.__saldo
    def Depositar(self,monto):
        if monto > 0 :
            self.__saldo+=monto
        return self.__saldo
    def validarCuil(self,cuil1):
        print("hola")
        
        
                  
        