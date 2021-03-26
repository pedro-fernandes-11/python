# Dict subclass that calls a factory function to supply missing values
from collections import defaultdict


def no_return():
    return "No value"


dicnry = defaultdict(no_return)

dicnry["name"] = 'Pedro Pouzada Fernandes'
print(dicnry['age'])  # returns the default value
print(dicnry)
