# Int, Float, Complex

print("Int, Float, Complex:")

numeroInteiro = 5
print(numeroInteiro)

numeroReal = 3.1415
print(numeroReal)

numeroComplexo = 6j
print(numeroComplexo)

# Casting

float(numeroInteiro)
int(numeroReal)  # Arredonda pro menor inteiro

# Boolean

print("Boolean:")

ativo = True
print(f"O funcionário está ativo: {ativo}")

print(f"O Funcionário está ativo: {ativo}")
print(not ativo)

logado = False
print(ativo or logado)  # True
print(ativo and logado)  # False

"""
String:
Sempre que estiver entre aspas simples, duplas, simples triplas ou duplas triplas
"""

print("String:")

intString = "6"
floatString = '3.14'
booleanString = 'True'

print(f"{intString} = {type(intString)}")
print(f"{floatString} = {type(floatString)}")
print(f"{booleanString} = {type(booleanString)}")

nome = 'pedro pouzada fernandes'

print(nome.upper())
print(nome.lower())

nome = nome.title()
print(nome.title())

print(nome.split())  # Separação em elementos de um Array
print(nome[0:6])  # Slice de String
print(nome[::-1])  # Inversão uma String [::] => primeiro ao último
print(nome.replace('P', 'E'))  # Replace de String

# NoneType: tipo sem tipo (vazio)
# None sempre será falso
teste = None
print(teste)
print(type(teste))
