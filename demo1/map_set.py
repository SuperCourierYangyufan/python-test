map = {'a': 1, 'b': 2, 'c': 3}
print(map['a'])

map['a'] = 20
print(map['a'])
print('d' in map)
print('b' in map)

print(map.get('b'))
print(map.get('d', 'hello'))

print(map.pop('c'))
print(map)

sets = set([2, 4, 3, 3, 1])
sets.add(-1)
sets.remove(4)
print(sets)

