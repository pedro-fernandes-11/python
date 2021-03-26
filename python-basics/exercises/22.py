nota, qtd, soma = 15, 0, 0

while 10 <= nota <= 20:
    nota = 0
    nota = int(input("Qual sua nota?"))
    if nota < 10 or nota > 20:
        break
    soma += nota
    qtd += 1

print(f"Média aritmética: {soma/qtd}")
