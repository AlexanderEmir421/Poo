from gestor import gestoragro
from refrigerados import refri
from congelados import conge

def menu():
    op=None
    try:
        op=int(input("""
                            Menú De Opciones
                [1] Agregar productos al gestor de productos.
                [2] Dada una posición de la lista: Mostrar qué tipo de producto se encuentra almacenado en dicha posición.
                [3] Mostrar la cantidad de productos de cada tipo.
                [4] Recorrer la colección y mostrar para todos los productos: Nombre, país de origen y temperatura de mantenimiento recomendada, e importe de venta.
                [0] SALIR
                -> """))
    except ValueError:
        pass #No quiero mostrar un print, para eso esta la "validacion" de opciones en el menu
    return op
    
if __name__=="__main__":
    GAgro = gestoragro()
    GAgro.cargar()
    GAgro.muestra_archi()

  
    opcion=menu()
    while opcion!=0:
        if opcion==1:
            tipo=input ("Ingrese tipo de producto : (C/R):")
            NombreProd = input("Ingrese Nombre del producto: ")
            fecha_env=input ("Ingrese fecha de envasado: ")
            fecha_venc=input ("Ingrese fecha de vencimientos: ")
            temp=float (input("Ingrese temperatura: "))
            pais_og=input("Ingrese pais de origen: ")
            nro_lote=int(input("Ingrese nro de lote: "))
            costo_base=float (input("Ingrese costo base: "))
            if (tipo =='R'):
                cod=int(input("Ingrese codigo: "))
                nuevo_prod=refri(NombreProd,fecha_env,fecha_venc,temp,pais_og,nro_lote,costo_base,cod)
                GAgro.agrega_nuevo_prod(nuevo_prod)
                GAgro.muestra_archi()
            elif (tipo =='C'):
                nitro=int(input("Ingrese porcentaje de nitrogeno: "))
                oxi=int(input("Ingrese porcentaje de oxigeno: "))
                diox_car=int (input("Ingrese porcentaje de dioxido: "))
                vap_agua= int(input("Ingrese vapor de agua (porcentaje): "))
                metodo=input("Ingrese metodo de congelacion : ")
                nuevo_prod=conge(NombreProd,fecha_env,fecha_venc,temp,pais_og,nro_lote,costo_base,nitro,oxi,diox_car,vap_agua,metodo)
                GAgro.agrega_nuevo_prod(nuevo_prod)
                GAgro.muestra_archi()
           
        elif opcion==2:
           posi = int(input("Ingrese una posicion para dicho producto: "))
           GAgro.mostrarposi(posi)

        elif opcion==3:
           GAgro.mostrarcantidad()
           
        elif opcion==4:
            GAgro.mostarTodos()
      
            
        opcion=menu()