scores = {'Alice': 88, 'Bob': 75, 'Charlie': 95}
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1]))

print("Sorted by values:", sorted_scores)
