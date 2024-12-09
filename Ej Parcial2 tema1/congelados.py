from Agroalimentaria import agro
class conge(agro):
    __nitro : int
    __oxigeno: int
    __dioxido: int 
    __vapor: int
    __metodo : str

    def __init__(self, nomproducto, fechaenva, fechavenci, temperatura, pais, numlote, costobase, nitro, oxigeno,dioxido,vapor, metodo) :
        super().__init__(nomproducto, fechaenva, fechavenci, temperatura, pais, numlote, costobase)
        self.__nitro = nitro
        self.__oxigeno = oxigeno
        self.__dioxido = dioxido
        self.__vapor = vapor
        self.__metodo = metodo

    def getnitro(self) -> int:
        return self.__nitro
    
    def getoxigeno(self) -> int:
        return self.__oxigeno
    
    def getdioxido(self) -> int:
        return self.__dioxido
    
    def getvapor(self) -> int:
        return self.__vapor
    
    def getmetodo(self) -> str:
        return self.__metodo
    
    def imp_venta(self):
        costo = self.getcostobase
        if self.getmetodo == "mecanico":
            costo = costo + ((costo*15) / 100)
        if self.getmetodo == "criogenico":
            costo = costo + ((costo*10) / 100)

        return costo



