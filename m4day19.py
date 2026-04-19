# 🔹 DAY 19 - LINKED LIST


# 🔹 Node Class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 🔹 Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None


    # 🔹 Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    # 🔹 Insert at End
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node


    # 🔹 Delete Node
    def delete(self, key):
        temp = self.head

        # if head is to be deleted
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found")
            return

        prev.next = temp.next
        temp = None


    # 🔹 Traverse List
    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# 🔹 MAIN PROGRAM

ll = LinkedList()

print("\n--- Insert at Beginning ---")
ll.insert_beginning(10)
ll.insert_beginning(20)
ll.traverse()

print("\n--- Insert at End ---")
ll.insert_end(30)
ll.insert_end(40)
ll.traverse()

print("\n--- Delete Node ---")
ll.delete(20)
ll.traverse()

print("\n--- Final Traversal ---")
ll.traverse()