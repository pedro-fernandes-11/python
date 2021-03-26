preco = float(input('Qual o preço do produto? '))
desconto = preco * (5/100)
preco_final = preco - desconto

print('O preço final do produto sai por R${}'.format(preco_final))