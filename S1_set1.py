# Problem 1: Build a Binary Tree I
# Given the following TreeNode class, create the binary tree depicted in the image below.
#   10
#  /  \
# 4    6


# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# # create the nodes
# root = TreeNode(10)
# root.left = TreeNode(4)
# root.right = TreeNode(6)


# Problem 2: 3-Node Sum I
# Given the root of a binary tree that has exactly 3 nodes: the root, its left child, and its right child, 
# return True if the value of the root is equal to the sum of the values of its two children. 
# Return False otherwise.
# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
#     if not root:
#         return False

#     return root.val == root.left.val + root.right.val
    

# root = TreeNode(10)
# root.left = TreeNode(4)
# root.right = TreeNode(6)

# result = check_tree(root)
# print(result)

# Example Input Tree #1: 
#   10
#  /  \
# 4    6
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   1
# Input: root = 5
# Expected Output: False


# Problem 3: 3-Node Sum II
# Given the root of a binary tree that has at most 3 nodes: the root, its left child, and its right child, 
# return True if the value of the root is equal to the sum of the values of its two children. 
# Return False otherwise.
# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def check_tree(root):
#     count = 0
#     if root.right:
#         count += root.right.val
#     if root.left:
#         count += root.left.val
    
#     return count == root.val

# # root = TreeNode(10)
# # root.left = TreeNode(10)

# root = TreeNode(5)
# root.left = TreeNode(3)
# root.right = TreeNode(2)
# result = check_tree(root)
# print(result)

# Example Input Tree #1: 
#   10
#  /  
# 10    
# Input: root = 10
# Expected Output: True

# Example Input Tree #2: 
#   5
#  / \
# 3   2
# Input: root = 5
# Expected Output: True

# Example Input Tree #3: 
#   5
#    \
#     2
# Input: root = 5
# Expected Output: False

# Example Input Tree #4: 
# Empty Tree (None)
# Input: root = None
# Expected Output: False

# Problem 4: Find Leftmost Node I
# Given the root of a binary tree, write a function that finds the value of the left most node in the tree.
# Evaluate the time complexity of your function.

# class TreeNode:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def left_most(root):
#     if not root:
#         return None
    
#     temp = root

#     while temp.left:
#         temp = temp.left
    
#     return temp.val
        

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(3)
# root.right = TreeNode(5)

# result = left_most(root)
# print(result)

# Example Input Tree #1: 

#       1
#      / \
#     /   \
#    2     5
#   / \    
#  4   3    

# Input: root = 1
# Expected Output: 4

# Example Input Tree #2: 

#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: 1

# Example Input Tree #3: 

# Input: root = None
# Output: None

# Problem 5: Find Leftmost Node II
# If you implemented the previous left_most() function iteratively, implement it recursively. 
# If you implemented it recursively, implement it iteratively.
# Evaluate the time complexity of the function.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if not root:
        return None
    
    if root.left:
        return left_most(root.left)
    
    return root.val


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(3)
root.right = TreeNode(5)

result = left_most(root)
print(result)

# Problem 6: In-order Traversal
# Given the root of a binary tree, return a list representing the inorder traversal of its nodes' values. 
# In an inorder traversal we traverse the left subtree, then the current node, then the right subtree.

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if not root:
        return []
    
    return inorder_traversal(root.left) + [root.value] 


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
result = inorder_traversal(root)

print(result)

# Example Input Tree #1: 
#      1
#       \
#        2
#       / 
#      3    

# Input: root = 1
# Expected Output: [1,3,2]

# Example Input Tree #2 : 

# Input: root = None
# Output: []

# Example Input Tree #3:
#     1  

# Input: root = 1
# Output: [1]