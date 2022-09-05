import msvcrt
import os
import pickle
import articulos as registroA
import proveedores as registroP
import empleados as registroE
import clientes as registroC

lstProveedor = []
lstArticulo = []
lstEmpleados = []
lstClientes = []
lstFacturas = []

class busqueda:
    
    def modeloFactura(self):
        os.system("cls")
        global lstClientes
        # ---Importar datos de clientes a la lista.---
        archivoClientes = open("clientes.pkl", "ab+")
        archivoClientes.seek(0)
        try:
            lstClientes = pickle.load(archivoClientes)
            print(f"Se cargaron {len(lstClientes)} empleados.")
        except EOFError:
            print("No existen empleados registados.")
        finally:
            archivoClientes.close()
        
        repetido = False

        print("___________ SUPER TIENDA LA COBANERITA ___________")
        print("___________Coban,Alta Verapaz")
        print("")
        NitCl = int(input("Ingrese numero de NIT"))
        contadorClientes = 0
        for clientes in lstClientes:
            if (clientes.getNitCl() == NitCl):
                repetido = True
                continue        
            contadorClientes += 1

            if repetido == True:
                return f"Nombre: {self.nomCl}"        
            else:
                print("Cliente no encontrado")
                
            

    msvcrt.getch()

