# -*- coding: utf-8 -*-
"""
Created on Thu May  6 09:55:47 2021

@author: ADMIN

Caracteres que no estan en común
"""
def noComunes(A,B): #N long A, M long B
    respuesta= ""
    for a in A: #O(N)
        if not a in B: #O(N*M)
            respuesta = respuesta + a #O(N)
    for b in B: #O(M)
        if not b in A: #O(M*N)
            respuesta = respuesta + b #O(M)
    return respuesta #O(1)
        #________________+
        #    O(N*M) Intentarlo resolver en O(N+M)
            
noComunes("abcd","afgd")

def noComunesHash(A,B):
    respuesta = "" #O(N)
    tabla = dict()
    for a in A: #O(N)
        if a in tabla.keys():
            pass
        else:
            tabla[a] = True
    for b in B: #O(M)
        if b in tabla.keys():
            tabla[b] = False
        else:
            tabla[b] = True
    for c in tabla.keys(): #O(N+M)
        if tabla[c] == True:
            respuesta = respuesta + c
    return respuesta #O(1)
        #________________+
        #     O(N+M)
        
noComunesHash("ABCD","ABCDFE")
