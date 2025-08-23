file_name = "sample.txt"  # Make sure file exists
with open(file_name, 'r') as f:
    words = f.read().split()
print("Number of words:", len(words))
