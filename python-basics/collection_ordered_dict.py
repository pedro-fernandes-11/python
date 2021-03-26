from collections import OrderedDict

dicnry = {'Name': 'Pedro', 'Surname': 'Fernandes'}
dicnry2 = {'Surname': 'Fernandes', 'Name': 'Pedro'}

ordered = OrderedDict(dicnry)
ordered2 = OrderedDict(dicnry2)

print(dicnry == dicnry2)  # True
print(ordered == ordered2)  # False
