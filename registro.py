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

class registro:
    def registroArticulo(self):
        #Cargar Provedoores
        global lstProveedor
        os.system("cls")
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print("-------------------------------------------")
            print(f"Se cargaron {len(lstProveedor)} proveedores ")
        except EOFError:
            print("No existen proveedores")
        finally:
            archivoProveedor.close

        #Cargar Articulos
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

        repetido = False
        repetido2 = False

        print("___________ SUPER TIENDA LA COBANERITA ___________")
        print("___________    REGISTRO DE ARTICULOS   ___________")
        print("")
        while True:
            try:
                codArt = int(input("Ingrese el código del artículo: "))
            except ValueError:
                print("El código debe contener NUMEROS en su totalidad.\n")
                continue
            else:
                break

        contador = 0
        for articulos in lstArticulo:
            if (articulos.getCodArt()==codArt):
                repetido = True

        if repetido == True:
            print("Este codigo de articulo ya se encuentra ingresado")
            articulos = lstArticulo[contador]
            print("Presione Enter para regresar...")
        else:
            while True:
                try:
                    codProvArt =int(input("ingrese codigo de Provedoor"))
                except ValueError:
                    continue
                else:
                    break

            contadorProveedor = 0
            for proveedores in lstProveedor:
                if (proveedores.getCodProv()==codProvArt):
                    nomProv = proveedores.getNomProv()
                    repetido2 = True
                    break
                contadorProveedor += 1

            #si existe un provedoor repetido/valido
            if repetido2 == True:
                nomArt = input("Ingrese Nombre del Articulo ")
                cantArt = int(input(" Ingrese cantidad "))
                while True:
                    try:
                        precioArt = float(input("Ingrese el costo por unidad: Q."))
                    except ValueError:
                        print("El costo debe ser un NUMERO o DECIMAL.\n")
                        continue
                    else:
                        break
                #agregando articulo al archivo
                cantCompra = 0
                lstArticulo.append(registroA.Articulo(codArt, codProvArt, nomArt, cantArt, precioArt, cantCompra))
                archivoArticulo = open("articulos.pkl", "wb")
                pickle.dump(lstArticulo, archivoArticulo)
                archivoArticulo.close()
            else:
                print("No existe ningun proveedor con ese codigo")
                print("Presione enter para regresar...")
        msvcrt.getch()

    def registroProveedor(self):
        global lstProveedor
        os.system("cls")
        # ---Importar datos de proveedores a la lista.---
        archivoProveedor = open("proveedor.pkl", "ab+")
        archivoProveedor.seek(0)
        try:
            lstProveedor = pickle.load(archivoProveedor)
            print(f"Se cargaron {len(lstProveedor)} proveedores.")
        except EOFError:
            print("No existen proveedores registados.")
        finally:
            archivoProveedor.close()
        repetido = False

        print("REGISTRO PROVEEDOR")
        codProv = int(input("Ingrese codigo Proveedor"))
        #validar cod repetido

        contadorProveedor = 0
        for proveedores in lstProveedor:
            if (proveedores.getCodProv() == codProv):
                repetido = True
                continue
            contadorProveedor += 1

        
        if repetido == True:
            print("El codigo ya fue ingresado")
            print("Presione enter para contiduar")
        else:
            nomProv = input(" Ingrese Nombre Proveedor")

        #Almacenar proveedor
        lstProveedor.append(registroP.Proveedor(codProv, nomProv))
        archivoProveedor = open("proveedor.pkl", "ab+")
        pickle.dump(lstProveedor, archivoProveedor)
        archivoProveedor.close()
        print("Registro Correctamente")
        print("presione enter para regresar")
    msvcrt.getch()

    def registroEmpleados(self):
        global lstEmpleados
        os.system("cls")

        # ---Importar datos de empleados a la lista.---
        archivoEmpleados = open("empleados.pkl", "ab+")
        archivoEmpleados.seek(0)
        try:
            lstEmpleados = pickle.load(archivoEmpleados)
            print(f"Se cargaron {len(lstEmpleados)} empleados.")
        except EOFError:
            print("No existen empleados registados.")
        finally:
            archivoEmpleados.close()
        repetido = False

        print("REGISTRO Empleados")
        print("-------------------------------------")
        codEmp = int(input("Ingrese codigo Empleado"))
        
        #validar cod repetido
        contadorEmpleados = 0
        for empleados in lstEmpleados:
            if (empleados.getCodEmp() == codEmp):
                repetido = True
                continue       
            contadorEmpleados += 1

            if repetido == True:
                print("El codigo ya fue ingresado ")
                print("Presione enter para contiduar ")
            else:
                nomEmp = input(" Ingrese Nombre empleado: ")
                puesEmp = input(" Ingrese el puesto del empleado: ")
                #Almacenar Empleados
                lstEmpleados.append(registroE.Empleados(codEmp, nomEmp,puesEmp))
                archivoEmpleados = open("empleados.pkl", "ab+")
                pickle.dump(lstEmpleados, archivoEmpleados)
                archivoEmpleados.close()
                print("Registro Correctamente")
                print("presione enter para regresar")  
            break    
    msvcrt.getch()
    
    def registroClientes(self):
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

        print("REGISTRO CLIENTES")
        print("-------------------------------------")
        NitCl = int(input("Ingrese numero de NIT"))
        
        #validar cod repetido
        contadorClientes = 0
        for clientes in lstClientes:
            if (clientes.getNitCl() == NitCl):
                repetido = True
                continue        
            contadorClientes += 1

            if repetido == True:
                print("El codigo ya fue ingresado ")
                print("Presione enter para contiduar ")
            else:
                nomCl = input(" Ingrese Nombre del Cliente:  ")
                #Almacenar Empleados
                lstClientes.append(registroC.Cliente(NitCl, nomCl))
                archivoClientes = open("cleintes.pkl", "ab+")
                pickle.dump(lstClientes, archivoClientes)
                archivoClientes.close()
                print("Registro Correctamente")
                print("presione enter para regresar")  
            break    
    msvcrt.getch()