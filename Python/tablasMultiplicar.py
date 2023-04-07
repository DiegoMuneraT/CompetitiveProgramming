def tablasM(n):
    for i in range(1, n):   # c1*n
        print(f'Tabla del:', i)  # c2*(n-1)
        hashtable = dict()  # c3
        for j in range(1, 11):  # c4+(n*m)
            m = i * j   # c5+(n*(m-1))
            hashtable[1] = m    # c6
            print(hashtable)


# T(n) = (c1*n) + (c2*(n-1)) + c3 + (c4+(n*m)) + (c5+(n*(j-1))) + c6
# T(n) = n(c1+2m-1) + c2(n-1) + c3 + c4 + c5 + c6 simplified form
# T(n) = O(n(c1+2m-1) + c2(n-1) + c3 + c4 + c5 + c6) O definition
# T(n) = O(n(2m-1) + c2*n) sum rule
# T(n) = O(2m*n-n + c2*n) expanded form
# T(n) = O(2m*n * n) product rule
# T(n) = O(n^2) product rule
# __________________________+
#           O(n^2)
# Complexity in the worst case, when n is too big

tablasM(5)
