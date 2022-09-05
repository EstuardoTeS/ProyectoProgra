from importlib import import_module
import msvcrt
import os
import pickle
from xmlrpc.client import boolean
import articulos as registroA
import proveedores as registroP
import empleados as registroE

lstProveedor = []
lstArticulo = []
lstEmpleados = []

class busqueda:
    def busquedaArticulo(self):
        global lstArticulo
        archivoArticulo = open("articulos.pkl", "ab+")
        archivoArticulo.seek(0)
        try:
            lstArticulo = pickle.load(archivoArticulo)
            print("-------------------------------------------")
            print(f"-Se cargaron {len(lstArticulo)} artículos.")
        except EOFError:
            print("No existen artículos registados.")
        finally:
            archivoArticulo.close()

        
        
        print("___________ SUPER TIENDA LA COBANERITA ___________")
        print("___________    ELIMINACION DE ARTICULOS  ___________")
        print("")
        codArticulo = int(input("Ingrese el Codigo del Articulo"))
        repetido = False
        contador = 0
        for articulo in lstArticulo:
            if (articulo.getCodArt() == codArticulo):
                repetido = True
                continue  
        contador += 1    
        if repetido == True:
            lstArticulo.pop(contador)
            print("El codigo a sido encontrado y Eliminado ") 
            #Almacenar Articulo de vuelta
            archivoArticulo = open("articulos.pkl", "wb+")
            pickle.dump(lstArticulo, archivoArticulo)
            archivoArticulo.close()
            print("Registro Correctamente")
            print("presione enter para regresar")  
        else:
            print("El codigo no a sido encontrado")
            

    msvcrt.getch()    
    
    def busquedaProveedor(self):
            global lstArticulo
            archivoArticulo = open("articulos.pkl", "ab+")
            archivoArticulo.seek(0)
            try:
                lstArticulo = pickle.load(archivoArticulo)
                print("-------------------------------------------")
                print(f"-Se cargaron {len(lstArticulo)} artículos.")
            except EOFError:
                print("No existen artículos registados.")
            finally:
                archivoArticulo.close()

            global lstProveedor
            archivoProveedor = open("proveedores.pkl", "ab+")
            archivoProveedor.seek(0)
            try:
                lstProveedor = pickle.load(archivoProveedor)
                print("-------------------------------------------")
                print(f"-Se cargaron {len(lstProveedor)} artículos.")
            except EOFError:
                print("No existen artículos registados.")
            finally:
                archivoProveedor.close()


            print("___________ SUPER TIENDA LA COBANERITA ___________")
            print("___________    ELIMINACION DE Proveedores  ___________")
            print("")
            codProveedor = int(input("Ingrese el Codigo del Proveedor"))
            repetido = False
            contador = 0
            for proveedor in lstProveedor:
                if (proveedor.getCodProv() == codProveedor):
                    repetido = True
                    continue  
            contador += 1    
            
            if repetido == True:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                respuesta = int(input("Al eliminar este proveedor eliminara varios articulos \n esta seguro de realizar esta accion...\n 1. Si \n 2. No"))
                if respuesta == 1:
                    print("Proveedor eliminado")
                elif respuesta == 2:
                    print("No se a eliminado ningun proveedor")     
            else:
                print("El codigo no a sido encontrado")
    msvcrt.getch()    
        

                
                     