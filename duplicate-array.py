#Use Floyd's cycle detection (tortoise & hare).
# It uses two pointers moving at different speeds (slow and fast) to determine whether a cycle (loop) exists in a sequence.

def find_duplicate(nums):
    # Phase 1: Finding the intersection point
    slow = fast = 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    # Phase 2: Finding the entrance to the cycle
    slow = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

# Example usage
nums = [1, 3, 4, 2, 2]
print("Duplicate Number:", find_duplicate(nums))