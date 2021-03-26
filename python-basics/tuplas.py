"""
Tuplas são imutáveis e representadas por parênteses
Definidas pelo uso de vírgula, não pela utilização de parênteses ()
"""

tupla1 = (1, 2, 3)
print(f"{tupla1}: {type(tupla1)}")

tupla2 = 1, 2, 3
print(f"{tupla2}: {type(tupla2)}")

tupla3 = (1,)  # (num) somente retornaria um inteiro, adicionando a vírgula, indicamos que é uma tupla
print(f"{tupla3}: {type(tupla3)}")

tupla_range = tuple(range(0, 3))
print(f"{tupla_range}: {type(tupla_range)}")

# Desempacotamento de tupla
tupla_nome_completo = 'Pedro', 'Pouzada', 'Fernandes'
primeiro, meio, ultimo = tupla_nome_completo
print(primeiro, end=' ')
print(meio, end=' ')
print(ultimo)

# Soma, Mínimo, Máximo e Tamanho
print(sum(tupla_range))
print(min(tupla_range))
print(max(tupla_range))
print(len(tupla_range))

# Concatenação
print(tupla1 + tupla_range)

if 'Pedro' in tupla_nome_completo:
    for index, value in enumerate(tupla_nome_completo):
        print(f"[{index}]: {value}")

nome_completo2 = tuple('Pedro Pouzada Fernandes')
print(f"{nome_completo2} tem {nome_completo2.count('e')} letras 'e'")

# OBS: Tuplas são iguais listas, com a diferença de serem imutáveis e representadas por parêntese
# Por serem imutáveis, devemos SEMPRE utiliza-las quando formos tratar de algo fixo

dias_da_semana = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro',
         'Outubro', 'Novembro', 'Dezembro')

print(dias_da_semana)
print(meses)
