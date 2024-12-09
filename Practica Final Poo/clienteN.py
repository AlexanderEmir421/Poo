from cliente import Cliente

class Nacionales(Cliente):
    def __init__(self, nom, ap, email, contra, dir, tel,prov,loca,cod):
        super().__init__(nom, ap, email, contra, dir, tel)
        self.__prov=prov
        self.__loca=loca
        self.__cod=cod
    def __str__(self):
        return f"{super().__str__()} Provincia: {self.__prov}"