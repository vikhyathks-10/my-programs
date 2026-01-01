"""interview Coding Questions in Python
Implement a Min-Heap

import heapq

class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, val)

    def extract_min(self):
        if self.heap:
            return heapq.heappop(self.heap)
        return None

    def get_min(self):
        if self.heap:
            return self.heap[0]
        return None

# Example
h = MinHeap()
h.insert(5)
h.insert(3)
h.insert(8)
print("Min:", h.get_min())       # Output: 3
print("Extract Min:", h.extract_min())  # Output: 3
print("Min now:", h.get_min())   # Output: 5

Implement a Max-Heap

import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        heapq.heappush(self.heap, -val)  # invert value for max-heap

    def extract_max(self):
        if self.heap:
            return -heapq.heappop(self.heap)
        return None

    def get_max(self):
        if self.heap:
            return -self.heap[0]
        return None

# Example
h = MaxHeap()
h.insert(5)
h.insert(3)
h.insert(8)
print("Max:", h.get_max())       # Output: 8
print("Extract Max:", h.extract_max())  # Output: 8
print("Max now:", h.get_max())   # Output: 5

Implement a Trie (Prefix Tree)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Example
trie = Trie()
trie.insert("hello")
trie.insert("helium")
print(trie.search("hello"))   # True
print(trie.search("helix"))   # False
print(trie.starts_with("he")) # True

Find the Kth Largest Element in an Array

import heapq

def kth_largest(nums, k):
    return heapq.nlargest(k, nums)[-1]

# Example
arr = [3,2,1,5,6,4]
print(kth_largest(arr, 2))  # Output: 5

Find the Kth Smallest Element in an Array

import heapq

def kth_smallest(nums, k):
    return heapq.nsmallest(k, nums)[-1]

# Example
arr = [3,2,1,5,6,4]
print(kth_smallest(arr, 2))  # Output: 2
Print All Prime Factors of a Number
def prime_factors(n):
    factors = []
    # Factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # Factor odd numbers
    i = 3
    while i*i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    if n > 2:
        factors.append(n)
    return factors

# Example
print(prime_factors(84))  # Output: [2, 2, 3, 7]

Print Pascal’s Triangle Using Recursion
def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        result = pascal_triangle(n-1)
        last = result[-1]
        new_row = [1] + [last[i] + last[i+1] for i in range(len(last)-1)] + [1]
        result.append(new_row)
        return result

# Example
n = 5
for row in pascal_triangle(n):
    print(row)

Check if a String is a Valid Shuffle of Two Strings
def is_valid_shuffle(s1, s2, result):
    i = j = k = 0
    while k < len(result):
        if i < len(s1) and s1[i] == result[k]:
            i += 1
        elif j < len(s2) and s2[j] == result[k]:
            j += 1
        else:
            return False
        k += 1
    return i == len(s1) and j == len(s2)

# Example
print(is_valid_shuffle("abc", "def", "adbcef"))  # True
print(is_valid_shuffle("abc", "def", "abdecf"))  # False

Find the Longest Common Subsequence (LCS)
def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # Reconstruct LCS
    i, j = m, n
    lcs_str = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs_str.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs_str))

# Example
print(lcs("AGGTAB", "GXTXAYB"))  # Output: "GTAB"

Find Longest Common Prefix
def longest_common_prefix(strs):
    if not strs:
        return ""
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix
# Example
print(longest_common_prefix(["flower","flow","flight"]))  # Output: "fl"
"""