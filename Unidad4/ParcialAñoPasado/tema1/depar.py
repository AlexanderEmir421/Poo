from inmueble import Inmuebles
class Departamento(Inmuebles):
    def __init__(self,localidad,direccion,superficie,cantiDor,numMono,numDepa,piso):
        super().__init__(localidad,direccion,superficie)
        self.__cantiDor=cantiDor
        self.__numMono=numMono
        self.__numDepa=numDepa
        self.__piso=piso
    def precioConstruction(self):
        return self.__cantiDor*17000
    def getNumdormitorios(self):
        return self.__cantiDor
    def mostrar(self):
        return f"\tDireccion: {super().get_direccion()},\tSuperifice:{super().get_superficie()},\tPrecio Venta:{super().calcular()}\n"
    def __str__(self):
        return f"\nLocalidad: {super().get_localidad()},\tDireccion: {super().get_direccion()},\tSuperficie: {super().get_superficie()},\tCantidad de dormitorios: {self.__cantiDor},\tNumero Monoblock: {self.__numMono},\tNumero Departamento: {self.__numDepa},\tPiso: {self.__piso},\tPrecio: {super().calcular()}"