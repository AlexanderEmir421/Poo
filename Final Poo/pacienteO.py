from pacientes import Paciente
class PacienteO(Paciente):
    def __init__(self, nombre, apellido, email, numero,historia,alergias,obra):
        super().__init__(nombre, apellido, email, numero)
        self.__historial=historia
        self.__alergias=alergias
        self.__obra_social=obra
    def calculo(self):
        importe=self.get_valor() - 1500
        if self.__obra_social=="Obra Social Provincia":
            importe=importe+5000
        elif self.__obra_social=="OSDE":
            importe=importe+2000
        else:
            importe=importe+10000
        return importe