# Palindrome check ignoring spaces and case
text = "A man a plan a canal Panama"
cleaned = text.replace(" ", "").lower()

if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
