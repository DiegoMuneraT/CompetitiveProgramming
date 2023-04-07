# método para dividir un segmento en dos variables
def getParts(segment):
    Li, Ri = map(int, segment.split())
    return Li, Ri

def minimalCoverage():
    answer = []
    # entran los casos de prueba
    test_cases = int(input())
    input()
    
    # loop para cada caso de prueba
    for case in range(test_cases):
        list = []
        m = int(input())
        segment = input()
        rightmost = -1
        # llenamos la lista de segmentos mientras el que ingresen no sea 0 0
        while(segment != "0 0"):
            l, r = getParts(segment)
            if r > 0 and l <= m:
                rightmost = max(rightmost, r)
                list.append((l, r))
            segment = input()

        list.sort()

        candidates = []
        if not (len(list) and ((list[0][0] > 0) or (rightmost < m))):
            # tomamos los candidatos y guardamos la respuesta
            for i in range(len(list)):
                l, r = list[i]
                ncand = len(candidates)
                #print("LS",list)
                #print(l, r)
                #print("Can",candidates)
                l = 0 if l < 0 else l
                if not ncand:
                    candidates.append(list[i])
                else:
                    ll, rl = candidates[-1]

                    ll = 0 if ll < 0 else ll
                    
                    if ncand >= 2:
                        l2, r2 = candidates[-2]
                        ll = r2
                    
                    if rl >= m and l > ll:
                      break

                    if l > rl:
                        candidates.clear()
                        break
                    elif l == rl:
                        candidates.append(list[i])
                    elif l == ll:
                      	if r > rl:
                          candidates.pop(-1)
                          candidates.append(list[i])
                    else:
                        if r <= rl:
                            continue
                            
                        if l > ll:
                          candidates.append(list[i])
                        else:
                          candidates.pop(-1)
                          candidates.append(list[i])

        input()
        answer.append(candidates)
    if(len(answer)):
        #imprimimos la respuesta
        for i in range(len(answer)-1):
            if len(answer[i]) == 0:
                print("0")
            else:
                print(len(answer[i]))
                for seg in answer[i]:
                    print(seg[0], seg[1])
            print()
            
        if len(answer[-1]) == 0:
                print("0")
        else:
            print(len(answer[-1]))
            for seg in answer[-1]:
                print(seg[0], seg[1])
minimalCoverage()