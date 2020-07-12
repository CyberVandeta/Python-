dict = {}
dict[1] = 100
dict['two'] = 'two hundred'
print(dict.items())
dict.pop(1)
print(dict)

nest = {1: {2: {3: 4}}}
print(nest[1])
print(nest[1][2])
print(nest[1][2][3])
print(nest.keys())
print(nest.items())
print(nest.values())