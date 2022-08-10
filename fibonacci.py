def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#   T(n) = T(n-1) + T(n-2)
#   T(n) = 2*T(n-1)
#   T(n) = O(2*T(n-1) O definition
#   T(n) = O(2^(n-1)) product rule
#   T(n) = O(2^n) sum rule
#   ____________+
#       O(2^n)

print(fibonacci(8))
