# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:14:56 2021

@author: ADMIN
"""
import time
import matplotlib.pyplot as plt
import random

def plot(times, n, lab):
    plt.xlabel('')
    plt.ylabel('Time Complexity')
    plt.plot(range(1,n), times, label = lab)
    plt.grid()
    plt.legend()
    plt.show()

def addition(summand_1, summand_2):
    return summand_1 + summand_2

times = []

for i in range(1, 500):
    start_time = time.time()
    addition(random.randint(0,100), random.randint(0,100))
    times.append(time.time() - start_time)
    
plot(times, 500, "Addition")
    