"""
Listas são mutáveis e representadas/definidas por colchetes []
"""

lista1 = []
lista2 = [1, 2, 3, 4, 5]
lista3 = list(range(1, 6))
if lista2 == lista3:
    print("São iguais")

num = int(input("Insira um número: "))
if num in lista2:
    print(f"{num} encontrado na lista2")

lista4 = list("Pedro Fernandes")
if 'e' in lista4:
    print(f"Tem {lista4.count('e')}")

# Adicionar no final um elemento
print(lista3)
lista3.append(6)  # Um por vez
lista3.append('Pedro')
print(lista3)

# Adicionar no final múltiplos elementos
lista3.extend([7, 8, 9, 10, 12])  # Adiciona mais de um por vez
lista3.extend('Pedro')
lista3.extend('Da Silva')
print(lista3)

# Organizar
print(lista4)
lista4.sort()

# Inserir em um índice específico
lista4.insert(6, list('Pouzada '))

# Inverter a lista
lista4.reverse()  # print(lista4[::-1])
print(lista4)

# Cópia da lista
lista5 = lista4.copy()
print(lista5)

# Comprimento da lista
print(f"lista5 tem {len(lista5)} elementos")

# Remover elemento
print(lista3)
lista3.pop()

print(lista3)

# Remover específico
lista3.pop(1)
print(lista3)

# Dividir a lista
frase = "Bom dia, pessoal"
print(frase.split())
print(frase.split(','))

# Transformar lista em string
frase2 = list('Pedro Pouzada Fernandes')
print(frase2)
frase2str = ' '.join(frase2)
print(frase2str)

# Iterando sobre listas
carrinho = []
produto = ''

while produto != 'sair':
    print("Escolha um produto: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto, end=', ')

lista6 = ['branco', 'azul', 'preto']
#  lista6[0] = 'branco'
#  lista6[1] = 'azul'
#  lista6[2] = 'preto'

print(lista6[-1])
print(lista6[-2])
print(lista6[-3])

numeros = [1, 5, 8, 9, 13, 5, 17, 22, 28, 5, 31]
print(numeros.index(5))  # Retorna o primeiro que achar
print(numeros.index(5, 2, 10))  # Retorna o primeiro que achar em determinado intervalo

# Slicing de lista: lista[aonde_começar (default = 0):aonde_terminar (default = len(lista)):passo (default = 1))]
print(numeros[1::2])

# Reverter lista
boolean_list = [True, False]
boolean_list[0], boolean_list[1] = boolean_list[1], boolean_list[0]
print(boolean_list)

# Se a lista for maior...
boolean_list.reverse()
print(boolean_list)

# Funções importantes
print(sum(numeros))
print(max(numeros))
print(min(numeros))
print(len(numeros))

tuplaNumeros = tuple(numeros)
print(tuplaNumeros, type(tuplaNumeros))

numeros_pouco = [1, 2, 3]
num1, num2, num3 = numeros_pouco
print(num1)
print(num2)
print(num3)

# DEEP COPY:
numeros_deep_copy = numeros_pouco.copy()
numeros_deep_copy.append(99)
print(numeros_deep_copy)
print(numeros_pouco)  # Lista original não é influenciada com o DEEP COPY

# SHALLOW COPY:
numeros_shallow_copy = numeros_pouco
numeros_shallow_copy.append(99)
print(numeros_shallow_copy)
print(numeros_pouco)  # Lista original é influenciada com o SHALLOW COPY
