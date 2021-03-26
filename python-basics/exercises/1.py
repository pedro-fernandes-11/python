for i in range(10):
    contador = 0
    if i % 3 == 0 and i != 0:
        print(f"{i} é múltiplo de 3")
        contador += 1
    if contador == 5:
        break
