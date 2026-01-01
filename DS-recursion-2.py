# 7. Print all permutations of a string

def permutations(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        permutations(s[:i] + s[i+1:], ans + s[i])

# 8. Tower of Hanoi
def tower_of_hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    tower_of_hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, helper, source, destination)

# 9. Generate all subsets of a set
def subsets(arr, index=0, current=[]):
    if index == len(arr):
        print(current)
        return
    subsets(arr, index + 1, current)
    subsets(arr, index + 1, current + [arr[index]])

# 10. GCD using recursion
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


# Test the functions
print("Permutations:")
permutations("ABC")

print("\nTower of Hanoi:")
tower_of_hanoi(3, "A", "B", "C")

print("\nSubsets:")
subsets([1, 2, 3])

print("\nGCD:", gcd(36, 24))
