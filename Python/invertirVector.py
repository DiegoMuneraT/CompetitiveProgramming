import math


def invert(array):
    arrayInverted = array[::-1]
    return arrayInverted


array = []
n = int(input('Input a number: '))
while n != -1:
    array.append(n)
    n = int(input('Input a number: '))

print(array)
print(invert(array))
