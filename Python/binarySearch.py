# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 16:24:03 2021

@author: ADMIN
"""

import random
import time 
import matplotlib.pyplot as plt

def plot(times, n, lab):
    plt.xlabel('')
    plt.ylabel('Time Complexity')
    plt.plot(range(1,n), times, label = lab)
    plt.grid()
    plt.legend()
    plt.show()

def binary_search(item_list, item):
    first = 0
    last = len(item_list)-1
    found = False
    while(first<=last and not found):
        mid = (first + last)//2
        if item_list[mid] == item:
            found = True
        else:
            if item<item_list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return found

times = []
for i in range(1, 6000):
    array = [random.randint(0, x) for x in range(6000)]
    array.sort()
    start_time = time.time()
    binary_search(array, array[random.randint(0, i)])
    times.append(time.time() - start_time)
    
plot(times, 6000, "Binary Search")
        