import datetime
from Agroalimentaria import agro
class refri(agro):
    __codigo : str

    def __init__(self, nomproducto, fechaenva, fechavenci, temperatura, pais, numlote, costobase, codigo):
        super().__init__(nomproducto,fechaenva, fechavenci, temperatura, pais, numlote, costobase)
        self.__codigo = codigo

    def getcodigo(self) -> str:
        return self.__codigo
    
    def imp_venta(self):
        costo = self.getcostobase()
        if datetime(self.getfechavenci().year()) >= datetime.datetime.now().year:
            if ((self.getfechavenci().month - 2) <= datetime.datetime.now().month): 
                costo = costo - ((costo*10) / 100)
        else:
            costo = costo + ((costo*1) / 100)

        return costo


