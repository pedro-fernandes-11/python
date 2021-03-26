"""
Sets don't allow duplicated values, there's no index for the values
"""

s = {99, 12, 3, 99, 1, 131, 1, 3, 5}
print(s)

_list = [1, 2, 3, 4, 5]

dic = {}.fromkeys(_list, 'teste')
print(set(dic))

cities = ['Cachoeirinha', 'Gravataí', 'Porto Alegre', 'Gravataí', 'Cachoeirinha']
print(len(cities))  # How many cities
print(len(set(cities)))  # Distinct cities

# Adding values to the set
s.add(6)
print(s)

# Removing from the set
s.remove(6)  # If it's not a set key, returns error
s.discard(6)  # If it's not a set key, it's ignored
print(s)

s.clear()  # Clear the set
print(s)

# Copying: Deep Copy (new = s.copy()) and Shallow Copy (new = s)

# Math methods:
A = {1, 2, 3, 4, 5, 6, 7}
B = {4, 5, 6, 7, 8, 9, 10}

# AUB (A union with B):
union = A.union(B)
union2 = A | B
print(union, union2)

# A∩B (A intersection with B):
intersection = A.intersection(B)
intersection2 = A & B
print(intersection, intersection2)

# A - B
only_a = A.difference(B)
print(only_a)

# sum(), max(), min(), len() methods
s = {4, 6, 2, 17, 32, 4}
print(sum(s))
print(min(s))
print(max(s))
print(len(s))
