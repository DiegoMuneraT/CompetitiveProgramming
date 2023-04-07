def patron(n):
    array = []
    list = []
    j = 1
    if n > 0:
        for i in range(1, (n-(n-j))):
            array.extend(i)
            list.append(array)
            print(array)
            j += 1
        print(list)


patron(5)
