
class Paciente:
    __nom=str
    __ap=str
    __email=str
    __numero=int
    __valor=15000
    def __init__(self,nombre,apellido,email,numero):
        self.__nom=nombre
        self.__ap=apellido
        self.__email=email
        self.__numero=numero
    def calculo(self):
        pass
    def mostrar(self):
        return f"{self.__nom} {self.__valor}"
    def get_valor(self):
        return self.__valor
    @classmethod
    def set_valor(cls,consulta):
        cls.__valor=consulta        