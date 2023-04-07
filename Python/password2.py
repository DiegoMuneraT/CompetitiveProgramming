def main():
  # Entrada de los casos de prueba
  casos_de_prueba = int(input())
  for t in range(casos_de_prueba):
    # Entrada de k
    k = int(input())
    # Definir lista 
    imagen1 = [""] * 6
    for i in range(6):
      # Coger entrdada de la primera imagen
      imagen1[i] = input()
    imagen2 = [""] * 6
    for i in range(6):
      # Coger entrada de la segunda imagen
      imagen2[i] = input()
    # Agregar los elementos iguales de las columnas
    iguales = []
    for i in range(5):
      iguales.append([])
      for j in range(6):
        for l in range(6):
          if imagen1[j][i] not in iguales[i] and imagen1[j][i] == imagen2[l][i]:
            iguales[i].append(imagen1[j][i])
    # Ordenar los elementos de las columnas
    for i in range(5):
      iguales[i].sort()
    # Crear lista de posibilidades
    posibilidades = [0] * 5
    for i in range(5):
      if i == 0:
        posibilidades[4] = len(iguales[4])
      else:
       posibilidades[5-i-1] = posibilidades[5-i] * len(iguales[5-i-1])
    # Encontrar la posibilidad k
    if posibilidades[0] < k:
      print("NO") 
    else:
      residuo = k-1
      respuesta = ""
      # Usar división y módulo para hallar las posibilidades de combinaciones
      for i in range(1,5):
        cociente = residuo // posibilidades[i]
        respuesta += iguales[i-1][cociente]
        residuo = residuo % posibilidades[i]
      respuesta += iguales[4][residuo]
      print(respuesta)
main()