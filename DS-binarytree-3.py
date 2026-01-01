# BST Node
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Insert into BST
def insert(root, key):
    if not root:
        return BSTNode(key)
    if key < root.data:
        root.left = insert(root.left, key)
    elif key > root.data:
        root.right = insert(root.right, key)
    return root

# Search in BST
def search(root, key):
    if not root or root.data == key:
        return root
    if key < root.data:
        return search(root.left, key)
    return search(root.right, key)

# Find Minimum Value Node
def min_value_node(root):
    curr = root
    while curr.left:
        curr = curr.left
    return curr

# Delete from BST
def delete(root, key):
    if not root:
        return root

    if key < root.data:
        root.left = delete(root.left, key)
    elif key > root.data:
        root.right = delete(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete(root.right, temp.data)

    return root

# Inorder Traversal (BST)
def inorder_bst(root):
    if root:
        inorder_bst(root.left)
        print(root.data, end=" ")
        inorder_bst(root.right)


# --------- Testing ----------
bst_root = None
for val in [50, 30, 70, 20, 40, 60, 80]:
    bst_root = insert(bst_root, val)

print("BST Inorder:")
inorder_bst(bst_root)

bst_root = delete(bst_root, 50)
print("\nAfter Deletion:")
inorder_bst(bst_root)
