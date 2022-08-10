#método para dividir un segmento en dos variables
def getParts(segment):
    Li,Ri = map(int,segment.split())
    return Li,Ri

def minimalCoverage():
    #entran los casos de prueba
    test_cases = int(input())
    print("\n")
    #loop para cada caso de prueba
    for case in range(test_cases):
        list = [] 
        m=int(input())
        segment = input()
        #llenamos la lista de segmentos mientras el que ingresen no sea 0 0
        while(segment != "0 0"):
            list.append(segment)
            segment = input()
            
        for i in range(0,len(list)): # sorting list
            L, R = getParts(list[i])
            for j in range(i+1, len(list)):
                L2, R2 = getParts(list[j])
                if L > L2:
                    list[i], list[j] = list[j], list[i]
        Lmin = 0 
        Rmin = 0
        count = 0
        candidates = []
        
        for i in range(len(list)): # getting candidates
            L, R = getParts(list[i])
            if L<=0 and R>= m:
                candidates.clear()
                candidates.append(list[i])
                count+=1
                break
            elif L<=Rmin and R>Rmin: # [0 4] - [2 6] - [3 6]
                Lmin = L
                Rmin = R
                candidates.append(list[i])
                count+=1
        answer = []
    answer.append(candidates)
    print("\n",count, end="")
    for i in answer:
        for j in i:
            if len(i) == 0:
                print("0","\n")
            else:
                print(j)
    return 0;       
minimalCoverage()