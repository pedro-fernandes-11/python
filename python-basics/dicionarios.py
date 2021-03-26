"""
Dicionários é um conjunto de chave/valor
São representados/definidos pela utilização de colchetes {}
"""

dados = {'Nome': 'Pedro Pouzada Fernandes',
         'Data de nascimento': '25.02.2003',
         'CPF': '054.812.420-52',
         'Nome do pai': 'Márcio da Silva Fernandes',
         'Nome da mãe': 'Rosângela Pouzada Ferandes'
         }

dados_segunda_forma = dict(Nome='Pedro Pouzada Fernandes',
                           Nascimento='25.02.2003',
                           CPF='054.812.420-52',
                           Nome_do_pai='Márcio da Silva Fernandes',
                           Nome_da_mãe='Rosângela Pouzada Ferandes',
                           )

print(dados)
print(type(dados))
print(dados_segunda_forma)
print(type(dados_segunda_forma))

# Acessar dados através da chave, diferentemente de lista/tupla, que é através do índice
print(dados['Nome'])  # Se não encontrar a chave, retornará erro
print(dados.get('Nome avô'))  # Se não encontrar a chave, não retornará erro

estado_civil = dados.get('Estado civil')

if estado_civil:
    print(f"O {dados.get('Nome')} está {dados['Estado civil']}")
else:
    print("Estado civil não informado")

# .get(chave, default = None)
estado_civil = dados.get('Estado civil', 'Não encontrado')
print(estado_civil)

if 'Estado civil' in dados:
    print("True")
else:
    print("False")

# OBS: É interessante utilizar tuplas como chave de dicionário, pois são imutáveis

# Adicionar valores em um Dict:
receita = {'janeiro': 9999.90,
           'fevereiro': 9999.90,
           'março': 9999.90
           }

receita['abril'] = 9999.90
receita.update({'maio': 9999.90})

print(receita)

# Remover dados de um Dict (SEMPRE informar chave)
receita.pop('maio')  # Valor removido é retornado
print(receita)

del receita['abril']  # Valor removido não é retornado
print(receita)

"""
Carrinho loja virtual comparação Lista x Tupla x Dicionário
"""

# List
carrinho = []

produto1 = ['PlayStation', 1, 2300.00]
produto2 = ['Xbox', 2, 1700.00]

carrinho.extend([produto1, produto2])
print(f"List: {carrinho}")

# Tuple
carrinho = []

produto1 = ('PlayStation', 1, 2300.00)
produto2 = ('Xbox', 2, 1700.00)

carrinho = (produto1, produto2)
print(f"Tuple: {carrinho}")

# Dictionary
carrinho = []

produto1 = {'Nome': 'PlayStation', 'Quantidade': 1, 'Preço': 2300.00}
produto2 = {'Nome': 'Xbox', 'Quantidade': 2, 'Preço': 1700.00}

carrinho.append(produto1)
carrinho.append(produto2)
print(f"Dictionary: {carrinho}")

d = dict(a=1, b=2, c=3)
print(d)
d.clear()  # Limpa o dicionário
print(d)

# .fromkeys(iterable, value)
dic = {}
dic = dic.fromkeys(['Nome', 'Emprego', 'Estágio', 'Estudando'], 'negativo')
print(dic)

antes_de_100 = range(0, 100)
dictionary1 = {}
dictionary1 = dictionary1.fromkeys(antes_de_100, 'Antes de 100')
print(dictionary1)
