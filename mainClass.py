# *
# * Author: Fabian Dario Florez Raigoso
# *
from ordenarClass import *
from ficheroClass import *

def definirFicheroEntrada():
    fichero = Fichero()
    fichero.crearFicheroEntrada()
    return fichero

def definirFicheroSalida():
    fichero = Fichero()
    fichero.crearFicheroSalida()
    return fichero

def menu():
    opcion = 0
    print("\t\t\tmenu\n"\
    "Opciones\n"\
    "\t(1)\tSeleccionar Fichero que desea Ordenar\n"\
    "\t(2)\tCrear Fichero donde guardara el resultado ordenado\n"\
    "\t(3)\tOrdenar Fichero\n\n"\
    "\t(4)\tSalir\n")
    try:
        opcion = int(input("Ingresa tu opcion\n-->"))
    except ValueError:
        print("Ingresa una opcion correcta")
    except Exception as e:
        print(type(e).__name__)
    finally:
        return opcion 

def protocoloSalida():
    opcion = 0
    print("\n\n"\
        "¡¡¡¡---Esta Seguro---!!!!\n"\
        "\t(1)\tNo\n"\
        "\t(2)\tSi\n")
    try:
        opcion = int(input("Ingresa tu opcion\n-->"))
    except ValueError:
        print("Ingresa una opcion correcta")
    except Exception as e:
        print(type(e).__name__)
    finally:
        return opcion 
    
def main():
    print(\
    "+---------------------------+\n"\
    "\tBienvenido\n"\
    "+---------------------------+")
    while(True):
        opc = menu()
        if opc == 4:
            salirOpc = protocoloSalida()
            if salirOpc == 2:
                print("\nSalinedo...")
                break
            elif salirOpc == 1:
                print("\nVolviendo al menu...")
        if opc == 1:
            ficheroEntrada = definirFicheroEntrada()
        elif opc == 2:
            ficheroSalida = definirFicheroSalida()
        elif opc == 3:
            ord = Ordenar()
            ord.ordenarFichero(ficheroEntrada,ficheroSalida)
        else:
            print("Opcion no encontrada")

# Ejecutamos el main
main()
