maior = -99999
menor = 99999

for i in range(1, 11):
    valor = int(input("Valor:"))
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor

print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
