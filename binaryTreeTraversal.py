class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_traversal(tree.root, "")

        if traversal_type == "inorder":
            return self.inorder_traversal(tree.root, "")

        if traversal_type == "postorder":
            return self.postorder_traversal(tree.root, "")

        else:
            print("Traversal type " + str(traversal_type) + " is not supported")
            return False

    def preorder_traversal(self, node, traversal):
        # Root -> Left -> Right , consider for the pre part you will get the root first
        if node:
            traversal += (str(node.value) + "-")
            traversal = self.preorder_traversal(node.left, traversal)
            traversal = self.preorder_traversal(node.right, traversal)
        return traversal

    def inorder_traversal(self, node, traversal):
        # left -> root -> right
        if node:
            traversal = self.inorder_traversal(node.left, traversal)
            traversal += (str(node.value) + "-")
            traversal = self.inorder_traversal(node.right, traversal)
        return traversal

    def postorder_traversal(self, node, traversal):
        # Left -> Right -> Root
        if node:
            traversal = self.postorder_traversal(node.left, traversal)
            traversal = self.postorder_traversal(node.right, traversal)
            traversal += (str(node.value) + "-")
        return traversal

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)

print(tree.print_tree("preorder"))
print(tree.print_tree("inorder"))
print(tree.print_tree("postorder"))
