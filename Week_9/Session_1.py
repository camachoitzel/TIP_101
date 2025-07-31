# Instructor Demo
# Binary Tree Traversal


class TreeNode(object):
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def printInOrder(root):
    result = []

    # Left -> Root -> Right
    def inOrderHelper(node):
        nonlocal result
        if not node:
            return
        # recurse left
        inOrderHelper(node.left)
        # append the value to result list
        result.append(node.val)
        # recurse right
        inOrderHelper(node.right)


    inOrderHelper(root)
    print(result)


tree = TreeNode(5, TreeNode(4, TreeNode(3)) , TreeNode(8, TreeNode(7, TreeNode(9))))
printInOrder(tree)

def printPreOrder(root):
    result = []

    # Left -> Root -> Right
    def preOrderHelper(node):
        nonlocal result
        if not node:
            return
        # append the value to result list
        result.append(node.val)
        # recurse left
        preOrderHelper(node.left)
        # recurse right
        preOrderHelper(node.right)


    preOrderHelper(root)
    print(result)

classTree = TreeNode(13, TreeNode(6, TreeNode(4), TreeNode(8)) , TreeNode(21, TreeNode(15), TreeNode(24, None, TreeNode(26))))
printPreOrder(classTree)


def printPostOrder(root):
    result = []

    # Left -> Root -> Right
    def postOrderHelper(node):
        nonlocal result
        if not node:
            return
        
        # recurse left
        postOrderHelper(node.left)
        # recurse right
        postOrderHelper(node.right)
        # append the value to result list
        result.append(node.val)


    postOrderHelper(root)
    print(result)

printPostOrder(classTree)

# returns True if a node that has this value in the tree
def findNode(root, value):
    if not root:
        return False
    
    if root.val == value:
        return True
    elif root.val < value:
        return findNode(root.right, value)
    else:
        return findNode(root.left, value)
    
print(findNode(classTree, 21)) #True
print(findNode(classTree, 20)) #False

