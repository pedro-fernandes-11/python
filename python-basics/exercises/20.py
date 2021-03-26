numero = 0

while numero != 1000:
    numero = int(input("Informe um número"))
    if numero % 2 == 0:
        print("Par")
    elif numero % 2 == 1:
        print("Ímpar")
