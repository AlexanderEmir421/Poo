from planes import Plan

class Television(Plan):
    def __init__(self,nombre,duracion,cobertura,precio,CanalesN,CanalesI):
        super().__init__(nombre,duracion,cobertura,precio)
        self.__CanalesN=CanalesN
        self.__CanalesI=CanalesI
    def calcular(self):
        if self.__CanalesI>10:
            return self.getprecio()+ ((self.getprecio()*15)/100)
        else:
            return self.getprecio()
    def getCanales(self):
        return self.__CanalesI    
        