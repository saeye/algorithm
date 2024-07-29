class TreeNode(self, node):
    self.node = node
    self.left = None
    self.right = None
class BinaryTree:
    def __init__(self):
        self.root = TreeNode(self.node)

    def preorder(self, node):
        if node:
            print(node.node)
            self.preorder(node.left)
            self.preorder(node.right)

    def inorder(self, node):
        if node:
            self.preorder(node.left)
            print(node.node)
            self.inorder(node.right)

    def postorder(self, node):
        if node:
            self.preorder(node.left)
            self.preorder(node.right)
            print(node.node)

