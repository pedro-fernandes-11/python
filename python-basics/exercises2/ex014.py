salario = float(input('Qual seu salário? '))
aumento = salario * (15/100)
salario_final = salario + aumento

print('Seu salário, com o aumento, ficará R${}'.format(salario_final))