"""
LCM of a List of Numbers

from math import gcd

def lcm(a,b):
    return a*b//gcd(a,b)

from functools import reduce
def lcm_list(lst):
    return reduce(lcm, lst)

print(lcm_list([4,5,10]))  # Output: 20


Simplify a Fraction Using GCD

def simplify_fraction(numer, denom):
    g = gcd(numer, denom)
    return (numer//g, denom//g)

print(simplify_fraction(8,12))  # Output: (2,3)

Pascal’s Triangle Variations

Print Only the nth Row

def pascal_nth_row(n):
    row = [1]
    for _ in range(n):
        row = [sum(pair) for pair in zip([0]+row, row+[0])]
    return row

print(pascal_nth_row(4))  # Output: [1,4,6,4,1]


Binomial Coefficient (nCr) Using Pascal’s Triangle

def nCr(n,r):
    row = pascal_nth_row(n)
    return row[r]

print(nCr(5,2))  # Output: 10

Missing & Duplicate Numbers Variations

Find All Missing Numbers in a List

def find_missing(nums, n):
    return [i for i in range(1,n+1) if i not in nums]

print(find_missing([1,3,4],4))  # Output: [2]


Find Single Number Appearing Once

def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

print(single_number([2,2,1]))  # Output: 1


Find Duplicate Numbers Without count()

def find_duplicates(nums):
    seen = set()
    duplicates = set()
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)

print(find_duplicates([1,2,3,2,1,4]))  # Output: [1,2]

Rotate Array Variations

Rotate Array Left

def rotate_left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]

print(rotate_left([1,2,3,4,5],2))  # Output: [3,4,5,1,2]


Rotate Array In-Place Without Extra Space

def rotate_inplace(arr, k):
    n = len(arr)
    k %= n
    arr[:] = arr[::-1]
    arr[:k] = arr[:k][::-1]
    arr[k:] = arr[k:][::-1]
    return arr

print(rotate_inplace([1,2,3,4,5],2))  # Output: [3,4,5,1,2]


Rotate a String Instead of Number List

def rotate_string(s, k):
    k %= len(s)
    return s[-k:] + s[:-k]
print(rotate_string("hello",2))  # Output: "lohel"
 """