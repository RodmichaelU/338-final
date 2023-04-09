from myLib.datastructures.Linear.SLL import SLL
from myLib.datastructures.nodes.SNode import SNode
import pytest

def test_insert_head():
    sll = SLL()
    sll.insert_head(SNode(1))
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1

def test_insert_tail():
    sll = SLL()
    sll.insert_tail(SNode(1))
    assert sll.head.data == 1
    assert sll.tail.data == 1
    assert sll.size == 1

def test_insert():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 1)
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3

def test_sorted_insert():
    sll = SLL()
    sll.sorted_insert(SNode(2))
    sll.sorted_insert(SNode(1))
    sll.sorted_insert(SNode(3))
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 3

def test_search():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 1)
    node = sll.search(2)
    assert node.data == 2

def test_delete_head():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.delete_head()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0

def test_delete_tail():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.delete_tail()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0

def test_delete():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 1)
    sll.delete(2)
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 2

def test_sort():
    sll = SLL()
    sll.insert(SNode(3), 0)
    sll.insert(SNode(2), 0)
    sll.insert(SNode(1), 0)
    sll.sort()
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 3

def test_clear():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.clear()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0

def test_empty_list():
    sll = SLL()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0

def test_insert_middle():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(3), 1)
    sll.insert(SNode(2), 1)
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 3

def test_sorted_insert_duplicate():
    sll = SLL()
    sll.sorted_insert(SNode(1))
    sll.sorted_insert(SNode(1))
    sll.sorted_insert(SNode(2))
    assert sll.head.data == 1
    assert sll.tail.data == 2
    assert sll.size == 3

def test_search_not_found():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 1)
    node = sll.search(4)
    assert node is None

def test_delete_empty_list():
    sll = SLL()
    with pytest.raises(RuntimeError, match="Cannot Delete From an Empty List"):
        sll.delete(1)

def test_delete_not_found():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 1)
    with pytest.raises(ValueError, match="Node Not Found"):
        sll.delete(4)

def test_delete_middle():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 1)
    sll.delete(2)
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 2

def test_sort_already_sorted():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 2)
    sll.sort()
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 3

def test_sort_reverse_sorted():
    sll = SLL()
    sll.insert(SNode(3), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(1), 2)
    sll.sort()
    assert sll.head.data == 1
    assert sll.tail.data == 3
    assert sll.size == 3

def test_clear_non_empty_list():
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 2)
    sll.clear()
    assert sll.head is None
    assert sll.tail is None
    assert sll.size == 0

def test_sll_print(capfd):
    sll = SLL()
    sll.insert(SNode(1), 0)
    sll.insert(SNode(2), 1)
    sll.insert(SNode(3), 2)

    sll.print()
    
    captured = capfd.readouterr()
    expected_output = "List length: 3\nSorted status: Yes\nList content:\n1 -> 2 -> 3 -> None\n"
    assert captured.out == expected_output

