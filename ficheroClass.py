# *
# * Author: Fabian Dario Florez Raigoso
# *
from tkinter.filedialog import *
from io import *

# filename = askopenfilename()
# print(filename)
# fichero = open(filename,"r")
# print(len(fichero.readlines()))
# fichero.close()
# directoriname = asksaveasfile()
class Fichero():
    nombre = ""
    tipo = ""
    cantLineas = 0
    lineas = [] 
    
    # Constructor
    def __init__(self):
        pass
        
    def buscarNombre(self):
        self.nombre = askopenfilename()

    def contarLineas(self):
        ficheroTemporal = open(self.nombre, self.tipo)
        self.cantLineas = len(ficheroTemporal.readlines())
        ficheroTemporal.close()

    def leerLineas(self):
        if self.cantLineas == 0:
            return
        ficheroTemporal = open(self.nombre, self.tipo)
        self.lineas = ficheroTemporal.readlines()
        ficheroTemporal.close()

    def crearFicheroSalida(self):
        ficherosalida = asksaveasfilename(defaultextension='.txt')
        self.nombre = ficherosalida

    def crearFicheroEntrada(self):
        self.tipo = "r+"
        self.buscarNombre()
        self.contarLineas()
        self.leerLineas()
        print("Se creo un fichero")

    def __str__(self):
        text = "Nombre fichero: {}\n"\
            "Cantidad de lineas: {}\n".format(self.nombre,self.cantLineas)
        return text
        
