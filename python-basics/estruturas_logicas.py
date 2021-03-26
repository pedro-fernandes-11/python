"""
Operador unário: not
Operadores binários: and, or e is
"""

ativo = True
logado = False

if ativo and logado:
    print("Ativo e logado")

if not ativo:
    print("Não está ativo")

if ativo or logado:
    print("Está ativo ou logado")

if ativo is True:
    print("Está ativo")  # Is tem o mesmo comportamento de ==
