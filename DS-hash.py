# 1. Hash Table using Dictionary
hash_table = {}

hash_table["name"] = "Vikyat"
hash_table["age"] = 19
hash_table["course"] = "B.Tech CSE"

print("Hash Table:", hash_table)


# 2. First Repeating Element using Hashing
def first_repeating(arr):
    seen = set()
    for x in arr:
        if x in seen:
            return x
        seen.add(x)
    return -1

arr = [10, 5, 3, 4, 3, 5, 6]
print("First Repeating Element:", first_repeating(arr))

# 3. LRU Cache Implementation
from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value

        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)


# --------- Testing ----------
lru = LRUCache(2)
lru.put(1, "A")
lru.put(2, "B")
print(lru.get(1))   # A
lru.put(3, "C")     # removes key 2
print(lru.get(2))   # -1
