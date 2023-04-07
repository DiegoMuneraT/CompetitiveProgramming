# -*- coding: utf-8 -*-
"""
Created on Sun May  2 19:23:31 2021

@author: ADMIN

Métodod de busqueda en binary tree
"""

def __buscar(self, nodo, busqueda):
    if nodo is None:
        return None
    if nodo.dato == busqueda:
        return nodo
    if busqueda < nodo.dato:
        return self.__buscar(nodo.izquierda, busqueda)
    else:
        return self.__buscar(nodo.derecha, busqueda)