# 🔹 DAY 20 - ADVANCED LINKED LIST


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    # 🔹 Insert at End
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    # 🔹 Traverse
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


    # 🔹 1. Reverse Linked List
    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        self.head = prev


    # 🔹 2. Detect Loop (Floyd Cycle Detection)
    def detect_loop(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


    # 🔹 3. Find Middle Node
    def find_middle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow.data if slow else None


    # 🔹 5. Remove Duplicates (for sorted list)
    def remove_duplicates(self):
        temp = self.head

        while temp and temp.next:
            if temp.data == temp.next.data:
                temp.next = temp.next.next
            else:
                temp = temp.next


# 🔹 4. Merge Two Sorted Lists
def merge_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 if l1 else l2
    return dummy.next


# 🔹 MAIN PROGRAM

ll = LinkedList()
ll.insert_end(1)
ll.insert_end(2)
ll.insert_end(3)
ll.insert_end(4)

print("\n--- Original List ---")
ll.traverse()


print("\n--- Reverse Linked List ---")
ll.reverse()
ll.traverse()


print("\n--- Detect Loop ---")
print("Loop Exists:", ll.detect_loop())


print("\n--- Find Middle Node ---")
print("Middle:", ll.find_middle())


print("\n--- Remove Duplicates ---")
ll2 = LinkedList()
ll2.insert_end(1)
ll2.insert_end(1)
ll2.insert_end(2)
ll2.insert_end(2)
ll2.insert_end(3)
ll2.remove_duplicates()
ll2.traverse()


print("\n--- Merge Two Lists ---")
l1 = LinkedList()
l1.insert_end(1)
l1.insert_end(3)

l2 = LinkedList()
l2.insert_end(2)
l2.insert_end(4)

merged_head = merge_lists(l1.head, l2.head)

temp = merged_head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")