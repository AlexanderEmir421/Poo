from productos import Productos
import datetime
class Refrigerado(Productos):
    def __init__(self,nombre,fEnvasado,fVencimiento,tempertura,pais,numeroLote,costobase,codOrg):
        super().__init__(nombre,fEnvasado,fVencimiento,tempertura,pais,numeroLote,costobase)
        self.__codOrg=codOrg
    def precio(self):
        fV=datetime.datetime(self.getFechaVencimiento())
        fE=datetime.datetime(self.getFechaEnvasado())
        if(fV-fE <= 2):
            return self.getcosto() + ((self.getcosto() * 10) / 100)
        else:
            return self.getcosto() + ((self.getcosto() * 1) / 100)
    