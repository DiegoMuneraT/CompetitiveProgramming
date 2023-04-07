# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 18:20:57 2021

@author: ADMIN
"""
from time import time

""" Se organizan 2 sub arrays"""


def merge(left, right, arr):
    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i = i + 1
        else:
            arr[k] = right[j]
            j = j + 1
        k = k + 1
    while i < len(left):
        arr[k] = left[i]
        i = i + 1
        k = k + 1
    while j < len(right):
        arr[k] = right[j]
        j = j + 1
        k = k + 1


"""Se divide en 2 el array y se llama a la funcion de ordenamiento"""


def mergeSort(arr):
    start_time2 = time()
    n = len(arr)
    if n < 2:
        return

    mid = n / 2
    mid = int(mid)

    left = arr[0:mid]
    right = arr[mid:n]

    mergeSort(left)
    mergeSort(right)
    merge(left, right, arr)
    elapsed_time2 = time() - start_time2
    print(f"Tiempo de ejecución: {elapsed_time2} seconds")


# main
arr = [9, 6, 14, 18, 25, 29, 31, 42, 50]
mergeSort(arr)
for i in arr:
    print(i)
