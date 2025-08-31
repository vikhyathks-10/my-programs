#Rotate Array by K Positions
def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    arr[:] = arr[-k:] + arr[:-k]  # Rotate the array in place
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
k = 2
print("Original Array:", arr)
print("Rotated Array:", rotate_array(arr, k))
