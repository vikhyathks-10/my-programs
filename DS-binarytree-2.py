# Height of Binary Tree
def height(root):
    if not root:
        return 0
    return 1 + max(height(root.left), height(root.right))

# Count Number of Nodes
def count_nodes(root):
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)

# Find Maximum Element
def find_max(root):
    if not root:
        return float('-inf')
    return max(root.data, find_max(root.left), find_max(root.right))

# Check if Two Trees are Identical
def is_identical(t1, t2):
    if not t1 and not t2:
        return True
    if t1 and t2:
        return (t1.data == t2.data and
                is_identical(t1.left, t2.left) and
                is_identical(t1.right, t2.right))
    return False

# Check if Tree is Balanced
def is_balanced(root):
    def check(root):
        if not root:
            return 0
        lh = check(root.left)
        rh = check(root.right)
        if lh == -1 or rh == -1 or abs(lh - rh) > 1:
            return -1
        return 1 + max(lh, rh)

    return check(root) != -1

# Level Order Traversal
from collections import deque

def level_order(root):
    if not root:
        return
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# Diameter of Binary Tree
def diameter(root):
    diameter = 0

    def height_d(root):
        nonlocal diameter
        if not root:
            return 0
        lh = height_d(root.left)
        rh = height_d(root.right)
        diameter = max(diameter, lh + rh)
        return 1 + max(lh, rh)

    height_d(root)
    return diameter

# Convert to Mirror Tree
def mirror(root):
    if root:
        root.left, root.right = root.right, root.left
        mirror(root.left)
        mirror(root.right)
