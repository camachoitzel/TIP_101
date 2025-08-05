# Unit 9 test
from collections import deque 

# class TreeNode:
#     def __init__(self, key, value, left = None, right = None):
#         self.key = key
#         self.val = value
#         self.left = left
#         self.right = right
    
# def mys_func(root, key):
#     if root is None:
#         return TreeNode(key, value)
    
#     if key < root.key:
#         root.left = mys_func(root.left , key , value)
#     elif key > root.key:
#         root.right = mys_func(root.right , key , value)
#     else:
#         root.val = value 
    
#     return root


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

# def level_order(root):
#     if not root:
#         return
    
#     queue = deque([root])

#     result = []

#     while queue:
#         node = queue.popleft()
#         result.append(node.val)

#         if node.left:
#             queue.append(node.left)
            
#         if node.right:
#             queue.append(node.right)
           
#     return result

# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)

# print(level_order(root))

# def sum_left_leaves(root):
#     if root is None:
#         return 0
    
#     left_sum =  0
    
#     if root.left and not root.left.left and not root.left.right:
#         left_sum += root.left.val
    
#     left_sum += sum_left_leaves(root.left)
#     left_sum += sum_left_leaves(root.right)

#     return left_sum

# root = TreeNode(3)
# root.left = TreeNode(9)
# root.right = TreeNode(20)
# root.right.left = TreeNode(15)
# root.right.right = TreeNode(24)

# output = sum_left_leaves(root)
# print(output)

def find_target(root, k):
    if not root:
        return False
    
    queue = deque([root])

    # empty set to store visited values
    seen = set()

    while queue:
        node = queue.popleft()
        complement = k - node.val

        if complement in seen:
            return True
        
        seen.add(node.val)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return False



root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

result = find_target(root, 9)
result_2 = find_target(root, 28)

print(result)
print(result_2)