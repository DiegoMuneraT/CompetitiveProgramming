#1 Backtracking, brute force
def password():
    rows = 6
    cols = 5
    #Entrada de los casos de prueba
    test_cases = int(input())
    for t in range(test_cases):
        #Entra k
        k = int(input())
        list1 = [""]*rows
        for i in range(rows):
            list1[i] = input()
        list2 = [""]*rows
        for i in range(rows):
            list2[i] = input()
        
        #Guardar los elementos en común que encuentre"
        commonList = []
        for i in range(cols):
            commonList.append([])
            for j in range(rows):
                for t in range(rows):
                    if list1[j][i] not in commonList[i] and list1[j][i] == list2[t][i]:
                        commonList[i].append(list1[j][i])
        #Se sortea los elementos de las columnas
        for i in range(cols):
            commonList[i].sort()
        #Arreglo de posibilidades
        prob = [0]*cols
        for i in range(cols):
            if i == 0:
                prob[4] = len(commonList[4])
            else:
                prob[5-i-1] = prob[5-i] * len(commonList[5-i-1])
        if prob[0] < k:
            print("NO")
        else:
            remainder = k-1
            answ = ""
            # Usar la division y el modulo para hallar las posibilidades de combinación
            for i in range(1,cols):
                quote = remainder // prob[i]  #cociente=residuo entre probs
                answ += commonList[i-1][quote] #lista de comunes y cociente
                remainder = remainder % prob[i] #mod entre residuo y prob en i
            answ += commonList[4][remainder]
            print(answ)
password()