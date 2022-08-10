# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 15:56:59 2021

@author: ADMIN
"""

from time import time
def suma():
    start_time = time()
    x = 5
    y = x + 5
    print(y)
    elapsed_time = time() - start_time
    print(f"Tiempo de ejecución: {elapsed_time} seconds")
    
suma()
