print("Qual seu nome?")
nome = input()

print(f"Olá {nome}, quantos anos você tem?")
idade = int(input())

if idade < 18:
    menor = True
    print("Menor de idade")
else:
    menor = False
    print("Maior de idade")

if menor:
    print("Quanto tirou na prova?")
    nota = float(input())
    if 6 > nota >= 0:
        print("Você está reprovado")
    elif nota == 6:
        print("Você está na média")
    elif 10 >= nota > 6:
        print("Você está aprovado")
    else:
        print("Nota inválida")
