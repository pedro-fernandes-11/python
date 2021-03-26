n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))

soma = n1 + n2
produto = n1 * n2
subtracao = n1 - n2
divisao = n1 / n2
divisaoi = n1 // n2
potencia = n1 ** n2

print('A soma dos números é {} \nO produto dos números é {} \nA'.format(soma, produto), end=' ')
print('subtração dos números é {} \nA divisão dos números é {}'.format(subtracao, divisao))
print('A divisão inteira dos números é {}\n{} elevado na potência {} é {}'.format(divisaoi, n1, n2, potencia))
