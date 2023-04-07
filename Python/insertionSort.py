from time import time


# Effective in less than 100 elements
def insertionSort(arr):
    start_time = time()
    for i in range(1, len(arr)):  # c1*n
        key = arr[i]  # c2*(n-1)
        j = i - 1  # c3*(n-1)
        while j >= 0 and key < arr[j]:  # c4*(n-1)(n)/2
            arr[j + 1] = arr[j]  # c5*((n-1)(n)/2-1)
            j -= 1  # c6*((n-1)(n)/2-1)
        arr[j + 1] = key  # c7*(n-1)
    elapsed_time = time() - start_time
    print(f"Tiempo de ejecución: {elapsed_time} seconds")


#  T(n) = c1*n + (c2+c3)*(n-1) + c4*(n-1)(n)/2 + (c5+c6)*((n-1)(n)/2-1) +
#         c7*(n-1)
#  T(n) = O(n + (n-1) + (n-1)(n)/2 + (n-1)(n)/2-1 + (n-1)) O definition
#  T(n) = O(n + (n-1) + (n-1)(n)/2 + (n-1)(n)/2-1 + (n-1)) product rule
#  T(n) = O((n-1) n + 3n - 3) simplified form
#  T(n) = O((n-1)n^2) sum rule
#  T(n) = O(n^2) product rule
#   _________________________+
#              O(n^2)
#   Complexity in the worst case when the array is sorted in descending order

arr = [38, 7, 5, 6, 9, 12, 21]
insertionSort(arr)
print("The sorted array is: ")
for i in range(len(arr)):
    print(arr[i])
