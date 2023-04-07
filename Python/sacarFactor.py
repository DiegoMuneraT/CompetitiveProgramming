# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 10:40:47 2021

@author: DIEGO
"""
def factorial_recursive(n):
    #Caso base: 1! = 1
    if (n==1):
        return 1
    
    #Caso recursivo: n*(n-1)!
    else: 
        return n*factorial_recursive(n-1)
    
factorial = int(input('Factorial de: '))
print(factorial_recursive(factorial))
