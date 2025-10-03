scores = {'Alice': 90, 'Bob': 75, 'Charlie': 85}
sorted_dict = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))

print("Sorted by values:", sorted_dict)
