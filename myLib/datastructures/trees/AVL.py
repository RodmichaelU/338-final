from myLib.datastructures.nodes import TNode
from BST import BST

class AVL(BST):
    def __init__(self, val = None):
        super().__init__()  # call parent constructor
        if val is not None:
            self.root = self.TNode(val)

    def AVL(self, obj):
        """
        Overload constructor to create an AVL tree from a TNode obj
        """
        self.root = obj  # use TNode obj as the root of the tree
        if obj.left is not None or obj.right is not None:
            # if obj has children create a balanced tree from it iteratively inserting nodes from the original tree and balancing
            # the new created AVL tree
            nodes = []  # list to store nodes in BFS order
            nodes.append(obj)
            i = 0
            while i < len(nodes):
                node = nodes[i]
                i += 1
                if node.left is not None:
                    nodes.append(node.left)
                if node.right is not None:
                    nodes.append(node.right)
            nodes.reverse()  # reverse the list to insert nodes in reverse BFS order
            for node in nodes:
                self.insert(node)

    """
    def __init__(self, val):
            self.root = TNode(val)
    """

    def set_root(self, node):
        if node is None:
            self.root = None
        else:
            self.root = self.__create_balanced_avl_tree(node)

    def get_root(self):
        return self.root
    
    def __create_balanced_avl_tree(self, node):
        """
        Helper function to create a balanced AVL tree starting from the given node
        """
        if node is None:
            return None
        
        new_node = self.TNode(node.val)
        new_node.left = self.__create_balanced_avl_tree(node.left)
        new_node.right = self.__create_balanced_avl_tree(node.right)
        
        self.balance(new_node)
        
        return new_node

    def balance(self, node):
        """
        Helper function to balance the AVL tree starting from the given node
        """
        if node is None:
            return 0

        left_height = self.balance(node.left)  # recursively balance left subtree
        right_height = self.balance(node.right)  # recursively balance right subtree

        balance_factor = left_height - right_height  # calculate balance factor

        # check if tree is unbalanced and perform rotations accordingly
        if balance_factor > 1:  # left heavy
            if self.get_height(node.left.left) >= self.get_height(node.left.right):
                node = self.rotate_right(node)
            else:
                node.left = self.rotate_left(node.left)
                node = self.rotate_right(node)
        elif balance_factor < -1:  # right heavy
            if self.get_height(node.right.right) >= self.get_height(node.right.left):
                node = self.rotate_left(node)
            else:
                node.right = self.rotate_right(node.right)
                node = self.rotate_left(node)

        return max(left_height, right_height) + 1

    def insert(self, val):
        """
        Inserts a node with the given value into the AVL tree while maintaining
        the balance of the tree
        """
        super().insert(val)  # call parent insert method
        self.balance(self.root)  # balance the tree starting from the root

    def delete(self, val):
        """
        Deletes the node with the given value from the AVL tree while maintaining
        the balance of the tree
        """
        super().delete(val)  # call parent delete method
        self.balance(self.root)  # balance the tree starting from the root
