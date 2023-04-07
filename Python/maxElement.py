def arrayMax(arr, n):
    maximum = arr[n]  # constant
    if n != 0:  # constant
        temp = arrayMax(arr, n - 1)  # c1*n
        if temp > maximum:  # c2*n
            maximum = temp  # constant
    return maximum  # T(1)


#   T(n) = (c1 + c2)n
#   T(n) = O((c1+c2)n  O definition
#   T(n) = O(n) product rule
#   ____________+
#       O(n)

array = [1, 2, 3, 8, 10, 4]
print(arrayMax(array, 5))
