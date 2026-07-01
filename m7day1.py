# ==========================================================
# Month 7 - Day 1
# Python Interview Basics I
#
# Topics Covered:
# 1. List vs Tuple Comparison
# 2. Mutable vs Immutable Objects
# # 3. Identity (is) vs Equality (==)
# 4. pass vs continue vs break
# 5. Variable Scope (Local & Global)
# 6. Global Keyword Practice
# ==========================================================

print("=" * 60)
print("1. LIST vs TUPLE")
print("=" * 60)

my_list = [10, 20, 30]
my_tuple = (10, 20, 30)

print("List :", my_list)
print("Tuple:", my_tuple)

# List is mutable
my_list.append(40)
print("After appending to list:", my_list)

# Tuple is immutable
try:
    my_tuple += (40,)
    print("Tuple after concatenation:", my_tuple)
except TypeError:
    print("Tuple cannot be modified.")


print("\n" + "=" * 60)
print("2. MUTABLE vs IMMUTABLE")
print("=" * 60)

# Mutable Example
numbers = [1, 2, 3]
another = numbers

another.append(4)

print("numbers :", numbers)
print("another :", another)

# Immutable Example
a = 100
b = a
b += 1

print("\na =", a)
print("b =", b)

print("\nLists are mutable.")
print("Integers are immutable.")


print("\n" + "=" * 60)
print("3. IDENTITY (is) vs EQUALITY (==)")
print("=" * 60)

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x =", x)
print("y =", y)
print("z =", z)

print("\nx == y :", x == y)
print("x is y :", x is y)

print("\nx == z :", x == z)
print("x is z :", x is z)


print("\n" + "=" * 60)
print("4. pass vs continue vs break")
print("=" * 60)

print("\npass Example")
for i in range(5):
    if i == 2:
        pass
    print(i)

print("\ncontinue Example")
for i in range(5):
    if i == 2:
        continue
    print(i)

print("\nbreak Example")
for i in range(5):
    if i == 2:
        break
    print(i)


print("\n" + "=" * 60)
print("5. VARIABLE SCOPE (Local & Global)")
print("=" * 60)

message = "I am Global"

def show_scope():
    message = "I am Local"
    print("Inside Function :", message)

show_scope()

print("Outside Function:", message)


print("\n" + "=" * 60)
print("6. GLOBAL KEYWORD")
print("=" * 60)

count = 0

def increment():
    global count
    count += 1
    print("Inside Function Count =", count)

increment()
increment()
increment()

print("Outside Function Count =", count)

print("\n" + "=" * 60)
print("INTERVIEW SUMMARY")
print("=" * 60)

print("""
✔ List
  - Mutable
  - Uses []
  - Can add/remove/update elements

✔ Tuple
  - Immutable
  - Uses ()
  - Faster than list
  - Hashable (if elements are immutable)

✔ Mutable Objects
  - List
  - Dictionary
  - Set

✔ Immutable Objects
  - int
  - float
  - string
  - tuple
  - frozenset

✔ == compares VALUES

✔ is compares MEMORY ADDRESS

✔ pass
  - Does nothing

✔ continue
  - Skips current iteration

✔ break
  - Terminates loop immediately

✔ Local Variable
  - Exists only inside a function

✔ Global Variable
  - Exists throughout the program

✔ global keyword
  - Allows modifying a global variable inside a function
""")