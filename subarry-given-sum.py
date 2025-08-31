arr = [1, 4, 20, 3, 10, 5]
k = 33
current_sum = 0
start = 0

for end in range(len(arr)):
    current_sum += arr[end]
    while current_sum > k:
        current_sum -= arr[start]
        start += 1
    if current_sum == k:
        print("Subarray with sum", k, ":", arr[start:end+1])
        break
