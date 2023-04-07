
def arraySum(arr):
    sum = 0
    for i in range(0, len(arr)):  # c1*n
        sum += arr[i]   # c2*(n-1)
    return sum  # c3


#   T(n) = c1*n + c2*(n-1) + c3
#   T(n) = O(c1*n + c2*(n-1) + c3) O definition
#   T(n) = O(n + (n-1)) sum rule
#   T(n) = O(2n-1) simplified expression
#   T(n) = O(2n) sum rule
#   ______________________
#          O(2n)
#   Complexity in the worst case, when the array is too long


array = [10, 20, 30, 40, 50, 60, 100, 10000]
print(arraySum(array))
