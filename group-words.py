words = ["apple", "bat", "ball", "cat", "banana"]
grouped = {}

for w in words:
    grouped.setdefault(len(w), []).append(w)

print("Grouped by length:", grouped)
