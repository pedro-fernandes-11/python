receita = dict(jan=800, fev=900, mar=1000)

for chave in receita:
    print(f"{chave} = R${receita[chave]}")

for chave, valor in receita.items():
    print(f"{chave} = R${valor},", end=' ')

print("\n")
print(sum(receita.values()))
print(min(receita.values()))
print(max(receita.values()))

print(receita.items())