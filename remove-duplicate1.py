d = {'a': 1, 'b': 2, 'c': 2, 'd': 3}
unique = {}

for k, v in d.items():
    if v not in unique.values():
        unique[k] = v

print("After removing duplicates:", unique)
