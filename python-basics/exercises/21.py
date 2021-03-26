soma = 0
mult = 1
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma += i
        
    if i % 2 != 0:
        mult *= i

print(soma)
print(mult)
