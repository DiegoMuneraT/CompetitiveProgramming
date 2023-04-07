# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 12:00:37 2021

@author: ADMIN
"""


def power_recursive(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        return base * power_recursive(base, exponent - 1)


base = int(input('Base: '))
potencia = int(input('Potencia: '))

print(power_recursive(base, potencia))
