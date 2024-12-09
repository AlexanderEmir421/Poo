from anucio import Anucio

class AnucioAudioVisual(Anucio):
    def __init__(self, titulo, duracion, fecha_creacion, costo, formato,resolucion):
        super().__init__(titulo, duracion, fecha_creacion, costo, formato)
        self.__resolucion=resolucion
    def get_costo(self):
        if self.__resolucion == "1440p":
            porce=(self.__costo * 1.5)/100
        elif self.__resolucion == "1080p":
            porce=(self.__costo * 0.5)/100
        else:
            porce=0
        total= (self.__costo * self.__duracion)+porce
        return total
    def __str__(self):
        return f"Formato:{self.__format},Resoluciom:{self.__resolucion}"