def entrance():
    n = int(input("N: "))
    for i in range(0, n):
        if (n > 0) and (n <= 5):
            k = int(input("K: "))
            if (k > 0) and (k <= 100):
                hashtable = dict()
                for i in range(0, k):
                    objet = input("character and price: ")
                    character = objet[0]
                    price = objet[1:7]
                    hashtable[character] = float(price)
        m = int(input("M: "))
        if (m > 0) and (m < 150000):
            text = ''
            suma = 0.00
            for i in range(0, m):
                s = input(f"Linea {i+1}:")
                text += s
            for character in text:
                if character in hashtable:
                    value = hashtable.get(character)
                    suma += value
                else:
                    suma += 0
            suma = suma/100
            print(suma, '$')

entrance()


