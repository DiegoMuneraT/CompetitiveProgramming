def estaLibre(fila, columna):
    """ Determina si la casilla f, c esta libre de ataques.
    
    @param f: Fila
    @param c: Columna
    @return: True si la casilla esta libre de ataques.
    """
    for i in range(8):
        if tablero[fila][i] == '[Q]' or tablero[i][columna] == '[Q]':
            return False
    if fila<=columna:
        c= columna-fila
        r = 0
    else:
        r = fila-columna
        c= 0
    while c < 8 and r < 8:
        if tablero[r][c] == '[Q]':
            return False
        r +=1
        c +=1
    if fila <= columna:
        r= 0
        c = columna + fila
        if c > 7:
            r = c - 7
            c = 7
    else:
        c = 7
        r = fila - (7 - columna)
    while c >= 0 and r < 8:
        if tablero[r][c] == '[Q]':
            return False
        r += 1
        c -= 1        
    return True

def agregar_Q(n):
    """Agregar n reinas
    @param n: numero de reinas a agregar
    @return True si se pudo agregar lo requerido"""
    
    if n < 1:
        return True
    
    for idx_fila in range(8):
        for idx_columna in range(8):
            if estaLibre(idx_fila, idx_columna):
                tablero[idx_fila][idx_columna] = '[Q]'
                if agregar_Q(n-1):
                    return True
                else:
                    tablero[idx_fila][idx_columna] = '[ ]'
    return False

tablero = []
n = 8
for i in range(n):
    tablero.append(['[ ]'] * n)
agregar_Q(n)
for fila in tablero:
    print(*fila)

