from planes import Plan

class Telefonia(Plan):
    def __init__(self,nombre,duracion,cobertura,precio,tipollamadas,min):
        super().__init__(nombre,duracion,cobertura,precio)
        self.__tipollamadas=tipollamadas
        self.__min=min
    def calcular(self):
        if self.__tipollamadas == "internacional":
            return self.getprecio()+ ((self.getprecio()*20)/100)
        elif self.__tipollamadas == "Locales":
            return self.getprecio()- ((self.getprecio()* 7.5 )/100)
        