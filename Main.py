import os
import msvcrt
from busqueda import busqueda
import registro
import busqueda

clsRegistro = registro.registro
clsBusqueda = busqueda.busqueda

def MenuRegistro(self):
    os.system("cls")
    op = 0
    print("_____SUPER TIENDA LA COBANERIA________")
    print("1.Registro")
    print("2.Eliminacion")
    print("3.Edicion")
    print("4.Factura")
    op=int(input("Seleccione opcion: "))
    while True:
        if op == 1:
            op1 = 0 
            print("REGISTRO")
            print("1. Articulos")
            print("2. Proveedores")
            print("3. Empleados")
            print("4. Regresar")
            op1 = int(input("Seleccione opcion"))
            while True:
                    if op1 == 1:
                        clsRegistro.registroArticulo(self) 
                        os.system("cls")
                        break  
                    elif op1 == 2:
                        clsRegistro.registroProveedor(self)
                        os.system("cls")
                        break        
                    elif op1 ==3:
                        clsRegistro.registroEmpleados(self)
                        os.system("cls") 
                        break
                    elif op1 == 4:
                        break             
                        
                   
        elif op == 2:
            op2 = 0 
            print("2.Eliminaciones")
            print("1. Articulos")
            print("2. Proveedores")
            print("3. Empleados")
            print("4. Salirr")
            op2 = int(input("Seleccione opcion"))
            while True:
                if op2 == 1:
                    clsBusqueda.busquedaArticulo(self)
                    os.system("cls")
                elif op2 ==2:
                    clsBusqueda.busquedaProveedor(self)
                    os.system("cls")

                continue        
        elif op ==3:
            op3 ==0 
            print("3.Edicion")     
            print("1. Articulos")
            print("2. Proveedores")
            print("3. Empleados")
            print("4. Salir")
            op3 = int(input("Seleccione opcion"))
            os.system("cls")

            continue

        elif op ==4:
            op ==0 
            print("Factura")
            os.system("cls")
            continue
        elif op==5:
            break    

MenuRegistro(True)