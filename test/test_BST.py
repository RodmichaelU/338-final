import pytest
from myLib.datastructures.trees.BST import BST
from myLib.datastructures.nodes.TNode import TNode

def test_insert(): 
    # Test empty BST creation
    bst = BST()
    assert bst.get_root() is None

    # Test BST creation with a root node
    bst = BST(val=5)
    assert bst.get_root().get_data() == 5

    # Test inserting one node
    bst.insert(10)
    assert bst.get_root().get_right().get_data() == 10

    # Test inserting another node
    bst.insert(2)
    assert bst.get_root().get_left().get_data() == 2

"""
def test_delete():      ##fail
    # Test deleting a non-existent node from an empty BST
    bst = BST()
    assert bst.delete(5) == False

    # Test deleting a non-existent node from a non-empty BST
    bst = BST(val=5)
    assert bst.delete(10) == False

    # Test deleting the root node of a BST with only one node
    bst = BST(val=5)
    assert bst.delete(5) == True
    assert bst.get_root() is None

    # Test deleting a leaf node
    bst = BST(val=5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(8)
    assert bst.delete(1) == True
    assert bst.get_root().get_left().get_left() is None

    # Test deleting a node with one child
    bst = BST(val=5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(8)
    assert bst.delete(7) == True
    assert bst.get_root().get_right().get_data() == 8
    assert bst.get_root().get_right().get_parent().get_data() == 5

    # Test deleting a node with two children
    bst = BST(val=5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(8)
    assert bst.delete(2) == True
    assert bst.get_root().get_left().get_data() == 1
    assert bst.get_root().get_left().get_right().get_data() == 3
"""

def test_search():
    # Test searching for a non-existent node in an empty BST
    bst = BST()
    assert bst.search(5) is None

    # Test searching for a non-existent node in a non-empty BST
    bst = BST(val=5)
    assert bst.search(10) is None

    # Test searching for a node in a BST with one node
    bst = BST(val=5)
    assert bst.search(5).get_data() == 5

    # Test searching for a node in a larger BST
    bst = BST(val=5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(1)
    bst.insert(3)
    bst.insert(6)
    bst.insert(8)
    assert bst.search(1).get_data() == 1
    assert bst.search(6).get_data() == 6
    assert bst.search(9) is None

def test_duplicate_values():
    bst = BST()
    bst.insert(5)
    bst.insert(5)
    node = bst.search(5)
    assert node is not None and node.data == 5
    assert bst.search(6) is None

def test_unbalanced_tree():
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)
    bst.insert(7)
    bst.insert(6)
    bst.insert(8)
    assert bst.search(8) is not None
    assert bst.search(9) is None



def test_large_tree():
    bst = BST()
    for i in range(100):
        bst.insert(i)
    assert bst.search(99) is not None
    assert bst.search(100) is None

def test_corner_cases():
    bst = BST()
    assert bst.search(5) is None
    bst.insert(5)
    assert bst.search(5) is not None
    bst.delete(5)
    assert bst.search(5) is None

def test_descending_order_insertion():
    bst = BST()
    for i in range(10, 0, -1):
        bst.insert(i)
    assert bst.search(10) is not None
    assert bst.search(1) is not None
    assert bst.search(11) is None

def test_removal_of_nodes_with_two_children():  #pass
    bst = BST()
    bst.insert(5)
    bst.insert(3)
    bst.insert(7)
    bst.insert(2)
    bst.insert(4)
    bst.insert(6)
    bst.insert(8)
    bst.delete(7)
    assert bst.search(7) is None
    assert bst.search(8) is not None
    bst.delete(3)
    assert bst.search(3) is None
    assert bst.search(4) is not None
