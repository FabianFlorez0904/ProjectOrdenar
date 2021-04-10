# *
# * Author: Fabian Dario Florez Raigoso
# *
from ordenarClass import * 
from tkinter.filedialog import askopenfilename

def main():
    print("Hola Mundo!")
    filename = askopenfilename()
    print(filename)
# Ejecutamos el main
main()