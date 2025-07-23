# Instructor Demo

# BST

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

# reg linked list
class ListNode:
    def __init__(self, key):
        self.value = key
        self.next = None

def insert(root, key):
    # if the tree is empty, create anew node with the key and return it
    if root is None:
        return TreeNode(key)
    else:
        # if key is greater than current node val -> insert in R subtree
        if root.value < key:
            root.right = insert(root.right, key)
        # if the key is smaller than current node val -> insert in L subtree
        else: 
            root.left = insert(root.left, key)
    # return the unchanged root node to maintain the tree structure
    return root


# create the root node
root = TreeNode(13)

# create left subtree
root.left = TreeNode(6)
root.left.left = TreeNode(4)
root.left.right = TreeNode(8)

# create the right subtree
root.right = TreeNode(21)
root.right.left = TreeNode(15)
root.right.right = TreeNode(24)
root.right.right.right = TreeNode(26)