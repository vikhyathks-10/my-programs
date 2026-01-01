# 6. First non-repeating character in stream
from collections import deque

def first_non_repeating(stream):
    freq = {}
    q = deque()

    for ch in stream:
        freq[ch] = freq.get(ch, 0) + 1
        q.append(ch)

        while q and freq[q[0]] > 1:
            q.popleft()

        print(q[0] if q else -1, end=" ")
    print()

# 7. Priority Queue
import heapq

pq = []
heapq.heappush(pq, 30)
heapq.heappush(pq, 10)
heapq.heappush(pq, 20)

print(heapq.heappop(pq))   # highest priority (smallest)

# 8. Generate binary numbers from 1 to n
def generate_binary(n):
    q = deque()
    q.append("1")

    for i in range(n):
        curr = q.popleft()
        print(curr, end=" ")
        q.append(curr + "0")
        q.append(curr + "1")
    print()

# 9. Deque operations
d = deque()
d.append(10)
d.appendleft(5)
d.pop()
d.popleft()

# 10. Sliding window maximum
def sliding_window_max(arr, k):
    dq = deque()
    result = []

    for i in range(len(arr)):
        while dq and dq[0] <= i - k:
            dq.popleft()

        while dq and arr[dq[-1]] < arr[i]:
            dq.pop()

        dq.append(i)

        if i >= k - 1:
            result.append(arr[dq[0]])

    return result


# --------- Testing ----------
first_non_repeating("aabc")
generate_binary(5)
print(sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
