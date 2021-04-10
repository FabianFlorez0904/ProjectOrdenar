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


def main():
    print("Hola Mundo!")
    ficheroEntrada = definirFicheroEntrada()
    ficheroSalida = definirFicheroSalida()

# Ejecutamos el main
main()