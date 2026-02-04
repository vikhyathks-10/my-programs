# 6️⃣ Function to return number of digits
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

print("Number of digits:", count_digits(45678))


# 7️⃣ Function to return GCD of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

print("GCD:", gcd(24, 36))


# 8️⃣ Function to return LCM of two numbers
def lcm(a, b):
    return (a * b) // gcd(a, b)

print("LCM:", lcm(12, 15))


# 9️⃣ Function to calculate simple interest
def simple_interest(p, r, t):
    return (p * r * t) / 100

print("Simple Interest:", simple_interest(1000, 5, 2))


# 🔟 Function to return power (xⁿ)
def power(x, n):
    result = 1
    for i in range(n):
        result *= x
    return result

print("Power:", power(2, 5))
