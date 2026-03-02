# =====================================
# 1️⃣ String + Function Program
# =====================================
def string_analysis(text):
    length = len(text)
    vowels = sum(1 for ch in text.lower() if ch in "aeiou")
    reversed_text = text[::-1]

    print("\nString Analysis")
    print("Length:", length)
    print("Vowels:", vowels)
    print("Reversed:", reversed_text)

text = input("Enter a string: ")
string_analysis(text)


# =====================================
# 2️⃣ List + Function Program
# =====================================
def list_analysis(lst):
    print("\nList Analysis")
    print("Sum:", sum(lst))
    print("Maximum:", max(lst))
    print("Minimum:", min(lst))

n = int(input("\nEnter number of elements in list: "))
numbers = [int(input(f"Enter element {i+1}: ")) for i in range(n)]
list_analysis(numbers)


# =====================================
# 3️⃣ Dictionary + Function Program
# =====================================
def dictionary_analysis(d):
    print("\nDictionary Analysis")
    print("Keys:", list(d.keys()))
    print("Values:", list(d.values()))
    print("Total items:", len(d))

d = {}
m = int(input("\nEnter number of key-value pairs: "))
for i in range(m):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

dictionary_analysis(d)


# =====================================
# 4️⃣ Menu-Driven Mini Project (Simple Calculator)
# =====================================
def calculator():
    while True:
        print("\nCalculator Menu")
        print("1.Add  2.Sub  3.Mul  4.Div  5.Exit")

        choice = int(input("Enter choice: "))

        if choice == 5:
            break

        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == 1:
            print("Result:", a + b)
        elif choice == 2:
            print("Result:", a - b)
        elif choice == 3:
            print("Result:", a * b)
        elif choice == 4:
            if b != 0:
                print("Result:", a / b)
            else:
                print("Division not allowed")
        else:
            print("Invalid choice")

calculator()


# =====================================
# 5️⃣ Quiz System
# =====================================
def quiz():
    questions = {
        "What is 2 + 2?": "4",
        "Capital of India?": "Delhi",
        "Python is a language? (yes/no)": "yes"
    }

    score = 0

    for question, answer in questions.items():
        user_answer = input("\n" + question + " ")
        if user_answer.strip().lower() == answer.lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")

    print("\nFinal Score:", score, "/", len(questions))

quiz()