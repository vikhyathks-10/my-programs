arr = [1, 2, 3, 2, 1]
is_palindrome = True

for i in range(len(arr) // 2):
    if arr[i] != arr[-(i + 1)]:
        is_palindrome = False
        break

print("Palindrome:", is_palindrome)
