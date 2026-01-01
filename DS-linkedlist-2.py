# Singly Linked List Advanced Operations
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 6. Reverse linked list (iterative)
def reverse_iterative(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev

# 7. Reverse linked list (recursive)
def reverse_recursive(head):
    if not head or not head.next:
        return head
    rest = reverse_recursive(head.next)
    head.next.next = head
    head.next = None
    return rest

# 8. Find middle element
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.data

# 9. Detect loop (Floyd’s Cycle)
def detect_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

# 10. Remove loop
def remove_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
            fast.next = None
            return

# 11. Find nth node from end
def nth_from_end(head, n):
    first = second = head
    for _ in range(n):
        first = first.next
    while first:
        first = first.next
        second = second.next
    return second.data

# 12. Check if palindrome
def is_palindrome(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp:
        if temp.data != stack.pop():
            return False
        temp = temp.next
    return True
