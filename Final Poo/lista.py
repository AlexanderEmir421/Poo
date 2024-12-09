from nodo import Nodo
from pacientes import Paciente
from pacienteO import PacienteO
from pacienteH import PacienteH
class Lista:
    __cabeza=Nodo
    def __init__(self,obj=None):
        self.__cabeza=obj
    def agregar(self,nodo):
        if self.__cabeza==None:
            self.__cabeza=nodo
        else:
            #INSERTAR AL FINAL
            aux=self.__cabeza
            while aux.get_sig() != None:
                aux=aux.get_sig()
            aux.set_sig(nodo)
            print("Insertado al final correctamente")
    def mostrar(self):
        aux=self.__cabeza
        while aux != None:
            print(aux.mostrar())
            aux=aux.get_sig()
    def pacientesneumonia(self):
        aux=self.__cabeza
        cantiN=0
        cantiA=0
        while aux!= None:
            if isinstance(aux.get(),PacienteH):
                if aux.get_diagnotisco()=="Neumonia":
                    cantiN=cantiN+1
            elif isinstance(aux.get(),PacienteO):
                cantiA=cantiA+1
            aux=aux.get_sig()
        return f"Cantidad de Neumonia:{cantiN},Cantidad de Ambulatorios:{cantiA}"
    def importetotal(self):
        aux=self.__cabeza
        while aux != None:
            print(f"Paciente: {aux.mostrar()} Importe: {aux.get_importe_total()}")
            aux=aux.get_sig()
    def buscar(self,posicion):
        aux=self.__cabeza
        i=0
        while i!=posicion and aux!= None:
            i=i+1
            aux=aux.get_sig()
        if i<=posicion and aux!=None:
            print(f"Paciente en la posicion {posicion} de Tipo: {aux.get_tipo()}")    
        else:
            raise IndexError
    def setiar(self,consulta):
        self.__cabeza.setiar(consulta)