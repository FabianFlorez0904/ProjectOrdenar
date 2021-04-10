# *
# * Author: Fabian Dario Florez Raigoso
# *
from tkinter.filedialog import *
from io import *

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
        ficherosalida = open(ficherosalida,"w")
        ficherosalida.close()

    def crearFicheroEntrada(self):
        self.tipo = "r+"
        self.buscarNombre()
        self.contarLineas()
        self.leerLineas()
        print("Se creo un fichero")

    def escribirFicheroSalida(self, lista):
        fichero = open(self.nombre,"w")
        for line in lista:
            fichero.write(str(line))
            fichero.write("\n")
        fichero.close()

    def __str__(self):
        text = "Nombre fichero: {}\n"\
            "Cantidad de lineas: {}\n".format(self.nombre,self.cantLineas)
        return text
    
    def getNombre(self):
        return self.nombre

    def getCantLineas(self):
        return self.cantLineas

    def getLineas(self):
        return self.lineas        
