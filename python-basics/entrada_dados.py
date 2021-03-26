nome = input("Qual seu nome?")

print(f"Olá {nome.title()}, qual seu ano de nascimento?") # .title() Primeira letra maiúscula
nascimento = input()

print(f"Se você nasceu em {nascimento}, você tem {2020 - int(nascimento)} anos")
# foi feito um cast (conversão) para um número inteiro, tudo lido em um input é string