# Mock-Interview

# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

from collections import deque 

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    if not root:
        return True
    
    queue = deque([root.left, root.right])
    
    while queue:
        remove_left = queue.popleft()
        remove_right = queue.popleft()


        if remove_left == None and remove_right == None:
            continue
        elif remove_left == None or remove_right == None:
            return False
        
        queue.appendleft((remove_left.left, remove_right.right))
        queue.appendleft((remove_left.right, remove_right.left))

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