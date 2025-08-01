marks = list(map(int, input("Enter marks separated by space: ").split()))

minimum = min(marks)
maximum = max(marks)
average = sum(marks) / len(marks)

print(f"\nLowest Mark : {minimum}")
print(f"Highest Mark: {maximum}")
print(f"Average     : {average:.2f}")
