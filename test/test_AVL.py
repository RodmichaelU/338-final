from myLib.datastructures.trees.BST import BST
from myLib.datastructures.trees.AVL import AVL
from myLib.datastructures.nodes.TNode import TNode

def test_AVL_constructor():
    avl = AVL()
    assert avl.root == None

def test_AVL_constructor_with_value():
    avl = AVL(5)
    assert avl.root.data == 5

def test_AVL_insert():
    avl = AVL(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    avl.insert(9)
    assert avl.root.right.right.right.data == 9

def test_AVL_insert_node():
    avl = AVL(5)
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None
    node = Node(9)
    avl.insert_node(node)
    assert avl.root.right.right.right.data == 9


def test_AVL_delete():
    avl = AVL(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    avl.delete(7)
    assert avl.root.right.data == 8

def test_AVL_search():
    avl = AVL(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    assert avl.Search(7).data == 7
    assert avl.Search(10) == None

def test_AVL_set_root():
    avl = AVL(5)
    class Node:
        def __init__(self, val):
            self.data = val
            self.left = None
            self.right = None
    node = Node(9)
    avl.set_root(node)
    assert avl.root.data == 9


def test_AVL_get_root():
    avl = AVL(5)
    assert avl.get_root().data == 5


def test_AVL_printInOrder(capsys):
    avl = AVL(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    avl.printInOrder()
    captured = capsys.readouterr()
    assert captured.out == "2 3 4 5 6 7 8 "


def test_AVL_printBF(capsys):
    avl = AVL(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    avl.printBF()
    captured = capsys.readouterr()
    assert captured.out == "5 3 7 2 4 6 8 "

"""
def test_AVL_balancing_performance():
        avl = AVL()
        for i in range(8191):
            avl.insert(i)
        assert avl.root.height <= 13

"""


def test_AVL_duplicate_values():
    avl = AVL(5)
    avl.insert(3)
    avl.insert(7)
    avl.insert(2)
    avl.insert(4)
    avl.insert(6)
    avl.insert(8)
    assert avl.search(5) is not None
    assert avl.search(9) is None
    avl.delete(5)
    assert avl.search(5) is None
    assert avl.search(4) is not None
    avl.delete(5)
    assert avl.search(5) is None
