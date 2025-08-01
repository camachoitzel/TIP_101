# Problem 1: Level Order Traversal of Binary Tree
# Given the following pseudocode and the root of a binary tree, 
# return a list of the level order traversal of it’s nodes’ values (i.e., from left to right, level by level).
# Evaluate the time complexity of your solution. 
# Define your variables and give a rationale as to why you believe your solution has the stated time complexity.

from collections import deque 


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def level_order(root):
    # If the tree is empty:
    # return an empty list
    if not root:
        return [] 

    # Create an empty queue using deque
    queue = deque()

    # Create an empty list to store the explored nodes
    explored = []

    # Add the root to the queue
    queue.append(root)

    # While the queue is not empty:
    while queue:
        # Pop the next node off the queue (pop from the left side!)
        remove_left = queue.popleft()
        # Add the popped node to the list of explored nodes
        
        explored.append(remove_left.val)
        # Add each of the popped node's children to the end of the queue
        if remove_left.left:
            queue.append(remove_left.left)
        
        if remove_left.right:
            queue.append(remove_left.right)
    # Return the list of visited nodes
    return explored

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(level_order(root))
# Example Input Tree:

#       4
#      / \
#     2   6
#    / \  
#   1   3

# Example Input: root = 4
# Expected Output: [4, 2, 6, 1, 3]
# Explanation: 
# Level 1: Node 4
# Level 2 (left to right): Node 2, Node 6
# Level 3 (left to right): Node 1, Node 3


# Problem 2: Find Minimum Depth of Binary Tree
# Given the root of a binary tree, return its minimum depth. 
# The minimum depth is the number of nodes along the shortest path from the root down to the nearest leaf node.
# Evaluate the time complexity of your solution. 
# Define your variables and give a rationale as to why you believe your solution has the stated time complexity.