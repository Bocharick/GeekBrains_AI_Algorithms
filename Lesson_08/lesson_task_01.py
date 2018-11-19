from binarytree import tree, bst

class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


a = bst(height=3, is_perfect=True)
print(a)

a = a + 555

