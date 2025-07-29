# Unit test 8 

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

# def find(root, target):
#      if not root:
#           return False
     
#      if root.val == target:
#           return True
#     # changed and to or b/c in the and case both left and right have to be the target value which will never be true
#      return find(root.left, target) or find(root.right, target)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# print(find(root, 3))

# class TreeNode():
#      def __init__(self, value, left=None, right=None):
#          self.val = value
#          self.left = left
#          self.right = right

# # i think this function return num of nodes in a tree
# def mys_func(root):
#      if not root:
#           return 0
     
#      return 1 + mys_func(root.left) + mys_func(root.right)

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)

# print(mys_func(root))


# complete insert Function
# class TreeNode():
#      def __init__(self, val = 0, left=None, right=None):
#          self.val = val
#          self.left = left
#          self.right = right

# def insert(root, val):
#     if not root:
#          return TreeNode(val)
    
#     if val > root.val:
#          root.right = insert(root.right, val)
#     elif val < root.val:
#         root.left = insert(root.left, val)

#     return root
    # if not root:
    #     return TreeNode(key, value)
    
    # # compare the key to the root
    # # recursively compare either left or right
    
    # if key > root.key:
    #      insert(root.right, key,  value)
    # elif key < root.key:
    #      insert(root.left, key, value)

    # else:
    #      root.val = value

    # return root.key

# root = TreeNode(3)
# root.left = TreeNode(2)
# root.right = TreeNode(4)

# insert(root, 5)
# print(root.val)


# Example Input Tree: 

#      3
#     / \
#    2   4


# Input: root = 3, val = 5
# Expected Output: root = 3

#      3
#     / \
#    2   4
#         \
#          5


# Given the root of a binary tree, return the sum of all it's nodes' values
# You may assume all values are integers

class TreeNode():
     def __init__(self, val = 0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def sum_tree(root):
     if not root:
          return 0
     
     return root.val + sum_tree(root.right) + sum_tree(root.left)


root = TreeNode(1)
root.left = TreeNode(5)
root.right = TreeNode(2)
root.right.right = TreeNode(4)
root.right.left = TreeNode(3)

print(sum_tree(root))

# Example Input Tree: 
# """For example:
#      1
#       \
#        2
#       / 
#      3    
# """
# Input: root = 1
# Expected Output: 6

# Input: root = None
# Output: 0

# Example Input Tree
# """ 1 """ 
# Input: root = 1
# Output: 1

# remove Node from BST
class TreeNode():
     def __init__(self, val = 0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def remove_node(root, value):
    if not root:
        return None
    
    if value < root.val:
        root.left = remove_node(root.left, value)
    
    elif value > root.val:
        root.right = remove_node(root.right, value)
    
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
    
        temp_val = find_min(root.right)
        root.val = temp_val
        root.right = remove_node(root.right, temp_val)
    
    return root

def find_min(node):
    # Find the smallest value in the BST.
    
    current = node
    while current.left is not None:
        current = current.left
    return current.val



# Example Input Tree:
#       7
#      / \
#     3  10
#        / \
#       8  12
# Input: root = 7, val = 10
# Expected Output: root = 7
# Expected output tree:
#       7
#      / \
#     3   12
#        /
#       8   
#
# Note: In-order successor of 10 is 12