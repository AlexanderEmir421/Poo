class Contenedor:
    cuenta = []
    def __init__(self):
        self.__cuenta=[]
    def recolectar(self,ahorro):
        self.__cuenta.append(ahorro)
    def mostrar(self):
        for cuenta in self.__cuenta:
            cuenta.MostrarDatos()
            
            
    