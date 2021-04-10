from ficheroClass import *
class Ordenar():
    
    def ordenarFichero(self,ficheroEntrada,ficheroSalida):
        lista = []
        listaFichero = ficheroEntrada.getLineas()
        
        for num in range(len(listaFichero)):
            lista.append(int(listaFichero[num]))

        lista = sorted(lista)

        ficheroSalida.escribirFicheroSalida(lista)
        print("Listo")