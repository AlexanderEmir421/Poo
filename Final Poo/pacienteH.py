from pacientes import Paciente
class PacienteH(Paciente):
    def __init__(self, nombre, apellido, email, numero,num_habitacion,fecha_ingreso,diagnostico,cant_dias_internado,importe_des):
        super().__init__(nombre, apellido, email, numero)
        self.__numero_habitacion=num_habitacion
        self.__fecha_ingreso=fecha_ingreso
        self.__diagnostico=diagnostico
        self.__cantidad_internado=cant_dias_internado
        self.__importe_descartable=importe_des
    def get_diagnotisco(self):
        return self.__diagnostico
    def calculo(self):
        importe=self.get_valor() + (self.__cantidad_internado*150000) + self.__importe_descartable
        return importe