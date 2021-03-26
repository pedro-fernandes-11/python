nome = 'Pedro Pouzada Fernandes'
lista = [1, 2, 3, 4, 5]
numeros = range(1, 10)

for letra in nome:
    print(letra, end='')
print('\n')

for item in lista:
    print(item, end='')
print('\n')

for numero in numeros:
    print(numero, end='')
print('\n')

for indice, letra in enumerate(nome):
    print(f'{indice}: {letra}', end='')

print('\n\n')

print('Quantas vezes rodar?')
qtde = int(input())
soma = 0

for item in range(1, qtde + 1):
    print('+ quanto?')
    valor = int(input())
    soma += valor

print(f'A soma deu: {soma}')
