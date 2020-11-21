class Bst:
    """Binary Search Tree

    Supports the following methods:
      - insert: adds a value to the BST
      - search: checks whether a value exists in the BST or not
      - inorder: traverses and returns the nodes of the BST following in-order sequence
    """

    class Node:
        """ BST Tree node """

        def __init__(self, key):
            self.left = None
            self.right = None
            self.val = key

    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Inserts a key in the BST
        """
        self.root = Bst.__insert(self.root, key)

    @staticmethod
    def __insert(node, key):
        if node is None:
            node = Bst.Node(key)
        else:
            if node.val == key:
                return node
            elif key < node.val:
                node.left = Bst.__insert(node.left, key)
            else:
                node.right = Bst.__insert(node.right, key)

        return node

    def search(self, key):
        """
        Indicates whether a key exists in the BST or not
        """
        return Bst.__search(self.root, key)

    @staticmethod
    def __search(node, key):
        if node is None:
            return False
        else:
            if node.val == key:
                return True
            elif key < node.val:
                return Bst.__search(node.left, key)
            else:
                return Bst.__search(node.right, key)

    def inorder(self) -> list:
        """
        Returns a list of keys that corresponds to the BST traversal
        """
        return Bst.__inorder(self.root)

    @staticmethod
    def __inorder(node) -> list:
        if not node:
            return []
        return Bst.__inorder(node.left) + [node.val] + Bst.__inorder(node.right)
