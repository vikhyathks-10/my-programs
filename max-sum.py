#Maximum Sum of Non-Adjacent Elements (House Robber)
#Use DP: dp[i] = max(dp[i-1], dp[i-2] + nums[i]).
def max_sum_non_adjacent(nums):
    incl = 0
    excl = 0
    for i in range(len(nums)):
        new_excl = max(incl, excl)
        incl = excl + nums[i]
        excl = new_excl
    return max(incl, excl)

# Example usage
arr = [3, 2, 5, 10, 7]
print("Maximum Sum of Non-Adjacent Elements:", max_sum_non_adjacent(arr))