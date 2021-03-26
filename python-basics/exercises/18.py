maior = -9999
menor = 9999
maiorContagem = 0
qtde = int(input("Quanto números deseja ler?"))

for i in range(1, qtde + 1):
    numero = int(input(f"{i}° número:"))
    if numero > maior:
        maior = numero
        maiorContagem += 1
    if numero < menor:
        menor = numero

print(f"Maior: {maior}")
print(f"Quantidade de vezes maior ultrapassado: {maiorContagem}")
