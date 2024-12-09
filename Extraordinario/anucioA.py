from anucio import Anucio
class AnucioA(Anucio):
    def __init__(self, titulo, duracion, fecha_creacion, costo, formato,canal):
        super().__init__(titulo, duracion, fecha_creacion, costo, formato)
        self.__canal=canal
    def get_costo(self):
        if self.__canal == "surround":
            porce=(self.__costo * 0.5)/100
        elif self.__canal =="mono":
            porce=(self.__costo * 0.5)/100
        else:
            porce=0
        total= (self.__costo * self.__duracion)+porce
        return total
    def __str__(self):
        return f"Formato:{self.getformato()},Canal:{self.__canal}"