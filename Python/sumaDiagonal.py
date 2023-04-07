def diagSum(arr):
    n = len(arr)
    sum = 0
    for i in range(n):
        for j in range(n):
            if i == j:
                sum += arr[i][j]
    print(sum)
            
matriz = [ [2,3,4], [3,6,7], [8,9,10] ] #sum = 2+6+10 = 18
diagSum(matriz)