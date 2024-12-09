from productos import Productos

class Congelados(Productos):
    def __init__(self,nombre,fEnvasado,fVencimiento,tempertura,pais,numeroLote,costobase,nitro,oxigeno,dioxido,vapor, metodo):
        super().__init__(nombre,fEnvasado,fVencimiento,tempertura,pais,numeroLote,costobase)
        self.__metodo=metodo
        self.__nitrogeno=nitro
        self.__oxigeno=oxigeno
        self.__vapor=vapor
        self.__dioxido=dioxido
    def precio(self):
        if self.__metodo == "mecanico":
            return self.getcosto() + ((self.getcosto()*15)/100)
        elif self.__metodo == "criogenico":
            return self.getcosto() + ((self.getcosto()*15)/100)
        