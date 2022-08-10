# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 09:44:22 2021

@author: ADMIN
"""
#definimos el nodo
class Node:
    def __init__(self, data):
        _next = None
        _data = data
        
#creamos la lista
class ListaDiego:
    def __init__(self):
        self.first = None
        self.size = 0
        
    def getNode(self, index):
        temp = self.first
        for i in range(index):
            temp = temp.next
        return temp
    
    def get(self, index):
        temp = self.first
        for i in range(index):
            temp = temp.next
        return temp.data
    
    def addFirst(self, e):
            #pasos para agregar al inicio:
            #(1)crear un nodo con el elemento adentro
            newNode = Node(e)
            #El siguiente del nodo es el primero que teniamos
            newNode.next = self.first
            #El nuevo nodo va a ser el primero
            self.first = newNode
    
    def add(self, e, i):
        if i == 0:
            Node.addFirst(e)
        else:
            nodeIlessOne = self.getNode(i-1)
            newNode = Node(e)
            temp = nodeIlessOne.next
            nodeIlessOne.next = newNode
            newNode.next = temp
        
    def contains(self, e):
        temp = self.first
        while(temp == None):
            if(temp.data == e):
                return True
            temp = temp.next
        return False
        