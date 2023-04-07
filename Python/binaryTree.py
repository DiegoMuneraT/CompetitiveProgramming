# -*- coding: utf-8 -*-
"""
Created on Sun May  2 18:37:44 2021

@author: ADMIN
"""


class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

    def __insertarDatos(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__insertarDatos(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__insertarDatos(nodo.derecha, dato)

    def __recorridoPO(self, nodo):
        if nodo is not None:
            self.__recorridoPO(nodo.izquierda)
            self.__recorridoPO(nodo.derecha)
            print(nodo.dato, end="\n")


class Arbol:

    # Funciones privadas
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    def __insertarDatos(self, nodo, dato):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.__insertarDatos(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.__insertarDatos(nodo.derecha, dato)

    def __recorridoPO(self, nodo):
        if nodo is not None:
            self.__recorridoPO(nodo.izquierda)
            self.__recorridoPO(nodo.derecha)
            print(nodo.dato, end="\n")

    # Funciones publicas
    def agregar(self, dato):
        self.__insertarDatos(self.raiz, dato)

    def postorder(self):
        print("Output PostOrder: ")
        self.__recorridoPO(self.raiz)
        print("")

    def inpt():
        print("Input preorder data")
        n = int(input("Input 0 to break: "))
        arbol = Arbol(n)
        while n != 0:
            n = int(input("Input 0 to break: "))
            if n == 0:
                break
            arbol.agregar(n)
        arbol.postorder()


Arbol.inpt()
