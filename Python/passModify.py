import numpy as np 

def password():
    rows = 6 
    columns = 5
    mat1 = []
    mat2 = []
    matFinal = []
    
    t = int(input("Test cases: "))
    for case in range(0,t):
        k = int(input("Order: "))
        
        #Llenamos la primera matriz
        for i in range(0,rows):
            fila = []
            combination = input()
            fila.append(list(combination))
            mat1.append(fila)
            
    #Todo este codigo se puede simplificar con
    #list = [""]*rows
    #list[i] = input()
    #Se llena toda la lista. 
    
        #Llenamos la segunda matriz    
        for i in range(0,rows):
            fila = []
            combination = input()
            fila.append(list(combination))
            mat2.append(fila)
        
        listCommon = []            
        for i in range(columns): # columna que queremos obtener
            columna = columnaN(mat1,i)
            columna2 = columnaN(mat2,i)
            for element in columna:
                for row in columna2:
                    for eachElement in row:  
                        if element == eachElement and element not in listCommon:
                            listCommon.append(element)
                            matFinal.append(listCommon)
def columnaN(mat, index):
    return [fila[index] for fila in mat if index < len(fila)]
    
          
password()
matriz1 = [
    ['A','Y','G','S','U'],
    ['D','O','M','R','A'],
]
