soma = 0
contador = 0

for i in range(1, 99999):
    if i % 2 == 0:
        soma += i
        print(i)
        contador += 1

    if contador == 50:
        break
print(soma)
