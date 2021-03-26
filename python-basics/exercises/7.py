numero = 0
soma = 0

while numero != 10:
    valor = int(input("Valor: "))
    if valor > 0:
        soma += valor
        numero += 1

print(f"Soma: {soma}")
print(f"Média: {soma / 10}")
