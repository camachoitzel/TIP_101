# Problem 1: Is Symmetric Tree
# Given the root of a binary tree, 
# return True if the tree’s left and right subtrees are mirrors of each other (i.e., tree is symmetric around its center). 
# Return False otherwise.
# Evaluate the time complexity of your function.

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    # create a left and right var that will hold the curr left and right val
    left = 0
    right = 0
    pass


# Example Tree #1:

#        1
#      /   \
#     /     \
#    2       2
#   / \     / \
#  3   4   4   3
#            |
 

# Input: root = 1
# Expected Output: True


# Example Tree #2:

#         1
#       /   \
#      /     \
#     2       2
#      \       \
#       3       3
         

# Input: root = 1
# Expected Output: False