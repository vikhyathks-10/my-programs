# Singly Linked List - Basic Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

# 1. Insert at beginning
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

# 2. Insert at end
    def insert_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

# 3. Delete node by value
    def delete_by_value(self, value):
        temp = self.head
        if temp and temp.data == value:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

# 4. Find length of linked list
    def length(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

# 5. Display list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# -Testing -
ll = SinglyLinkedList()
ll.insert_begin(10)
ll.insert_end(20)
ll.insert_end(30)
ll.insert_begin(5)
ll.display()
print("Length:", ll.length())
ll.delete_by_value(20)
ll.display()
