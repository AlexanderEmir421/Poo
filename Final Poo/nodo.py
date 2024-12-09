from pacienteH import PacienteH
from pacienteO import PacienteO
from pacientes import Paciente
class Nodo:
    __p=object
    def __init__(self,paciente):
        self.__paciente=paciente
        self.__siguiente=None
    def get(self):
        return self.__paciente
    def get_sig(self):
        return self.__siguiente
    def set_sig(self,nodo):
        self.__siguiente=nodo
    def mostrar(self):
        return self.__paciente.mostrar()
    def get_diagnotisco(self):
        return self.__paciente.get_diagnotisco()
    def get_importe_total(self):
        if isinstance(self.__paciente,PacienteH) or isinstance(self.__paciente,PacienteO):
            importe=self.__paciente.calculo()
        else:
            importe=self.__paciente.get_valor()
        return importe
    def get_tipo(self):
        if isinstance(self.__paciente,PacienteO):
            return "Paciente Obra Social"
        elif isinstance(self.__paciente,PacienteH):
            return "Paciente Hospitalario"
        else:
            return "Paciente"
    def setiar(self,consulta):
        Paciente.set_valor(consulta)