#Minimum Number of Jumps to Reach End
#Use greedy approach: track farthest and steps left.
def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                break
    return jumps

# Example usage
arr = [2, 3, 1, 1, 4]
print("Minimum Jumps to Reach End:", min_jumps(arr))