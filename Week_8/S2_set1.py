# Problem 1: Is Uni-valued
# A binary tree is uni-valued if every node in the tree has the same value. 
# Given the root of a binary tree, return True if the given tree is uni-valued and False otherwise.
# Evaluate the time complexity of your solution.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
         
# def is_univalued(root):
#     if not root:
#         return True
    
#     if root.left and  root.left.val != root.val:
#          return False
#     if root.right and  root.right.val != root.val:
#          return False
    
#     return is_univalued(root.left) and is_univalued(root.right)
         

# root = TreeNode(1)
# root.left = TreeNode(1)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(1)

# root.right = TreeNode(1)
# root.right.right = TreeNode(1)

# print(is_univalued(root))


# Example Input Tree #1

#       1
#      / \
#     /   \
#    1     1
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: True

# Example Input Tree #2

#       1
#      / \
#     /   \
#    1     2
#   / \     \
#  1   1     1

# Input: root = 1
# Expected Output: False

# Problem 2: Binary Tree Height
# Given the root of a binary tree, write a function height() that returns the height of a binary tree.
# Evaluate the time complexity of your function.

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right
   
# def height(root):
#     if not root:
#         return 0
    
#     left = height(root.left)
#     right = height(root.right)

#     if left > right:
#         return left + 1
#     else:
#         return right + 1
    


# root = TreeNode(4)
# root.left = TreeNode(2)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(3)

# root.right = TreeNode(5)

# print(height(root))

# Example Input Tree #1

#       4
#      / \
#     /   \
#    2     5
#   / \    
#  1   3    

# Input: root = 4
# Expected Output: 3

# Example Input Tree #2 

#       4 

# Input: root = 4
# Expected Output: 1

# Problem 3: BST Insert
# Given the root of a binary search tree, insert a new node with a given key and value into the tree. Return the root of the modified tree. 
# The tree is sorted by key. 
# If a node with the given key already exists, update the the existing key’s value. You do not need to maintain a balanced tree.
# Evaluate the time complexity of your function.


# class TreeNode():
#      def __init__(self, key, value, left=None, right=None):
#             self.key = key
#             self.val = value
#             self.left = left
#             self.right = right
   
# def insert(root, key, value):
#     if not root:
#         return TreeNode(key, value)
    
#     # compare the key to the root
#     # recursively compare either left or right
    
#     if key > root.key:
#          insert(root.right, key,  value)
#     elif key < root.key:
#          insert(root.left, key, value)

#     else:
#          root.val = value

#     return root.key
        

# root = TreeNode(10, 'hi')
# root.left = TreeNode(5, 'hello')
# root.right = TreeNode(15, 'hola')
# root.left.left = TreeNode(1, 'y')
# root.left.right = TreeNode(6, 'z')

# print(insert(root, 9, 'Naruto'))

# Example Input Tree #1: (tree depicted using keys)

#       10
#      /  \
#     /    \
#    5      15
#   / \    
#  1   6    

# Input: root = 10, key = 9, value = 'Naruto' 
# Expected Output: root = 10
# Expected Output Tree:

#       10
#      /  \
#     /    \
#    5      15
#   / \    
#  1   6
#       \
#        9    


# Example Input Tree #2: Empty Tree (None)

# Input: root = None, key = 4, value = "Sailor Moon"
# Expected Output: root = 4
# Expected Output Tree:

#       4

# Problem 4: BST Remove I
# Use the provided pseudocode to solve the problem below. Given a key and the root of a binary search tree, 
# remove the node with the given key. Return the root of the modified tree.
# The tree is sorted by key. If multiple nodes with the given key exist, 
# remove the first node you find.
# If you need to remove a node with two children, use the in-order successor of that node, 
# which is the smallest value in its right subtree. 
# You do not need to maintain a balanced tree.
# Evaluate the time complexity of your function.

class TreeNode():
     def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.val = value
        self.left = left
        self.right = right
         
def remove_bst(root, key):
    # Remove a node with a given key from the BST and return the new root.
  
    if not root:
        return None

    # Find the node to delete
    if key < root.val:
        root.left = remove_bst(root.left, key)
    elif key > root.val:
        root.right = remove_bst(root.right, key)
    else:
        # Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children, get the in-order successor (smallest in the right subtree)
        temp_val = find_min(root.right)
        root.val = temp_val
        root.right = remove_bst(root.right, temp_val)

    return root

def find_min(node):
    # Find the smallest value in the BST.
    
    current = node
    while current.left is not None:
        current = current.left
    return current.val

root = TreeNode(10, 'hi')
root.left = TreeNode(5, 'hello')
root.right = TreeNode(15, 'hola')
root.left.left = TreeNode(1, 'a')
root.left.right = TreeNode(8, 'b')
root.right.left = TreeNode(13, 'c')
root.right.right = TreeNode(16, 'd')