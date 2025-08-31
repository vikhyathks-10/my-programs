# Rearrange Positive and Negative Numbers Alternately
def rearrange(arr):
    n = len(arr)
    # Separate positive and negative numbers
    pos = [x for x in arr if x >= 0]
    neg = [x for x in arr if x < 0]
    # Merge them alternately
    result = []
    i, j = 0, 0
    while i < len(pos) and j < len(neg):
        result.append(pos[i])
        result.append(neg[j])
        i += 1
        j += 1
    # Append any remaining elements from either list
    result.extend(pos[i:])
    result.extend(neg[j:])
    return result

# Example usage
arr = [1, -2, 3, -4, 5, -6]
print("Rearranged Array:", rearrange(arr))